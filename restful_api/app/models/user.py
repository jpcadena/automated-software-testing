"""
A module for user in the restful api.app.models package.
"""

from typing import Any, Optional, Type

from sqlalchemy import CheckConstraint, Integer, String
from sqlalchemy.orm import Mapped, Session, mapped_column
from werkzeug.security import generate_password_hash

from restful_api.app.db.db import Base


class User(Base):  # type: ignore
    """
    SQLAlchemy model for user.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        index=True,
        nullable=False,
        primary_key=True,
        unique=True,
        comment="ID of the user",
    )
    username: Mapped[str] = mapped_column(
        String(80),
        nullable=False,
        comment="Name of the user",
    )
    password: Mapped[str] = mapped_column(
        String(24),
        nullable=False,
        comment="Password of the user",
    )

    __table_args__ = (
        CheckConstraint(
            "length(username) >= 4",
            name="users_username_length",
        ),
        CheckConstraint(
            "length(password) >= 8",
            name="users_password_length",
        ),
    )

    def __init__(self, username: str, password: str, **kw: Any) -> None:
        super().__init__(**kw)
        self.username: str = username
        self.password: str = password

    def json(self) -> dict[str, Any]:
        """
        Convert the user instance to a dictionary.
        :return: A dictionary representation of the user.
        :rtype: dict[str, Any]
        """
        return {
            "username": self.username,
            "password": self.password,
        }

    @classmethod
    def find_by_username(
        cls: Type[Base],  # type: ignore
        session: Session,
        username: str,
    ) -> Optional["User"]:
        """
        Find a user by its name.
        :param session: The SQLAlchemy session to use for the query.
        :type session: Session
        :param username: The username of the user to find.
        :type username: str
        :return: The user instance if found, None otherwise.
        :rtype: Optional[User]
        """
        return session.query(cls).filter_by(username=username).first()

    @classmethod
    def find_by_id(
        cls: Type[Base],  # type: ignore
        session: Session,
        _id: int,
    ) -> Optional["User"]:
        """
        Find a user by its name.
        :param session: The SQLAlchemy session to use for the query.
        :type session: Session
        :param _id: The ID of the user to find.
        :type _id: int
        :return: The user instance if found, None otherwise.
        :rtype: Optional[User]
        """
        return session.query(cls).filter_by(id=_id).first()

    def save_to_db(self, session: Session) -> None:
        """
        Save the user to the database.
        :param session: The SQLAlchemy session to use for the operation.
        :type session: Session
        :return: None
        :rtype: NoneType
        """
        session.add(self)
        session.commit()

    def set_password(self, password: str) -> None:
        """
        Hash the password and store it.
        :param password: The plaintext password
        """
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """
        Check the hashed password.
        :param password: The plaintext password
        :return: True if passwords match, False otherwise
        """
        print("Checking password")
        print(password, self.password)
        # return check_password_hash(self.password, password)
        return self.password == password

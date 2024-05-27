"""
A module for store in the restful api.app.models package.
"""

from typing import TYPE_CHECKING, Any, Optional, Type

from sqlalchemy import CheckConstraint, Integer, String
from sqlalchemy.orm import Mapped, Session, mapped_column, relationship

from restful_api.app.db.db import Base

if TYPE_CHECKING:
    from ..models.item import Item


class Store(Base):  # type: ignore
    """
    Store model class representing the "store" table
    """

    __tablename__ = "store"

    id: Mapped[int] = mapped_column(
        Integer,
        index=True,
        nullable=False,
        primary_key=True,
        unique=True,
        comment="ID of the store",
    )
    name: Mapped[str] = mapped_column(
        String(80),
        nullable=False,
        comment="Name of the item",
    )
    items: Mapped[list["Item"]] = relationship(
        "Item",
        back_populates="store",
        lazy="dynamic",
    )

    __table_args__ = (
        CheckConstraint(
            "length(name) >= 4",
            name="store_name_length",
        ),
    )

    def __init__(self, name: str, **kw: Any) -> None:
        super().__init__(**kw)
        self.name: str = name

    def json(self) -> dict[str, Any]:
        """
        Convert the store instance to a dictionary.
        :return: A dictionary representation of the store.
        :rtype: dict[str, Any]
        """
        return {
            "name": self.name,
            "items": [item.json() for item in self.items],
        }

    @classmethod
    def find_by_name(
        cls: Type[Base],  # type: ignore
        session: Session,
        name: str,
    ) -> Optional["Store"]:
        """
        Find a store by its name.
        :param session: The SQLAlchemy session to use for the query.
        :type session: Session
        :param name: The name of the store to find.
        :type name: str
        :return: The store instance if found, None otherwise.
        :rtype: Optional[Item]
        """
        return session.query(cls).filter_by(name=name).first()

    def save_to_db(self, session: Session) -> None:
        """
        Save the store to the database.
        :param session: The SQLAlchemy session to use for the operation.
        :type session: Session
        :return: None
        :rtype: NoneType
        """
        session.add(self)
        session.commit()

    def delete_from_db(self, session: Session) -> None:
        """
        Delete the store from the database.
        :param session: The SQLAlchemy session to use for the operation.
        :type session: Session
        :return: None
        :rtype: NoneType
        """
        session.delete(self)
        session.commit()

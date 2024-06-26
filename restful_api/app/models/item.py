"""
A module for item in the restful_api-models package.
"""

from typing import TYPE_CHECKING, Any, Optional, Type

from sqlalchemy import CheckConstraint, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, Session, mapped_column, relationship

from restful_api.app.db.db import Base

if TYPE_CHECKING:
    from ..models.store import Store


class Item(Base):  # type: ignore
    """
    SQLAlchemy model for items.
    """

    __tablename__ = "items"

    id: Mapped[int] = mapped_column(
        Integer,
        index=True,
        nullable=False,
        primary_key=True,
        unique=True,
        comment="ID of the item",
    )
    name: Mapped[str] = mapped_column(
        String(80),
        nullable=False,
        comment="Name of the item",
    )
    price: Mapped[float] = mapped_column(
        Float(
            precision=2,
        ),
        nullable=False,
        comment="Price of the item",
    )
    store_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "store.id",
            name="store_id_fkey",
        ),
        nullable=False,
        comment="ID of the store",
    )
    store: Mapped["Store"] = relationship(
        "Store",
        back_populates="items",
        lazy="joined",
    )

    __table_args__ = (
        CheckConstraint(
            "length(name) >= 4",
            name="items_name_length",
        ),
        CheckConstraint(
            "price >= 0.0",
            name="items_price_non_negative",
        ),
    )

    def __init__(
        self, name: str, price: float, store_id: int, **kw: Any
    ) -> None:
        super().__init__(**kw)
        self.name: str = name
        self.price: float = price
        self.store_id: int = store_id

    def json(self) -> dict[str, Any]:
        """
        Convert the item instance to a dictionary.
        :return: A dictionary representation of the item.
        :rtype: dict[str, Any]
        """
        return {
            "name": self.name,
            "price": self.price,
            "store_id": self.store_id,
        }

    @classmethod
    def find_by_name(
        cls: Type[Base],  # type: ignore
        session: Session,
        name: str,
    ) -> Optional["Item"]:
        """
        Find an item by its name.
        :param session: The SQLAlchemy session to use for the query.
        :type session: Session
        :param name: The name of the item to find.
        :type name: str
        :return: The item instance if found, None otherwise.
        :rtype: Optional[Item]
        """
        return session.query(cls).filter_by(name=name).first()

    def save_to_db(self, session: Session) -> None:
        """
        Save the item to the database.
        :param session: The SQLAlchemy session to use for the operation.
        :type session: Session
        :return: None
        :rtype: NoneType
        """
        session.add(self)
        session.commit()

    def delete_from_db(self, session: Session) -> None:
        """
        Delete the item from the database.
        :param session: The SQLAlchemy session to use for the operation.
        :type session: Session
        :return: None
        :rtype: NoneType
        """
        session.delete(self)
        session.commit()

import datetime
import enum
from sqlalchemy import MetaData, Table, Column, Integer, String, text, ForeignKey
from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated
from pydantic import Field


metadata_obj = MetaData()

# workers_table = Table(
#     "workers",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("user_name", String)
# )

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.datetime.utcnow,
)]


tax_limit = Annotated[int, Field(
    gt=0, le=10000, description='value gt 0 less 10000')]


class Status(enum.Enum):
    starting = 'starting'
    in_progress = 'in progress'
    rejected = 'rejected'
    closed = 'closed'


class UsersType(enum.Enum):
    admin = 'admin'
    consumer = 'consumer'
    contractor = 'contractor'


class UsersData(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    type: Mapped[UsersType] = mapped_column(default='consumer')


class Consumers(Base):
    __tablename__ = 'consumers'
    id: Mapped[int] = mapped_column(primary_key=True)
    consumer_id: Mapped[int] = mapped_column(ForeignKey='users.id')


class Contractors(Base):
    __tablename__ = 'contractors'
    id: Mapped[int] = mapped_column(primary_key=True)
    contractor_id: Mapped[int] = mapped_column(ForeignKey='users.id')


class Orders(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    consumer_id: Mapped[int] = mapped_column(ForeignKey='users.id')
    contractor_id: Mapped[int] = mapped_column(ForeignKey='users.id')
    description: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    status: Mapped[Status]


class FeedBack(Base):
    __tablename__ = 'feedback'
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey='orders.id')
    description: Mapped[str]
    rating: Mapped[int]

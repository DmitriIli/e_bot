import datetime
import enum
from sqlalchemy import MetaData, Table, Column, Integer, String, text
from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated
from pydantic import Field


metadata_obj = MetaData()

workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_name", String)
)

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"),
    onupdate=datetime.datetime.utcnow,
)]

tax_limit = Annotated[int, Field(gt=0, le=10000, description='value gt 0 less 10000')]


class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"


class WorkersORM(Base):
    __tablename__ = "workers"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    tax: Mapped[tax_limit]
    workload: Mapped[Workload] 

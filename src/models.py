import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, text
from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated

metadata_obj = MetaData()

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())")
    onupdate=datetime.datetime.utcnow,
    )]



workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_name", String)
)


class WorkersORM(Base):
    __tablename__ = "workers"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


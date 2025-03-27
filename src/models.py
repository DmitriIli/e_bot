from sqlalchemy import MetaData, Table, Column, Integer, String
from database import Base
from sqlalchemy.orm import Mapped, mapped_column

metadata_obj = MetaData()

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

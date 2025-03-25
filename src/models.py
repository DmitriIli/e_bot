from sqlalchemy import MetaData, Table, Column, Integer, String


metadata_obj = MetaData()


workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_name", String)
)

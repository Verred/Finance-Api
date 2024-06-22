from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Boolean
from config.db import meta, engine

users = Table(
    "users", meta,
    Column("id_cliente", Integer, primary_key=True),
    Column("nombre", String(50)),
    Column("Contrasena", String(30)),
    Column("Fecha_creacion", DateTime),
    Column("estado_usuario", Boolean),
    Column("edad", Integer),
    Column("dni", String(8)),
    Column("correo", String(30)),
    Column("celular", String(9))
)

meta.create_all(engine)
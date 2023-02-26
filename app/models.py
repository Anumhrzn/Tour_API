from email.policy import default
from enum import auto
from optparse import Option
from app.db import db
from pony.orm import PrimaryKey, Required, Optional, LongStr


class User(db.Entity):
    __table__ = "user table"

    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)


class Places(db.Entity):
    __table__ = "places table"

    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    image = Required(str)
    description = Optional(LongStr, default="")

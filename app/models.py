from email.policy import default
from enum import auto
from optparse import Option
from app.db import db
from pony.orm import PrimaryKey, Required, Optional


class User(db.Entity):
    __table__ = "user table"

    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)


class Candidate(db.Entity):
    __table__ = "candidate table"

    id = PrimaryKey(int, auto=True)
    candidate_id = Required(str, unique=True)
    first_name = Required(str)
    middle_name = Optional(str, default="")
    last_name = Required(str)
    post = Required(str)
    image = Optional(str, default="")


class Voter(db.Entity):
    __table__ = "voter table"

    id = PrimaryKey(int, auto=True)
    voter_id = Required(str, unique=True)
    first_name = Required(str)
    middle_name = Optional(str, default="")
    last_name = Required(str)
    image = Optional(str, default="")


class Admin(db.Entity):
    __table__ = "admin table"

    id = PrimaryKey(int, auto=True)
    admin_id = Required(str, unique=True)
    first_name = Required(str)
    middle_name = Optional(str, default="")
    last_name = Required(str)
    image = Optional(str, default="")


class AdminCredential(db.Entity):
    __table__ = "admin_credential table"

    id = PrimaryKey(int, auto=True)
    admin_id = Required(str, unique=True)
    password = Required(str)

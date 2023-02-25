SQL_ADD_USER = """
INSERT INTO "User" (name)
VALUES ('{name}');
"""

SQL_ADD_PLACE = """
INSERT INTO "Places" (name,image,description)
VALUES ('{name}','{image}','{description}');
"""
SQL_GET_PLACE_BY_NAME = """
select * from "Places" where name='{name}';
"""

SQL_ADD_USER = """
INSERT INTO "User" (name,password)
VALUES ('{name}','{password}');
"""

SQL_ADD_PLACE = """
INSERT INTO "Places" (name,image,description)
VALUES ('{name}','{image}','{description}');
"""
SQL_GET_PLACE_BY_NAME = """
select * from "Places" where name='{name}';
"""

SQL_GET_USER_BY_NAME = """
select * from "User" where name='{name}';
"""

SQL_ADD_USER_RATINGS = """
INSERT INTO "Ratings"(name,place_name,rating,description)
VALUES ('{name}','{place_name}','{rating}','{description}')
"""

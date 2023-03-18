SQL_ADD_USER = """
INSERT INTO "User" (name,password)
VALUES ('{name}','{password}');
"""

SQL_ADD_PLACE = """
INSERT INTO "Places" (name,image,description,latitude,longitude)
VALUES ('{name}','{image}','{description}','{latitude}','{longitude}');
"""

SQL_UPDATE_PLACE = """
UPDATE "Places"
SET latitude = '{latitude}' , longitude = '{longitude}'
WHERE name = '{name}'
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

SQL_GET_RATINGS_BY_PLACE_NAME = """
select * from "Ratings" where place_name='{place_name}';
"""

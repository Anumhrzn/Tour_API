SQL_CANDIDATES = """
select * from "Candidate" order by id desc
"""

SQL_ADD_CANDIDATE = """
INSERT INTO "Candidate" (candidate_id,first_name,middle_name,last_name,post,image)
VALUES ('{candidate_id}','{first_name}','{middle_name}','{last_name}','{post}','{image}');
"""

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

SQL_DELETE_CANDIDATE = """
delete from "Candidate" where candidate_id='{candidate_id}'
"""

SQL_UPDATE_CANDIDATE = """
update "Candidate" 
set first_name='{first_name}', middle_name='{middle_name}', last_name='{last_name}', post='{post}', image='{image}'
where candidate_id='{candidate_id}'
"""

SQL_VOTERS = 'select * from "Voter"'

SQL_SINGLE_VOTER_BY_ID = """
select * from "Voter" where voter_id='{voter_id}'
"""

SQL_ADD_VOTER = """
INSERT INTO "Voter" (voter_id,first_name,middle_name,last_name,image)
VALUES ('{voter_id}','{first_name}','{middle_name}','{last_name}','{image}');
"""

SQL_DELETE_VOTER = """
delete from "Voter" where voter_id='{voter_id}'
"""

SQL_UPDATE_VOTER = """
update "Voter" 
set first_name='{first_name}', middle_name='{middle_name}', last_name='{last_name}',image='{image}'
where voter_id='{voter_id}'
"""
SQL_SINGLE_ADMIN_CREDENTIAL_BY_ID = """
select * from "AdminCredential" where admin_id='{admin_id}'
"""

SQL_SINGLE_ADMIN_BY_ID = """
select * from "Admin" where admin_id='{admin_id}'
"""

SQL_ADD_ADMIN = """
INSERT INTO "Admin" (admin_id,first_name,middle_name,last_name,image)
VALUES ('admin','Nabin','','Kawan','localhost:5000/static/images/d07907be811379588986.jpeg');
"""

SQL_ADD_ADMIN_CREDENTIAL = """
INSERT INTO "AdminCredential" (admin_id,password)
VALUES ('admin','admin');
"""

from pony.orm import db_session
from fastapi import HTTPException
from app.dbsync.sql import SQL_ADD_ADMIN, SQL_ADD_ADMIN_CREDENTIAL, SQL_ADD_CANDIDATE, SQL_ADD_USER, SQL_ADD_VOTER, SQL_CANDIDATES, SQL_DELETE_CANDIDATE, SQL_DELETE_VOTER, SQL_SINGLE_ADMIN_BY_ID, SQL_SINGLE_ADMIN_CREDENTIAL_BY_ID, SQL_SINGLE_VOTER_BY_ID, SQL_UPDATE_CANDIDATE, SQL_UPDATE_VOTER, SQL_VOTERS
from app.schemas import CandidateCreate, VoterCreate, UserCreate
from app.models import Candidate
from app.db import db
from pony.orm.dbapiprovider import IntegrityError


class UserService:
    @db_session
    def create_user(self, user_ob: UserCreate):
        sql = SQL_ADD_USER.format(
            name=user_ob.name
        )
        try:
            db.execute(sql)
        except IntegrityError:
            raise HTTPException(
                status_code=409, detail="User already registered")


class CandidateService:
    @db_session
    def create_candidate(self, candidate_ob: CandidateCreate):
        sql = SQL_ADD_CANDIDATE.format(candidate_id=candidate_ob.candidate_id.upper(),
                                       first_name=candidate_ob.first_name,
                                       middle_name=candidate_ob.middle_name,
                                       last_name=candidate_ob.last_name,
                                       post=candidate_ob.post.upper(),
                                       image=candidate_ob.image)
        try:
            db.execute(sql)
        except IntegrityError:
            raise HTTPException(
                status_code=409, detail="Candidate already registered")

    @db_session
    def get_all_candidates(self):
        sql = SQL_CANDIDATES
        cursor = db.execute(sql)

        candidates = []
        for row in cursor.fetchall():
            id, candidate_id, first_name, middle_name, last_name, post, image = row
            document = {
                'candidate_id': candidate_id,
                'first_name': first_name,
                'middle_name': middle_name,
                'last_name': last_name,
                'post': post,
                'image': image
            }

            candidates.append(document)

        return candidates

    @db_session
    def delete_candidate(self, candidate_id: str):
        sql = SQL_DELETE_CANDIDATE.format(candidate_id=candidate_id.upper())

        db.execute(sql)

    @db_session
    def update_candidate(self, candidate_ob: CandidateCreate):
        sql = SQL_UPDATE_CANDIDATE.format(
            candidate_id=candidate_ob.candidate_id.upper(),
            first_name=candidate_ob.first_name,
            middle_name=candidate_ob.middle_name,
            last_name=candidate_ob.last_name,
            post=candidate_ob.post.upper(),
            image=candidate_ob.image)

        db.execute(sql)


class VoterService:

    @db_session
    def get_all_voters(self):
        sql = SQL_VOTERS
        cursor = db.execute(sql)

        voters = []
        for row in cursor.fetchall():
            id, voter_id, first_name, middle_name, last_name, image = row
            document = {
                'voter_id': voter_id,
                'first_name': first_name,
                'middle_name': middle_name,
                'last_name': last_name,
                'image': image
            }

            voters.append(document)

        return voters

    @db_session
    def get_voter_by_id(self, voter_id):
        sql = SQL_SINGLE_VOTER_BY_ID.format(voter_id=voter_id)
        cursor = db.execute(sql)
        voters = []
        for row in cursor.fetchall():
            id, voter_id, first_name, middle_name, last_name, image = row
            document = {
                'voter_id': voter_id,
                'first_name': first_name,
                'middle_name': middle_name,
                'last_name': last_name,
                'image': image
            }

            voters.append(document)

        return voters

    @db_session
    def create_voter(self, voter_ob: VoterCreate):
        sql = SQL_ADD_VOTER.format(voter_id=voter_ob.voter_id.upper(),
                                   first_name=voter_ob.first_name,
                                   middle_name=voter_ob.middle_name,
                                   last_name=voter_ob.last_name,
                                   image=voter_ob.image)
        try:
            db.execute(sql)
        except IntegrityError:
            raise HTTPException(
                status_code=409, detail="Voter already registered")

    @db_session
    def delete_voter(self, voter_id: str):
        sql = SQL_DELETE_VOTER.format(voter_id=voter_id.upper())

        db.execute(sql)

    @db_session
    def update_voter(self, voter_ob: VoterCreate):
        sql = SQL_UPDATE_VOTER.format(
            voter_id=voter_ob.voter_id.upper(),
            first_name=voter_ob.first_name,
            middle_name=voter_ob.middle_name,
            last_name=voter_ob.last_name,
            image=voter_ob.image)

        db.execute(sql)


class AdminService:

    @db_session
    def initialize_admin(self):
        sql1 = SQL_ADD_ADMIN
        sql2 = SQL_ADD_ADMIN_CREDENTIAL

        try:
            db.execute(sql1)
            db.execute(sql2)

        except:
            print("already exist")

    @db_session
    def get_admin_credential_by_id(self, admin_id):
        sql = SQL_SINGLE_ADMIN_CREDENTIAL_BY_ID.format(admin_id=admin_id)
        cursor = db.execute(sql)
        admin_credential = {}
        for row in cursor.fetchall():
            id, admin_id, password = row
            document = {
                'admin_id': admin_id,
                'password': password
            }

            admin_credential = document

        return admin_credential

    @db_session
    def get_admin_by_id(self, admin_id):
        sql = SQL_SINGLE_ADMIN_BY_ID.format(admin_id=admin_id)
        cursor = db.execute(sql)
        admin = {}
        for row in cursor.fetchall():
            id, admin_id, first_name, middle_name, last_name, image = row
            document = {
                'admin_id': admin_id,

                'first_name': first_name,
                'middle_name': middle_name,
                'last_name': last_name,
                'image': image
            }

            admin = document

        return admin

from pony.orm import Database, PrimaryKey, Required
# # Package # #

db = Database()


def init_local_db():
    db.bind(provider='sqlite', filename='bbvs_new.db', create_db=True)
    db.generate_mapping(create_tables=True)

# def init_db():
#     db.bind(provider=db_settings.provider,
#                  user=db_settings.user,
#                  password=db_settings.password,
#                  host=db_settings.host,
#                  port=db_settings.port,
#                  database=db_settings.database)
#     db.generate_mapping(create_tables=True)


if __name__ == '__main__':
    init_local_db()
    # db.drop_all_tables(with_all_data=True)

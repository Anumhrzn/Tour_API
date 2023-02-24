import time
# from decouple import config
from jose import jwt


# JWT_SECRET = config('JWT_SECRET')
# JWT_ALGORITHM = config('JWT_ALGORITHM')
#
# print(JWT_SECRET)
# print(JWT_ALGORITHM)


# returns generated token


def generate_token_response(user_id: str, token: str):
    return {
        'user_id': user_id,
        'access_token': token
    }


# Functions used for signing jwt string


def sign_jwt(user_id: str, end_time_ms=5 * 60 * 1000):
    pass


def decode_jwt(token: str):
    pass

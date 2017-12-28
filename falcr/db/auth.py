import jwt
from falcr.config import getLogger

SECRET = 'secret'
ALGO = 'HS256'
log = getLogger(__name__)


def valid_token(token):
    try:
        jwt.decode(
            token,
            SECRET,
            verify='True',
            algorithms=[ALGO],
            options={
                'verify_exp': True
            }
        )
        return True
    except jwt.DecodeError:
        return False


def get_token(user):
    return dict(token=jwt.encode(user, SECRET, algorithm=ALGO))

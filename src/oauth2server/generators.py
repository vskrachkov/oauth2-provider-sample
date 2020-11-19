from django.utils.crypto import get_random_string
from oauth2_provider.generators import BaseHashGenerator
from oauthlib.common import Request


def generate_access_token(request: Request, refresh_token=False) -> str:
    return get_random_string(length=30)


class ClientIdGenerator(BaseHashGenerator):
    def hash(self) -> str:
        """
        Generate a client_id for Basic Authentication scheme without colon char
        as in http://tools.ietf.org/html/rfc2617#section-2
        """
        return get_random_string(length=40)


class ClientSecretGenerator(BaseHashGenerator):
    def hash(self):
        return get_random_string(length=100)

import random
from string import ascii_letters, digits

from .models import Urls
all_valid_token_char = [ascii_letters+digits]

def generate_unique_short_link():
    """
    This function generate unique short url for each link
    :return: token:string:8 char
    """
    while True:
        random.shuffle(all_valid_token_char)
        token = random.choices(*all_valid_token_char,k=8)
        token = "".join(token)
        try:
            Urls.objects.get(shortURL=token)
        except Urls.DoesNotExist:
            return token
        else:
            continue

from selenium.common.exceptions import NoSuchElementException
import os

path = os.path.abspath(os.path.dirname(__file__))


def helper_try_except(fun):
    def inner_func(*args):
        try:
            return fun(*args)

        except NoSuchElementException:
            return None
    return inner_func

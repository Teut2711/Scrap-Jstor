
from selenium.common.exceptions import NoSuchElementException


def helper_try_except(fun):
    def inner_func(*args):
        try:
            return fun(*args)

        except NoSuchElementException:
            return None
    return inner_func

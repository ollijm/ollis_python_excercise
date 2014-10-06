__author__ = 'olli'


def is_stringinteger(s):
    """
    Check if given string contains an integer
    :param s: String
    :return: True if string contains integer, else False
    """
    try:
        int(s)
        return True
    except ValueError:
        return False


def validate_result(s):
    """
    Check if given string contains an integer
    :param s: String
    :return: True if string contains integer, else False
    """
    try:
        int(s)
        return True
    except ValueError:
        return False
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


def validate_web_page(webpage):
    if webpage.connection_state is not "OK" or webpage.actual_status_code is not webpage.expected_status_code \
            or not webpage.actual_content_type.startswith(webpage.expected_content_type):
        return False
    else:
        return True
__author__ = 'olli'

"""Place for all validation functions until they need more structured design"""

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


def validate_web_page(webpage):
    """
    Checks if web page passes content requirements. Web page must be connectible, and HTTP status code and Content-Type
    header must as expected.
    :param webpage:
    :return:
    """
    if webpage.read_state is not "OK" or webpage.actual_status_code is not webpage.expected_status_code \
            or not webpage.actual_content_type.startswith(webpage.expected_content_type):
        return False
    else:
        return True
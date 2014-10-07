"""
Place for all validation functions until they need more structured design
"""


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


def web_page_status_as_string(page):
    """
    Return web page's content checks result as human readable string.
    Web page must be connectible, and HTTP status code and Content-Type header must be as expected.
    We only return the first error encountered, although in the case of read error there's
    no need to further check for content errors.
    :param page:
    :return:
    """
    if page.read_state is not "OK":
        return "FAIL: Error trying to read the page [{0}]".format(page.read_state)
    if page.actual_status_code != page.expected_status_code:
        return "FAIL: Expected HTTP status [{0}], got [{1}]".format(page.expected_status_code, page.actual_status_code)
    if not page.actual_content_type.startswith(page.expected_content_type):
        return "FAIL: Expected Content-Type to start with [{0}], got [{1}]".format(page.expected_content_type,
                                                                                   page.actual_content_type)
    return "OK"

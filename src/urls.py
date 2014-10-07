__author__ = 'olli'

urls = [
    {
        "url" : "http://www.kaleva.fi/",
        "expected_status_code" : 200,
        "expected_content_type" : "text/html"
    },
    {
        "url" : "http://www.iltasanomat.fi/rss/uutiset.xml",
        "expected_status_code" : 200,
        "expected_content_type" : "text/xml"
    },
    {
        "url" : "http://www.google.fi/",
        "expected_status_code" : 200,
        "expected_content_type" : "text/html"
    },
    {
        "url" : "http://www.we-expect-this-respond-but-it-wont.com/",
        "expected_status_code" : 200,
        "expected_content_type" : "text/html"
    },
    {
        "url" : "http://www.google.fi/not-existing-file.html",
        "expected_status_code" : 404,
        "expected_content_type" : "text/html"
    },
    {
        "url" : "httXYZ://www.theres-a-typo-here-somehwere.com/",
        "expected_status_code" : 200,
        "expected_content_type" : "text/html"
    },
    {
        "url" : "http://www.google.com/someapi/expecting_no_content",
        "expected_status_code" : 204,
        "expected_content_type" : None
    },
    {
        "url" : "http://www.google.com/?q=expecting_XML",
        "expected_status_code" : 200,
        "expected_content_type" : "text/xml"
    }
]
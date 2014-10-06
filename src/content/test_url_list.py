__author__ = 'olli'

web_pages = [
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
        "url" : "http://www.reallynotexistingdomainxyz.fi/",
        "expected_status_code" : 200,
        "expected_content_type" : "text/html"
    },
    {
        "url" : "http://www.google.fi/not-existing-file.html",
        "expected_status_code" : 200,
        "expected_content_type" : "text/html"
    }
]
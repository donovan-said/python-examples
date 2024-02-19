""" HTTP Connections
"""

import urllib3
import requests


def http_connection():
    """HTTP Connection"""

    # With custom User-Agent header
    print("Connecting with custom User-Agent header...")
    result = requests.get(
        "https://www.google.com", headers={"User-Agent": "TEST"}
    )
    status_code = result.status_code
    print("Status Code: '%s'" % status_code)

    """
    Without User-Agent header
    The requests package uses urllib3, which by default adds a "User-Agent"
    header. You have to actively omit it. Please see:
    https://github.com/psf/requests/issues/5671
    """

    skip_header = {"User-Agent": urllib3.util.SKIP_HEADER}

    print("Connecting without User-Agent header...")
    result = requests.get("https://www.google.com", headers=skip_header)
    status_code = result.status_code
    print("Status Code: '%s'" % status_code)


if __name__ == "__main__":
    http_connection()

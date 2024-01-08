import pytest
from github_api.fetchData import fetch_github_data


def test_fetch_github_data_success():
    # Test successful data fetching
    url = 'https://api.github.com/search/repositories?q=stars:>1'
    data = fetch_github_data(url)

    #assert data.status_code == 200  # Check if the status code is 200 (OK)
    assert data is not None # Ensure a response is received
    assert 'items' in data  # Assuming 'items' should be in the response


def test_fetch_github_data_invalid_url():
    # Test case for an invalid URL
    invalid_url = 'https://api.github.com/invalid_url'
    data = fetch_github_data(invalid_url)
    #assert data.status_code != 200  # Check if the status code is NOT 200 (OK)
    assert data is None  # Expecting None as a response for an invalid URL

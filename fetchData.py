import requests
import logging

logging.basicConfig(level=logging.INFO)  # Set logging level to INFO


def fetch_github_data():
    """
    Fetches data from the GitHub API regarding top starred repositories.

    Returns:
    - Response JSON if successful.
    - None if there's an error.
    """
    url = 'https://api.github.com/search/repositories?q=stars:>1'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for unsuccessful HTTP responses
        return response.json()

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from the GitHub API: {e}")
        return None

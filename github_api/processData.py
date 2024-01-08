import logging

logging.basicConfig(level=logging.INFO)  # Set logging level to INFO


def process_github_data(data):
    """
    Processes the fetched GitHub data.

    Args:
    - data: JSON data from the GitHub API.

    Returns:
    - repo_names: List of names of the top starred repositories.
    - stars_count: List of star counts corresponding to the repositories.
    """
    repo_names = []
    stars_count = []

    try:
        if 'items' in data:
            repos = data['items']
            repo_names = [repo['name'] for repo in repos]
            stars_count = [repo['stargazers_count'] for repo in repos]

        return repo_names, stars_count

    except Exception as e:
        logging.error(f"Error processing data: {e}")
        return None, None

import pytest
from github_api.processData  import process_github_data


def test_process_github_data_success():
    # Test processing valid data
    sample_data = {
        'items': [
            {'name': 'Repo1', 'stargazers_count': 100},
            {'name': 'Repo2', 'stargazers_count': 200},
        ]
    }
    repo_names, stars_count = process_github_data(sample_data)
    assert repo_names is not None
    assert stars_count is not None
    assert len(repo_names) == 2
    assert len(stars_count) == 2


def test_process_github_data_missing_items():
    # Test case for missing 'items' key in the data
    sample_data = {'invalid_key': []}
    repo_names, stars_count = process_github_data(sample_data)
    assert repo_names == []
    assert stars_count == []

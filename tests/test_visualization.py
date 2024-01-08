from github_api.visualization import visualize_top_repositories
import matplotlib.pyplot as plt
import pytest


@pytest.fixture
def configure_matplotlib_backend():
    # Set the backend to 'agg' to prevent plot display
    plt.switch_backend('agg')
    yield


def test_visualize_top_repositories(configure_matplotlib_backend):
    # Mock data for most starred repositories
    repo_names = ['Repo1', 'Repo2', 'Repo3']
    stars_count = [100, 200, 150]

    # Call the visualization function
    visualize_top_repositories(repo_names, stars_count)

    # Assert that a plot is created
    assert plt.gcf().get_axes()

    # Check the title of the plot
    assert plt.gca().get_title() == 'Top 10 Most Starred GitHub Repositories'

    # Check the x-axis label
    assert plt.gca().get_xlabel() == 'Number of Stars'

    # Check the y-axis label
    assert plt.gca().get_ylabel() == 'Repository'


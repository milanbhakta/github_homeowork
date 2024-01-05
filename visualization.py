import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def visualize_top_repositories(repo_names, stars_count):
    """
    Creates a horizontal bar chart visualizing the top 10 repositories.

    Args:
    - repo_names: List of names of the top starred repositories.
    - stars_count: List of star counts corresponding to the repositories.
    """
    # Create a color scheme for bars
    num_repos = len(repo_names)
    colors = list(mcolors.TABLEAU_COLORS.keys())[:num_repos]

    plt.figure(figsize=(10, 6))
    plt.barh(repo_names[:10], stars_count[:10], color=colors)
    plt.xlabel('Number of Stars')
    plt.ylabel('Repository')
    plt.title('Top 10 Most Starred GitHub Repositories')

    plt.tight_layout()
    plt.show()

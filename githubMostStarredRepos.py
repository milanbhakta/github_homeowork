from fetchData import fetch_github_data
from processData import process_github_data
from visualization import visualize_top_repositories
import logging

logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

if __name__ == "__main__":
    github_data = fetch_github_data()

    if github_data:
        repo_names, stars_count = process_github_data(github_data)

        if repo_names is not None and stars_count is not None:
            try:
                visualize_top_repositories(repo_names, stars_count)
                logging.info("Visualization created successfully.")

            except Exception as e:
                logging.error(f"Error creating visualization: {e}")
        else:
            logging.warning("Failed to process data. Visualization cannot be created.")
    else:
        logging.warning("Failed to fetch data. Visualization cannot be created.")


# GitHub Top Starred Repositories Visualizer

This Python script utilizes the GitHub API to retrieve information about the top starred repositories and generates a horizontal bar chart using Matplotlib to visualize the data.

## Overview

This script allows users to visualize the top 10 most starred GitHub repositories based on the number of stars they've received.

## Prerequisites

- Python 3.x installed on your machine
- Required Python libraries (`requests`, `json`, `matplotlib`, `google-colab`, `pytest`)
  
1. Install the required packages (if not installed):

    ```bash
    pip install -r requirements.txt
    ```

2. To run the tests, execute the following command:

    ```bash
    pytest
    ```

   This will automatically discover and run all the test files in the `tests/` directory.

3. Optionally, you can run specific test files:

    ```bash
    pytest tests/test_fetch_data.py  # Run tests in test_fetch_data.py
    pytest tests/test_process_data.py  # Run tests in test_process_data.py
    pytest tests/test_visualization.py  # Run tests in test_visualization.py
    ```
  
import requests
import json
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
#from google.colab import userdata

# URL for GitHub API to fetch repositories
url = 'https://api.github.com/search/repositories?q=stars:>1'

# Make a GET request to fetch data from the API
response = requests.get(url)

if response.status_code != 200:
    print('Failed to fetch data from the API. Status code:', response.status_code)


# Convert the JSON response to a Python dictionary
data = json.loads(response.text)

# Extracting repository names and stars count
repo_names = [repo['name'] for repo in data['items']]
stars_count = [repo['stargazers_count'] for repo in data['items']]

# Create a color scheme for bars
num_repos = len(repo_names)
colors = list(mcolors.TABLEAU_COLORS.keys())[:num_repos]

# Create a horizontal bar chart for the top most starred repositories
plt.figure(figsize=(10, 8))
bars = plt.barh(repo_names[:10], stars_count[:10], color=colors)
plt.xlabel('Number of Stars')
plt.ylabel('Repository')
plt.title('Top 10 Most Starred GitHub Repositories')

plt.tight_layout()
plt.show()



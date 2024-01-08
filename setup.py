from setuptools import setup, find_packages

setup(
    name='github_api_package_dsi',
    version='1.0',
    packages=find_packages(),
    author='MILAN BHAKTA',
    author_email='MILZBHAKTA@GMAIL.COM',
    description='A package for fetching, processing, and visualizing data from the GitHub API',
    url='https://github.com/milanbhakta/github_api_package_dsi',
    python_requires='>=3.6',
    install_requires=[
        'requests',
        'matplotlib',
        'pytest'
    ],
)

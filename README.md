GitLab Exercise

This script extracts data from a given GitLab group and stores the information in an SQLite database. It fetches the following data:

1. All "projects" in the specified GitLab group.
2. All "users" in the group.
3. All "users" for each project in the group.

Requirements
1. Python 3.8 or higher
2. The following Python packages:
    1. python-gitlab: For interacting with the GitLab API.


    Pip install -r requirements.txt 

Usage

Run the main script and provide the necessary arguments:

    python main.py [GITLAB_GROUP_NAME] [YOUR_GITLAB_TOKEN]

Replace [GITLAB_GROUP_NAME] with the name of your desired 
GitLab group and [YOUR_GITLAB_TOKEN] with your GitLab 
personal access token.

Output

The script will fetch the data from GitLab and store it 
in an SQLite database named gitlab_data.db.
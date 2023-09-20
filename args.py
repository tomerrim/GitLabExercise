import argparse


# 1
def parse_arguments():
    parser = argparse.ArgumentParser(description="Extract information from a GitLab group.")
    parser.add_argument("group_name", help="Name of the GitLab group")
    parser.add_argument("token", help="Personal access token for GitLab")
    return parser.parse_args()

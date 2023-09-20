from args import parse_arguments
from gitlab_api import setup_gitlab_client, get_group_id, get_projects_in_group, get_users_in_group, get_users_in_project
from database import setup_database, store_data_in_db

if __name__ == "__main__":

    args = parse_arguments()

    con = setup_database()

    gl = setup_gitlab_client(args.token)
    group_id = get_group_id(gl, args.group_name)
    projects = get_projects_in_group(gl, group_id)
    users = get_users_in_group(gl, group_id)

    project_users = []
    for project in projects:
        user_in_project = get_users_in_project(gl, project.id)
        for user in user_in_project:
            project_users.append({"project_id": project.id, "user_id": user.id})

    store_data_in_db(projects, users, project_users, con)
    con.close()



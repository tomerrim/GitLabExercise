import gitlab


# 2
def setup_gitlab_client(token):
    gl = gitlab.Gitlab('https://gitlab.com', private_token=token)
    return gl


def get_group_id(gl, group_name):
    group = gl.groups.get(group_name)
    return group.id


def get_projects_in_group(gl, group_id):
    group = gl.groups.get(group_id)
    return group.projects.list(all=True)


def get_users_in_group(gl, group_id):
    group = gl.groups.get(group_id)
    return group.members.list(all=True)


def get_users_in_project(gl, project_id):
    project = gl.projects.get(project_id)
    return project.members.list(all=True)


from model.project import Project
import random


def test_delete_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.add_project(Project(name="test777888999"))
    old_project_list = app.project.get_project_list()
    project = random.choice(old_project_list)
    app.project.delete_project_by_name(Project(name=project.name))
    new_project_list = app.project.get_project_list()
    #assert len(old_project_list)-1 == len(new_project_list)
    old_project_list.remove(project)
    #assert sorted(old_project_list, key=(lambda x: x.name)) == sorted(new_project_list, key=(lambda x: x.name))
    assert sorted(old_project_list, key=(lambda x: x.name)) == sorted(
        app.soap.get_projects_list("administrator", "root"), key=(lambda x: x.name))
    app.session.logout()

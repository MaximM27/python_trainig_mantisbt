from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_project_list = app.project.get_project_list()
    project = Project(name="tgesbt3h2hijjjjbffybyyut7i9954")
    app.project.add_project(project)
    new_project_list = app.project.get_project_list()
    old_project_list.append(project)
    assert sorted(old_project_list, key=(lambda x: x.name)) == sorted(app.soap.get_projects_list("administrator", "root"), key=(lambda x: x.name))

    #assert sorted(old_project_list, key=(lambda x: x.name)) == sorted(new_project_list, key=(lambda x: x.name))
    app.session.logout()

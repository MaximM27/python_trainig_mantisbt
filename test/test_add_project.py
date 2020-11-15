from model.project import Project


def test_add_project(app):
    old_project_list = app.project.get_project_list()
    project = Project(name="test324479954")
    app.project.add_project(project)
    new_project_list = app.project.get_project_list()
    old_project_list.append(project)
    assert sorted(old_project_list, key=(lambda x: x.name)) == sorted(new_project_list, key=(lambda x: x.name))


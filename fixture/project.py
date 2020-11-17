from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def add_project(self, Project):
        wd = self.app.wd
        wd.get(self.app.base_url)
        self.open_projects_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(Project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        wd.find_element_by_css_selector("input[value='Create New Project']")

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='/mantisbt-1.2.20/manage_overview_page.php']").click()
        wd.find_element_by_css_selector("a[href='/mantisbt-1.2.20/manage_proj_page.php']").click()

    def fill_project_form(self, Project):
        wd = self.app.wd
        self.change_field_value("name", Project.name)
        self.change_field_value("description", Project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def get_project_list(self):
        wd = self.app.wd
        self.open_projects_page()
        self.project_cache = []
        for row in wd.find_elements_by_xpath("//table[3]/tbody/tr"):
            cells = row.find_elements_by_tag_name("td")
            name = cells[0].text
            self.project_cache.append(Project(name=name))
        #for row in wd.find_elements_by_xpath("//table[3]/tbody/tr.row2"):
           #cells = row.find_elements_by_tag_name("td")
            #name = cells[0].text
            #self.project_cache.append(Project(name=name))
        return list(self.project_cache)[2:]

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_link_text("%s" % name).click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()


import os
from buildspider.build import build_project, find_egg


def project_build(project_name):
    if project_name == "all":
        print("-----------build_all-------------")
        folders = [d for d in os.listdir('.')]
        print(folders)
        path = os.path.abspath(os.path.join(os.getcwd()))
        print(path)
        for folder in folders:
            project_path = os.path.join(path, folder)
            build_project(folder)
            egg = find_egg(project_path)
            print(egg)
        return "all build seccess"
    else:
        print("-----------project_build-----------")
        path = os.path.abspath(os.path.join(os.getcwd()))
        project_path = os.path.join(path, project_name)
        print("project_path: ", project_path)
        if not os.path.exists(project_path):
            return "folder not found "
        build_project(project_name)
        egg = find_egg(project_path)
        if not egg:
            return 'egg not found'
        else:
            return 'egg build seccess'

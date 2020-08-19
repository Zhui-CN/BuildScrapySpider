import os
import sys
from buildspider.config import config
import glob
import tempfile
import shutil
from scrapy.utils.python import retry_on_eintr
from subprocess import check_call

_SETUP_PY_TEMPLATE = \
    """# Build Scrapy Setup
from setuptools import setup, find_packages
setup(
    name='%(project)s',
    version='1.0',
    packages=find_packages(exclude=[]),
    package_data={'': ['*']},
    #zip_safe=False,
    entry_points={'scrapy':['settings=%(settings)s']},
)"""


def build_project(project):
    egg = build_egg(project)
    print('Built %(project)s into %(egg)s' % {'egg': egg, 'project': project})
    return egg


def find_egg(path):
    items = os.listdir(path)
    for name in items:
        if name.endswith(".egg"):
            return name
    return None


def create_default_setup_py(path, **kwargs):
    with open(os.path.join(path, 'setup.py'), 'w', encoding='utf-8') as f:
        file = _SETUP_PY_TEMPLATE % kwargs
        f.write(file)
        f.close()


def build_egg(project):
    print("-----build_egg-----")
    work_path = os.getcwd()
    try:
        path = os.path.abspath(os.path.join(os.getcwd()))
        project_path = os.path.join(path, project)
        os.chdir(project_path)
        settings = config(project_path, 'settings', 'default')
        create_default_setup_py(project_path, settings=settings, project=project)
        d = tempfile.mkdtemp(prefix="temp-")
        o = open(os.path.join(d, "stdout"), "wb")
        e = open(os.path.join(d, "stderr"), "wb")
        retry_on_eintr(check_call, [sys.executable, 'setup.py', 'clean', '-a', 'bdist_egg', '-d', d],
                       stdout=o, stderr=e)
        o.close()
        e.close()
        egg = glob.glob(os.path.join(d, '*.egg'))[0]

        if find_egg(project_path):
            os.remove(os.path.join(project_path, find_egg(project_path)))
        shutil.move(egg, project_path)
        return os.path.join(project_path, find_egg(project_path))
    except Exception as e:
        print(e)
    finally:
        os.chdir(work_path)

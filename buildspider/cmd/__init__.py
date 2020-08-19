import argparse
import os
from buildspider.buildspider import project_build

parser = argparse.ArgumentParser()
parser.add_argument("-p", help="文件夹绝对路径 可无")
parser.add_argument("-n", help="项目文件名 all为全部")


def cmd():
    args = parser.parse_args()
    if not args.n:
        print("Not Fount Project")
        return
    if args.p:
        try:
            os.chdir(args.p)
        except Exception as e:
            print(e)
            return

    print(project_build(args.n))

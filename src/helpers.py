import os


def read_resource_as_lines(path):
    script_dir = os.path.dirname(__file__)
    print(script_dir)
    file = open(script_dir +"/../res/" + path, "r")
    return file.readlines()
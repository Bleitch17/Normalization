import os

from objects.FunctionalDependency import FunctionalDependency, parse_dependency_string
from objects.Relation import Relation, parse_relation_string
from routines.Closure import attribute_closure


input_directory_path = "./input"


def create_relation_from_input_file(file: str) -> Relation:
    file_handle = open(input_directory_path + '/' + file)
    lines = [line.rstrip() for line in file_handle]

    base_relation = parse_relation_string(lines.pop(0))

    fds = set()
    for fd_info in lines:
        fds.add(parse_dependency_string(fd_info))
    base_relation.fds = fds

    file_handle.close()
    return base_relation


def print_relation(r: Relation) -> None:
    print(r.to_string())
    for fd in r.fds:
        print(fd.to_string())


if __name__ == '__main__':
    file_names = os.listdir(input_directory_path)

    relation = create_relation_from_input_file("test-relation-one-key")
    print(relation.to_string())
    for fd in relation.fds:
        print(fd.to_string())
    print(f"ABE+ = {attribute_closure({'A', 'B', 'E'}, relation.fds)}")



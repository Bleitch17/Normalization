import os

from routines.BCNF import *

input_directory_path = "./input"
output_directory_path = "./output"


def create_relation_from_input_file(file: str):
    file_handle = open(input_directory_path + '/' + file)
    lines = [line.rstrip() for line in file_handle]

    relations = list()
    all_relation_info = list()
    relation_index = 0
    for line in lines:
        if line.find("(") > -1 and line.find(")") > -1:
            all_relation_info.append(list())
            all_relation_info[relation_index].append(line)
            relation_index += 1
        elif line.find("->") > -1:
            all_relation_info[relation_index - 1].append(line)

    for relation_info in all_relation_info:
        relations.append(parse_relation_info(relation_info))

    for r in relations:
        for line in r.to_writeable_strings():
            print(line)
        print()

    decomposition = set()
    decompose_to_bcnf(relations[0], decomposition)
    for r in decomposition:
        for line in r.to_writeable_strings():
            print(line)
        print()

    file_handle.close()


if __name__ == '__main__':
    # file_names = os.listdir(input_directory_path)
    create_relation_from_input_file("test-bcnf-decomposition-one-relation.txt")




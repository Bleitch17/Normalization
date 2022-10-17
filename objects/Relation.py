from routines.Key import *


class Relation:
    def __init__(self, name: str, attributes: set[str], fds: set[FunctionalDependency]):
        self._name = name
        self._attributes = frozenset(attributes)
        self._fds = frozenset(fd_closure(fds))
        self._keys = frozenset(minimal_keys(self.attributes, self.fds))

    @property
    def name(self):
        return str(self._name)

    @property
    def attributes(self):
        return set(self._attributes)

    @property
    def fds(self):
        return set(self._fds)

    @property
    def keys(self):
        return set(self._keys)

    def to_writeable_strings(self) -> list[str]:
        relation_info = list()

        attributes_list = list(self._attributes)
        attributes_string = ",".join(attributes_list)
        relation_string = self._name + "(" + attributes_string + ")"
        relation_info.append(relation_string)

        key_strings = list()
        for key in self.keys:
            key_strings.append("{" + ",".join(list(key)) + "}")
        full_key_string = "Keys: {" + ", ".join(key_strings) + "}"
        relation_info.append(full_key_string)

        fd_strings = list()
        for fd in self.fds:
            fd_strings.append(fd.to_string())
        full_fd_string = "F+ = {" + ", ".join(fd_strings) + "}"
        relation_info.append(full_fd_string)

        return relation_info


def parse_relation_info(relation_info: list[str]) -> Relation:
    relation_string = relation_info.pop(0).strip()
    relation_string = relation_string.removesuffix(")")
    name, attributes_string = relation_string.split("(")

    attributes = set()
    for attribute in attributes_string.rsplit(","):
        attributes.add(attribute.strip())

    fds = set()
    for dependency_string in relation_info:
        fds.add(parse_dependency_string(dependency_string))

    return Relation(name, attributes, fds)

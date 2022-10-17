from objects.FunctionalDependency import FunctionalDependency as FD


class Relation:
    def __init__(self, name: str, attributes: set[str]):
        self._name = name
        self._attributes = attributes
        self._fds = set()

    @property
    def attributes(self):
        return self._attributes

    @property
    def fds(self):
        return self._fds

    @fds.setter
    def fds(self, functional_dependencies: set[FD]):
        self._fds = set(functional_dependencies)

    def to_string(self):
        return self._name + "(" + ",".join(self._attributes) + ")"


def parse_relation_string(relation_string: str) -> Relation:
    relation_string = relation_string.removesuffix(")")
    relation_name, attributes_string = relation_string.split("(")
    attributes = set(attributes_string.rsplit(","))
    return Relation(relation_name, attributes)

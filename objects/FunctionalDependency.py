class FunctionalDependency:
    def __init__(self, determiners: set[str], dependents: set[str]):
        self._determiners = determiners
        self._dependents = dependents

    @property
    def lhs(self):
        return set(self._determiners)

    @property
    def rhs(self):
        return set(self._dependents)

    def to_string(self):
        return ",".join(self._determiners) + "->" + ",".join(self._dependents)


def parse_dependency_string(dependency_string: str) -> FunctionalDependency:
    determiners, dependents = dependency_string.split("->")
    return FunctionalDependency(set(determiners.rsplit(",")), set(dependents.rsplit(",")))

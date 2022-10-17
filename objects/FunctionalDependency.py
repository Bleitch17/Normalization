class FunctionalDependency:
    def __init__(self, determiners: set[str], dependents: set[str]):
        self._determiners = frozenset(determiners)
        self._dependents = frozenset(dependents)

    @property
    def lhs(self):
        return set(self._determiners)

    @property
    def rhs(self):
        return set(self._dependents)

    def standard_form(self):
        standard_form_fds = set()
        for dependent in self._dependents:
            standard_form_fds.add(FunctionalDependency(self.lhs, {dependent}))
        return standard_form_fds

    def to_string(self) -> str:
        return ",".join(self._determiners) + "->" + ",".join(self._dependents)

    def __eq__(self, other):
        return len(self.lhs - other.lhs) == 0 and len(self.rhs - other.rhs) == 0

    def __hash__(self):
        lhs_elements = list(self.lhs)
        lhs_elements.sort()
        lhs_hash = hash(tuple(lhs_elements))

        rhs_elements = list(self.lhs)
        rhs_elements.sort()
        rhs_hash = hash(tuple(rhs_elements))

        return hash(lhs_hash + rhs_hash)


def print_fds(fds: set[FunctionalDependency]) -> None:
    display_string = "{"
    for fd in fds:
        display_string += fd.to_string() + ", "
    display_string = display_string.removesuffix(", ")
    display_string += "}"
    print(display_string)


def parse_dependency_string(dependency_string: str) -> FunctionalDependency:
    determiners, dependents = dependency_string.split("->")
    return FunctionalDependency(set(determiners.rsplit(",")), set(dependents.rsplit(",")))

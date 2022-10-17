from objects.FunctionalDependency import *


def attribute_closure(attributes: set[str], fds: set[FunctionalDependency]) -> set[str]:
    closure = set(attributes)
    while True:
        new_closure = set(closure)
        for fd in fds:
            if fd.lhs.issubset(new_closure):
                for attribute in fd.rhs:
                    new_closure.add(attribute)
        if len(new_closure.difference(closure)) > 0:
            closure = set(new_closure)
        else:
            break
    return closure


def fd_closure(fds: set[FunctionalDependency]) -> set[FunctionalDependency]:
    closure = set()
    for fd in fds:
        lhs_closure = attribute_closure(fd.lhs, fds)
        non_trivial_dependents = lhs_closure.difference(fd.lhs)
        for attribute in non_trivial_dependents:
            # Beware subtle bug: set(string) creates a set of characters, not a set of one string
            closure.add(FunctionalDependency(fd.lhs, {attribute}))
    return closure

import objects.FunctionalDependency as FD


def attribute_closure(attributes: set[str], fds: set[FD]) -> set[str]:
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

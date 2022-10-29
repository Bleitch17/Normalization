from routines.Closure import *
from routines.Subset import *


def is_super_key(candidate: set[str], attributes: set[str], fds: set[FunctionalDependency]) -> bool:
    candidate_closure = attribute_closure(candidate, fds)
    if len(attributes.difference(candidate_closure)) == 0:
        return True
    return False


def minimal_keys(attributes: set[str], fds: set[FunctionalDependency]) -> set[frozenset[str]]:
    keys = set()

    # if no fds: all attributes must be the key:
    if len(fds) == 0:
        keys.add(frozenset(attributes))
        return keys

    lhs_attributes = set()
    rhs_attributes = set()
    for fd in fds:
        lhs_attributes = lhs_attributes | fd.lhs
        rhs_attributes = rhs_attributes | fd.rhs

    all_fd_attributes = lhs_attributes | rhs_attributes
    mid_attributes = lhs_attributes & rhs_attributes

    # Debugging: rhs_attributes = rhs_attributes - mid_attributes
    lhs_attributes = (lhs_attributes - mid_attributes) | (attributes - all_fd_attributes)

    # If the closure of the LHS attributes is the key, no need to add from the middle: therefore, have one minimal key:
    key_base_closure = attribute_closure(lhs_attributes, fds)
    if len(attributes - key_base_closure) == 0:
        keys.add(frozenset(lhs_attributes))
        return keys
    else:
        length_of_mid_subset = 1
        min_mid_length_found = False
        while length_of_mid_subset <= len(mid_attributes) and not min_mid_length_found:
            subsets = attribute_subsets(mid_attributes, length_of_mid_subset)
            for subset in subsets:
                candidate = lhs_attributes | subset
                candidate_closure = attribute_closure(candidate, fds)
                if len(attributes - candidate_closure) == 0:
                    min_mid_length_found = True
                    keys.add(frozenset(candidate))
            length_of_mid_subset += 1
        return keys


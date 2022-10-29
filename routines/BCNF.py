from objects.Relation import *


def decompose_to_bcnf(relation: Relation, decomposition: set[Relation]) -> None:
    # Base case: if the relation has no functional dependencies, it must be in BCNF
    # Base case: relation has two attributes (all two attribute relations are in BCNF)
    if len(relation.fds) == 0 or len(relation.attributes) == 2:
        decomposition.add(relation)
        return

    for fd in relation.fds:
        # Test if the lhs of the fd is a super key
        if not is_super_key(fd.lhs, relation.attributes, relation.fds):
            relation_without_rhs = Relation(
                relation.name + "-BCNF",
                relation.attributes - fd.rhs,
                filter_fds(relation.attributes - fd.rhs, relation.fds)
            )
            # for f in filter_fds(relation.attributes - fd.rhs, relation.fds):
            #     print(f.to_string())
            lhs_and_rhs_relation = Relation(
                relation.name + "-BCNF",
                fd.lhs | fd.rhs,
                filter_fds(fd.lhs | fd.rhs, relation.fds)
            )
            decompose_to_bcnf(relation_without_rhs, decomposition)
            decompose_to_bcnf(lhs_and_rhs_relation, decomposition)
            return

    # If no fds violate BCNF, return the relation:
    decomposition.add(relation)
    return


def filter_fds(relevant_attributes: set[str], fds: set[FunctionalDependency]) -> set[FunctionalDependency]:
    relevant_fds = set()
    for fd in fds:
        if (fd.lhs | fd.rhs).issubset(relevant_attributes):
            relevant_fds.add(fd)
    return relevant_fds

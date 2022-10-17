def find_subsets(all_attributes: list[str], attribute_index: int, current_subset: set[str], max_length: int,
                 subsets: set[frozenset[str]]) -> None:
    # Base case: current subset being built is of required length
    if len(current_subset) == max_length:
        subsets.add(frozenset(current_subset))
        return
    # Base case: index has gone out of the list, but the first base case was not met: don't do anything
    if attribute_index >= len(all_attributes):
        return

    # Find all subsets that contain this element and do not contain this element:
    set_with_attribute = current_subset | {all_attributes[attribute_index]}
    set_without_attribute = current_subset
    find_subsets(all_attributes, attribute_index + 1, set_with_attribute, max_length, subsets)
    find_subsets(all_attributes, attribute_index + 1, set_without_attribute, max_length, subsets)

    # Return the union of the collection of subsets
    return


def attribute_subsets(attributes: set[str], length: int) -> set[frozenset[str]]:
    subsets = set()
    find_subsets(list(attributes), 0, set(), length, subsets)
    return subsets

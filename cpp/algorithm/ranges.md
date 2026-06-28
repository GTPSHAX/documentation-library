---
title: Constrained algorithms
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/ranges
---


# Constrained algorithms mark since c++20

C++20 provides constrained versions of most algorithms in the namespace `std::ranges`. In these algorithms, a range can be specified as either an iterator-sentinel pair or as a single  argument, and projections and pointer-to-member callables are supported. Additionally, the  of most algorithms have been changed to return all potentially useful information computed during the execution of the algorithm.

## Algorithm function objects

An ''algorithm function object'' (AFO), informally known as , is a customization point object (CPO) that is specified as one or more overloaded function templates. The name of these function templates designates the corresponding algorithm function object.
For an algorithm function object `o`, let `S` be the corresponding set of function templates. Then for any sequence of arguments `args...`, `o(args...)` is expression-equivalent to `s(args...)`, where the result of name lookup for `s` is the overload set `S`.
The constrained algorithms in the namespace `std::ranges` are defined as algorithm function objects. As a result:
* Explicit template argument lists cannot be specified when calling any of them.
* None of them are visible to argument-dependent lookup.
* When any of them are found by normal unqualified lookup as the name to the left of the function-call operator, argument-dependent lookup is inhibited.

## Range parameters

Some overloads take  arguments, they behave as if they are implemented by dispatching to the corresponding overload in namespace `ranges` that takes separate iterator and sentinel arguments, where for each range argument `r`:
* The corresponding iterator argument is initialized with `ranges::begin(r)`.
rev|until=c++26|
* The corresponding sentinel argument is initialized with `ranges::end(r)`.
rev|since=c++26|
* The corresponding sentinel argument is initialized with:
:* `ranges::next(ranges::begin(r), ranges::end(r))`, if the type of `r` models  and computing  meets the specified complexity requirements.
:* `ranges::end(r)` otherwise.

## Non-modifying sequence operations


| algorithm | |
| std::ranges | |

#### Batch operations

| cpp/algorithm/ranges/dsc for_each | (see dedicated page) |
| cpp/algorithm/ranges/dsc for_each_n | (see dedicated page) |

#### Search operations

| cpp/algorithm/ranges/dsc all_any_none_of | (see dedicated page) |
| cpp/algorithm/ranges/dsc contains | (see dedicated page) |
| cpp/algorithm/ranges/dsc find | (see dedicated page) |
| cpp/algorithm/ranges/dsc find_last | (see dedicated page) |
| cpp/algorithm/ranges/dsc find_end | (see dedicated page) |
| cpp/algorithm/ranges/dsc find_first_of | (see dedicated page) |
| cpp/algorithm/ranges/dsc adjacent_find | (see dedicated page) |
| cpp/algorithm/ranges/dsc count | (see dedicated page) |
| cpp/algorithm/ranges/dsc mismatch | (see dedicated page) |
| cpp/algorithm/ranges/dsc equal | (see dedicated page) |
| cpp/algorithm/ranges/dsc search | (see dedicated page) |
| cpp/algorithm/ranges/dsc search_n | (see dedicated page) |
| cpp/algorithm/ranges/dsc starts_with | (see dedicated page) |
| cpp/algorithm/ranges/dsc ends_with | (see dedicated page) |

#### Fold operations

| cpp/algorithm/ranges/dsc fold_left | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_first | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_right | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_right_last | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_with_iter | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_first_with_iter | (see dedicated page) |


## Modifying sequence operations


| algorithm | |
| std::ranges | |

#### Copy operations

| cpp/algorithm/ranges/dsc copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy_n | (see dedicated page) |
| cpp/algorithm/ranges/dsc copy_backward | (see dedicated page) |
| cpp/algorithm/ranges/dsc move | (see dedicated page) |
| cpp/algorithm/ranges/dsc move_backward | (see dedicated page) |

#### Swap operations

| cpp/algorithm/ranges/dsc swap_ranges | (see dedicated page) |

#### Transformation operations

| cpp/algorithm/ranges/dsc transform | (see dedicated page) |
| cpp/algorithm/ranges/dsc replace | (see dedicated page) |
| cpp/algorithm/ranges/dsc replace_copy | (see dedicated page) |

#### Generation operations

| cpp/algorithm/ranges/dsc fill | (see dedicated page) |
| cpp/algorithm/ranges/dsc fill_n | (see dedicated page) |
| cpp/algorithm/ranges/dsc generate | (see dedicated page) |
| cpp/algorithm/ranges/dsc generate_n | (see dedicated page) |

#### Removing operations

| cpp/algorithm/ranges/dsc remove | (see dedicated page) |
| cpp/algorithm/ranges/dsc remove_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc unique | (see dedicated page) |
| cpp/algorithm/ranges/dsc unique_copy | (see dedicated page) |

#### Order-changing operations

| cpp/algorithm/ranges/dsc reverse | (see dedicated page) |
| cpp/algorithm/ranges/dsc reverse_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc rotate | (see dedicated page) |
| cpp/algorithm/ranges/dsc rotate_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc shift | (see dedicated page) |
| cpp/algorithm/ranges/dsc shuffle | (see dedicated page) |

#### Sampling operations

| cpp/algorithm/ranges/dsc sample | (see dedicated page) |


## Sorting and related operations


| algorithm | |
| std::ranges | |

#### Partitioning operations

| cpp/algorithm/ranges/dsc is_partitioned | (see dedicated page) |
| cpp/algorithm/ranges/dsc partition | (see dedicated page) |
| cpp/algorithm/ranges/dsc partition_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc stable_partition | (see dedicated page) |
| cpp/algorithm/ranges/dsc partition_point | (see dedicated page) |

#### Sorting operations

| cpp/algorithm/ranges/dsc is_sorted | (see dedicated page) |
| cpp/algorithm/ranges/dsc is_sorted_until | (see dedicated page) |
| cpp/algorithm/ranges/dsc sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc partial_sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc partial_sort_copy | (see dedicated page) |
| cpp/algorithm/ranges/dsc stable_sort | (see dedicated page) |
| cpp/algorithm/ranges/dsc nth_element | (see dedicated page) |

#### Binary search operations (on sorted ranges)

| cpp/algorithm/ranges/dsc lower_bound | (see dedicated page) |
| cpp/algorithm/ranges/dsc upper_bound | (see dedicated page) |
| cpp/algorithm/ranges/dsc binary_search | (see dedicated page) |
| cpp/algorithm/ranges/dsc equal_range | (see dedicated page) |

#### Set operations (on sorted ranges)

| cpp/algorithm/ranges/dsc includes | (see dedicated page) |
| cpp/algorithm/ranges/dsc set_difference | (see dedicated page) |
| cpp/algorithm/ranges/dsc set_intersection | (see dedicated page) |
| cpp/algorithm/ranges/dsc set_symmetric_difference | (see dedicated page) |
| cpp/algorithm/ranges/dsc set_union | (see dedicated page) |

#### Merge operations (on sorted ranges)

| cpp/algorithm/ranges/dsc merge | (see dedicated page) |
| cpp/algorithm/ranges/dsc inplace_merge | (see dedicated page) |

#### Heap operations

| cpp/algorithm/ranges/dsc is_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc is_heap_until | (see dedicated page) |
| cpp/algorithm/ranges/dsc make_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc push_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc pop_heap | (see dedicated page) |
| cpp/algorithm/ranges/dsc sort_heap | (see dedicated page) |

#### Minimum/maximum operations

| cpp/algorithm/ranges/dsc max | (see dedicated page) |
| cpp/algorithm/ranges/dsc max_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc min | (see dedicated page) |
| cpp/algorithm/ranges/dsc min_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc minmax | (see dedicated page) |
| cpp/algorithm/ranges/dsc minmax_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc clamp | (see dedicated page) |

#### Lexicographical comparison operations

| cpp/algorithm/ranges/dsc lexicographical_compare | (see dedicated page) |

#### Permutation operations

| cpp/algorithm/ranges/dsc is_permutation | (see dedicated page) |
| cpp/algorithm/ranges/dsc next_permutation | (see dedicated page) |
| cpp/algorithm/ranges/dsc prev_permutation | (see dedicated page) |


## Numeric operations


| numeric | |
| std::ranges | |
| cpp/algorithm/ranges/dsc iota | (see dedicated page) |


## `Specialized `<memory>` algorithms`


| memory | |
| std::ranges | |

#### Object (batch) construction

| cpp/memory/ranges/dsc construct_at | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_copy | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_copy_n | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_fill | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_fill_n | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_move | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_move_n | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_default_construct | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_default_construct_n | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_value_construct | (see dedicated page) |
| cpp/memory/ranges/dsc uninitialized_value_construct_n | (see dedicated page) |

#### Object (batch) destruction

| cpp/memory/ranges/dsc destroy | (see dedicated page) |
| cpp/memory/ranges/dsc destroy_n | (see dedicated page) |
| cpp/memory/ranges/dsc destroy_at | (see dedicated page) |


## Specialized `<random>` algorithms


| random | |
| std::ranges | |
| cpp/algorithm/ranges/dsc generate_random | (see dedicated page) |


## Return types


| algorithm | |
| std::ranges | |
| cpp/algorithm/ranges/return_types/dsc in_fun_result | (see dedicated page) |
| cpp/algorithm/ranges/return_types/dsc in_in_result | (see dedicated page) |
| cpp/algorithm/ranges/return_types/dsc in_out_result | (see dedicated page) |
| cpp/algorithm/ranges/return_types/dsc in_in_out_result | (see dedicated page) |
| cpp/algorithm/ranges/return_types/dsc in_out_out_result | (see dedicated page) |
| cpp/algorithm/ranges/return_types/dsc min_max_result | (see dedicated page) |
| cpp/algorithm/ranges/return_types/dsc in_found_result | (see dedicated page) |
| cpp/algorithm/ranges/return_types/dsc in_value_result | (see dedicated page) |
| cpp/algorithm/ranges/return_types/dsc out_value_result | (see dedicated page) |


## Notes


## Defect reports


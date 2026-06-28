---
title: Algorithms library
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm
---


# Algorithms library

The algorithms library defines functions for a variety of purposes (e.g. searching, sorting, counting, manipulating) that operate on  of elements.

## <sup>(C++20)</sup>

C++20 provides constrained versions of most algorithms in the namespace `std::ranges`. In these algorithms, a range can be specified as either an iterator-sentinel pair or as a single  argument, and projections and pointer-to-member callables are supported. Additionally, the  of most algorithms have been changed to return all potentially useful information computed during the execution of the algorithm.

```cpp
std::vector<int> v{7, 1, 4, 0, -1};
std::ranges::sort(v); // constrained algorithm
```


## Parallel algorithms <sup>(C++17)</sup>

A ''parallel algorithm'' is a function template in the algorithms library with a template parameter named `ExecutionPolicy`<sup>(since C++26)</sup>  or constrained by . Such a template parameter is termed an ''execution policy template parameter'', it describes the manner in which the execution of a parallel algorithm may be parallelized.
Unless otherwise stated, parallel algorithms are allowed to make arbitrary copies of elements from ranges, as long as both `std::is_trivially_copy_constructible_v<T>` and `std::is_trivially_destructible_v<T>` are `true`, where `T` is the type of elements.

### Execution policies

The standard library algorithms support several execution policies, and the library provides corresponding execution policy types and objects. Users may select an execution policy statically by invoking a parallel algorithm with an execution policy object of the corresponding type.
Standard library implementations (but not the users) may define additional execution policies as an extension. The semantics of parallel algorithms invoked with an execution policy object of implementation-defined type is implementation-defined.


| execution | |
| std::execution | |
| cpp/algorithm/dsc execution_policy_tag_t | (see dedicated page) |
| cpp/algorithm/dsc execution_policy_tag | (see dedicated page) |
| std | |
| cpp/algorithm/dsc is_execution_policy | (see dedicated page) |
| cpp/algorithm/dsc execution-policy | (see dedicated page) |


## Non-modifying sequence operations


### Batch operations


| algorithm | |
| cpp/algorithm/dsc for_each | (see dedicated page) |
| cpp/algorithm/dsc for_each_n | (see dedicated page) |


### Search operations


| algorithm | |
| cpp/algorithm/dsc all_any_none_of | (see dedicated page) |
| cpp/algorithm/ranges/dsc contains | (see dedicated page) |
| cpp/algorithm/dsc find | (see dedicated page) |
| cpp/algorithm/ranges/dsc find_last | (see dedicated page) |
| cpp/algorithm/dsc find_end | (see dedicated page) |
| cpp/algorithm/dsc find_first_of | (see dedicated page) |
| cpp/algorithm/dsc adjacent_find | (see dedicated page) |
| cpp/algorithm/dsc count | (see dedicated page) |
| cpp/algorithm/dsc mismatch | (see dedicated page) |
| cpp/algorithm/dsc equal | (see dedicated page) |
| cpp/algorithm/dsc search | (see dedicated page) |
| cpp/algorithm/dsc search_n | (see dedicated page) |
| cpp/algorithm/ranges/dsc starts_with | (see dedicated page) |
| cpp/algorithm/ranges/dsc ends_with | (see dedicated page) |


### Fold operations <sup>(C++23)</sup>


| algorithm | |
| cpp/algorithm/ranges/dsc fold_left | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_first | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_right | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_right_last | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_with_iter | (see dedicated page) |
| cpp/algorithm/ranges/dsc fold_left_first_with_iter | (see dedicated page) |


## Modifying sequence operations


### Copy operations


| algorithm | |
| cpp/algorithm/dsc copy | (see dedicated page) |
| cpp/algorithm/dsc copy_n | (see dedicated page) |
| cpp/algorithm/dsc copy_backward | (see dedicated page) |
| cpp/algorithm/dsc move | (see dedicated page) |
| cpp/algorithm/dsc move_backward | (see dedicated page) |


### Swap operations


| algorithm| | |
| utility| | |
| string_view | |
| cpp/algorithm/dsc swap | (see dedicated page) |
| algorithm | |
| cpp/algorithm/dsc swap_ranges | (see dedicated page) |
| cpp/algorithm/dsc iter_swap | (see dedicated page) |


### Transformation operations


| algorithm | |
| cpp/algorithm/dsc transform | (see dedicated page) |
| cpp/algorithm/dsc replace | (see dedicated page) |
| cpp/algorithm/dsc replace_copy | (see dedicated page) |


### Generation operations


| algorithm | |
| cpp/algorithm/dsc fill | (see dedicated page) |
| cpp/algorithm/dsc fill_n | (see dedicated page) |
| cpp/algorithm/dsc generate | (see dedicated page) |
| cpp/algorithm/dsc generate_n | (see dedicated page) |


### Removing operations


| algorithm | |
| cpp/algorithm/dsc remove | (see dedicated page) |
| cpp/algorithm/dsc remove_copy | (see dedicated page) |
| cpp/algorithm/dsc unique | (see dedicated page) |
| cpp/algorithm/dsc unique_copy | (see dedicated page) |


### Order-changing operations


| algorithm | |
| cpp/algorithm/dsc reverse | (see dedicated page) |
| cpp/algorithm/dsc reverse_copy | (see dedicated page) |
| cpp/algorithm/dsc rotate | (see dedicated page) |
| cpp/algorithm/dsc rotate_copy | (see dedicated page) |
| cpp/algorithm/dsc shift | (see dedicated page) |
| cpp/algorithm/dsc random_shuffle | (see dedicated page) |


### Sampling operations


| algorithm | |
| cpp/algorithm/dsc sample | (see dedicated page) |


## Sorting and related operations


### Requirements

Some algorithms require the sequence represented by the arguments to be “sorted” or “partitioned”. The behavior is undefined if the requirement is not met.
rev|until=c++20|
A sequence is ''sorted with respect to a comparator `comp`'' if for every iterator `iter` pointing to the sequence and every non-negative integer `n` such that `iter + n` is a `valid iterator` pointing to an element of the sequence, `1=comp(*(iter + n), *iter) == false`.
rev|since=c++20|
A sequence is ''sorted with respect to `comp` and `proj`'' for a comparator `comp` and projection `proj` if for every iterator `iter` pointing to the sequence and every non-negative integer `n` such that `iter + n` is a valid iterator pointing to an element of the sequence, box|
`bool(std::invoke(comp, std::invoke(proj, *(iter + n)),`<br />
`std::invoke(proj, *iter)))`
is `false`.
A sequence is ''sorted with respect to a comparator `comp`'' if the sequence is sorted with respect to `comp` and } (the identity projection).
A sequence [start, finish) is ''partitioned with respect to an expression `f(e)`'' if there exists an integer `n` such that for all `i` in [0, std::distance(start, finish)), `f(*(start + i))` is `true` if and only if `i < n`.

### Partitioning operations


| algorithm | |
| cpp/algorithm/dsc is_partitioned | (see dedicated page) |
| cpp/algorithm/dsc partition | (see dedicated page) |
| cpp/algorithm/dsc partition_copy | (see dedicated page) |
| cpp/algorithm/dsc stable_partition | (see dedicated page) |
| cpp/algorithm/dsc partition_point | (see dedicated page) |


### Sorting operations


| algorithm | |
| cpp/algorithm/dsc sort | (see dedicated page) |
| cpp/algorithm/dsc stable_sort | (see dedicated page) |
| cpp/algorithm/dsc partial_sort | (see dedicated page) |
| cpp/algorithm/dsc partial_sort_copy | (see dedicated page) |
| cpp/algorithm/dsc is_sorted | (see dedicated page) |
| cpp/algorithm/dsc is_sorted_until | (see dedicated page) |
| cpp/algorithm/dsc nth_element | (see dedicated page) |


### Binary search operations (on partitioned ranges)


| algorithm | |
| cpp/algorithm/dsc lower_bound | (see dedicated page) |
| cpp/algorithm/dsc upper_bound | (see dedicated page) |
| cpp/algorithm/dsc equal_range | (see dedicated page) |
| cpp/algorithm/dsc binary_search | (see dedicated page) |


### Set operations (on sorted ranges)


| algorithm | |
| cpp/algorithm/dsc includes | (see dedicated page) |
| cpp/algorithm/dsc set_union | (see dedicated page) |
| cpp/algorithm/dsc set_intersection | (see dedicated page) |
| cpp/algorithm/dsc set_difference | (see dedicated page) |
| cpp/algorithm/dsc set_symmetric_difference | (see dedicated page) |


### Merge operations (on sorted ranges)


| algorithm | |
| cpp/algorithm/dsc merge | (see dedicated page) |
| cpp/algorithm/dsc inplace_merge | (see dedicated page) |


### Heap operations

rev|until=c++20|
A random access range [first, last) is a ''heap with respect to a comparator `comp`'' if `bool(comp(first[(i - 1) / 2], first[i]))` is `false` for all integer `i` in .
rev|since=c++20|
A random access range [first, last) is a ''heap with respect to `comp` and `proj`'' for a comparator `comp` and projection `proj` if box|
`bool(std::invoke(comp, std::invoke(proj, first[(i - 1) / 2]),`<br />
`std::invoke(proj, first[i]))`
is `false` for all integer `i` in .
A random access range [first, last) is a ''heap with respect to a comparator `comp`'' if the range is a heap with respect to `comp` and } (the identity projection).
A heap can be created by `std::make_heap`<sup>(since C++20)</sup>  and `ranges::make_heap`.
For more properties of heap, see [Binary heap|max heap](https://en.wikipedia.org/wiki/Binary heap|max heap).


| algorithm | |
| cpp/algorithm/dsc push_heap | (see dedicated page) |
| cpp/algorithm/dsc pop_heap | (see dedicated page) |
| cpp/algorithm/dsc make_heap | (see dedicated page) |
| cpp/algorithm/dsc sort_heap | (see dedicated page) |
| cpp/algorithm/dsc is_heap | (see dedicated page) |
| cpp/algorithm/dsc is_heap_until | (see dedicated page) |


### Minimum/maximum operations


| algorithm | |
| cpp/algorithm/dsc max | (see dedicated page) |
| cpp/algorithm/dsc max_element | (see dedicated page) |
| cpp/algorithm/dsc min | (see dedicated page) |
| cpp/algorithm/dsc min_element | (see dedicated page) |
| cpp/algorithm/dsc minmax | (see dedicated page) |
| cpp/algorithm/dsc minmax_element | (see dedicated page) |
| cpp/algorithm/dsc clamp | (see dedicated page) |


### Lexicographical comparison operations


| algorithm | |
| cpp/algorithm/dsc lexicographical_compare | (see dedicated page) |
| cpp/algorithm/dsc lexicographical_compare_three_way | (see dedicated page) |


### Permutation operations


| algorithm | |
| cpp/algorithm/dsc next_permutation | (see dedicated page) |
| cpp/algorithm/dsc prev_permutation | (see dedicated page) |
| cpp/algorithm/dsc is_permutation | (see dedicated page) |


## Numeric operations


| numeric | |
| cpp/algorithm/dsc iota | (see dedicated page) |
| cpp/algorithm/dsc accumulate | (see dedicated page) |
| cpp/algorithm/dsc inner_product | (see dedicated page) |
| cpp/algorithm/dsc adjacent_difference | (see dedicated page) |
| cpp/algorithm/dsc partial_sum | (see dedicated page) |
| cpp/algorithm/dsc reduce | (see dedicated page) |
| cpp/algorithm/dsc exclusive_scan | (see dedicated page) |
| cpp/algorithm/dsc inclusive_scan | (see dedicated page) |
| cpp/algorithm/dsc transform_reduce | (see dedicated page) |
| cpp/algorithm/dsc transform_exclusive_scan | (see dedicated page) |
| cpp/algorithm/dsc transform_inclusive_scan | (see dedicated page) |


## 


## Specialized `<random>` algorithms <sup>(C++26)</sup>


| random | |
| cpp/algorithm/ranges/dsc generate_random | (see dedicated page) |


## Notes


## C library


| cstdlib | |
| cpp/algorithm/dsc qsort | (see dedicated page) |
| cpp/algorithm/dsc bsearch | (see dedicated page) |


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2150 | C++98 | the definition of a sorted sequence was incorrect | corrected |


## See also


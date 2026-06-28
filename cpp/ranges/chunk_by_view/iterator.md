---
title: std::ranges::chunk_by_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_by_view/iterator
---

ddcla|since=c++23|expos=yes|
class /*iterator*/
The return type of `chunk_by_view::begin`, and of `chunk_by_view::end` when the underlying view `V` is a .

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |
| dsc|`iterator_concept`| | |
| * `std::bidirectional_iterator_tag`, if `V` models , otherwise | |
| * `std::forward_iterator_tag`. | |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions


| cpp/ranges/adaptor/iterator/dsc operator arith|chunk_by_view | (see dedicated page) |


## Non-member functions


| cpp/ranges/chunk_by_view/iterator/operator_cmp|title=operator==|compares the underlying iterators|notes= | |


## Example


## See also


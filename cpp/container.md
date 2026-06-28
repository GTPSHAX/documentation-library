---
title: Containers library
type: Containers
source: https://en.cppreference.com/w/cpp/container
---


# Containers library

The Containers library is a generic collection of class templates and algorithms that allow programmers to easily implement common data structures like queues, lists and stacks. There are <sup>(until C++11)</sup> two<sup>(since C++11)</sup> three classes of containers:
* sequence containers,
* associative containers,
rrev|since=c++11|
* unordered associative containers,
each of which is designed to support a different set of operations.
The container manages the storage space that is allocated for its elements and provides member functions to access them, either directly or through iterators (objects with  properties similar to pointers).
Most containers have at least several member functions in common, and share functionalities. Which container is the best for the particular application depends not only on the offered functionality, but also on its efficiency for different workloads.

## Sequence containers

Sequence containers implement data structures which can be accessed sequentially.


| cpp/container/dsc array | (see dedicated page) |
| cpp/container/dsc vector | (see dedicated page) |
| cpp/container/dsc inplace_vector | (see dedicated page) |
| cpp/container/dsc hive | (see dedicated page) |
| cpp/container/dsc deque | (see dedicated page) |
| cpp/container/dsc forward_list | (see dedicated page) |
| cpp/container/dsc list | (see dedicated page) |


## Associative containers

Associative containers implement sorted data structures that can be quickly searched ($O(log n)$ complexity).


| cpp/container/dsc set | (see dedicated page) |
| cpp/container/dsc map | (see dedicated page) |
| cpp/container/dsc multiset | (see dedicated page) |
| cpp/container/dsc multimap | (see dedicated page) |


## Unordered associative containers <sup>(C++11)</sup>

Unordered associative containers implement unsorted (hashed) data structures that can be quickly searched ($O(1)$ average, $O(n)$ worst-case complexity).


| cpp/container/dsc unordered_set | (see dedicated page) |
| cpp/container/dsc unordered_map | (see dedicated page) |
| cpp/container/dsc unordered_multiset | (see dedicated page) |
| cpp/container/dsc unordered_multimap | (see dedicated page) |


## Container adaptors

Container adaptors provide a different interface for sequential containers.


| cpp/container/dsc stack | (see dedicated page) |
| cpp/container/dsc queue | (see dedicated page) |
| cpp/container/dsc priority_queue | (see dedicated page) |
| cpp/container/dsc flat_set | (see dedicated page) |
| cpp/container/dsc flat_map | (see dedicated page) |
| cpp/container/dsc flat_multiset | (see dedicated page) |
| cpp/container/dsc flat_multimap | (see dedicated page) |


## Views <sup>(C++20)</sup>

Views provide flexible facilities for interacting with one- or multi-dimensional views over a non-owning array of elements.


| cpp/container/dsc span | (see dedicated page) |
| cpp/container/dsc mdspan | (see dedicated page) |


## Iterator invalidation

Read-only methods never invalidate iterators or references. Methods which modify the contents of a container may invalidate iterators and/or references, as summarized in this table.


| - |
| rowspan="2" | Category |
| rowspan="2" | Container |
| colspan="2" | After '''insertion''', are... |
| colspan="2" | After '''erasure''', are... |
| rowspan="2" | Conditionally |
| - |
| '''iterators''' valid? |
| '''references''' valid? |
| '''iterators''' valid? |
| '''references''' valid? |
| - |
| rowspan="8" | Sequence containers |
| ltt | cpp/container/array |
| colspan="2" |
| colspan="2" |
|  |
| - |
| rowspan="3" | ltt | cpp/container/vector |
| colspan="2" |
| colspan="2" |
| Insertion changed capacity |
| - |
| colspan="2" |
| colspan="2" |
| Before modified element(s)<br/>(for insertion only if capacity didn't change) |
| - |
| colspan="2" |
| colspan="2" |
| At or after modified element(s) |
| - |
| rowspan="2" | ltt | cpp/container/deque |
| rowspan="2" |
|  |
| colspan="2" maybe | Yes, except erased element(s) |
| Modified first or last element |
| - |
|  |
| colspan="2" |
| Modified middle only |
| - |
| ltt | cpp/container/list |
| colspan="2" |
| colspan="2" maybe | Yes, except erased element(s) |
|  |
| - |
| ltt | cpp/container/forward_list |
| colspan="2" |
| colspan="2" maybe | Yes, except erased element(s) |
|  |
| - |
| Associative containers |
| ltt | cpp/container/set<br/><!-- |
| colspan="2" |
| colspan="2" maybe | Yes, except erased element(s) |
| rowspan="1" |  |
| - |
| rowspan="2" | Unordered associative containers |
| rowspan="2" | ltt | cpp/container/unordered_set<br/><!-- |
|  |
| rowspan="2" |
| colspan="2" <!--N/A due to incompatibility between the condition "Insertion caused rehash" and this column's topic ("After erasure..."). maybe | Yes, except erased element(s)--> |
| Insertion caused rehash |
| - |
|  |
| colspan="2" maybe | Yes, except erased element(s) |
| No rehash |

> **TODO:** add iterator invalidation for C++23 "flat" adaptors (`std::flat_set` etc)
> **TODO:** add iterator invalidation for C++26 `std::inplace_vector`
Here, '''insertion''' refers to any method which adds one or more elements to the container and '''erasure''' refers to any method which removes one or more elements from the container.
* Examples of insertion methods are `std::set::insert`, `std::map::emplace`, `std::vector::push_back`, and `std::deque::push_front`.
rrev|since=c++11|
:* Note that `std::unordered_map::operator[]` also counts, as it may insert an element into the map.
* Examples of erasure methods are `std::set::erase`, `std::vector::pop_back`, `std::deque::pop_front`, and `std::map::clear`.
** `clear` invalidates all iterators and references. Because it erases all elements, this technically complies with the rules above.
Unless otherwise specified (either explicitly or by defining a function in terms of other functions), passing a container as an argument to a library function never invalidate iterators to, or change the values of, objects within that container.
The past-the-end iterator deserves particular mention. In general this iterator is invalidated as though it were a normal iterator to a non-erased element. So `std::set::end` is never invalidated<sup>(since C++11)</sup> , `std::unordered_set::end` is invalidated only on rehash, `std::vector::end` is always invalidated (since it is always after the modified elements), and so on.
There is one exception: an erasure which deletes the last element of a `std::deque` ''does'' invalidate the past-the-end iterator, even though it is not an erased element of the container (or an element at all). Combined with the general rules for `std::deque` iterators, the net result is that the only modifying operation which does ''not'' invalidate `std::deque::end` is an erasure which deletes the first element, but not the last.
rrev|since=c++11|

## Thread safety

# All container functions can be called concurrently by different threads on different containers. More generally, the C++ standard library functions do not read objects accessible by other threads unless those objects are directly or indirectly accessible via the function arguments, including the this pointer.
# All `const` member functions can be called concurrently by different threads on the same container. In addition, the member functions `begin()`, `end()`, `rbegin()`, `rend()`, `front()`, `back()`, `data()`, `find()`, `lower_bound()`, `upper_bound()`, `equal_range()`, `at()`, and, except in associative containers, `operator[]`, behave as `const` for the purposes of thread safety (that is, they can also be called concurrently by different threads on the same container). More generally, the C++ standard library functions do not modify objects unless those objects are accessible, directly or indirectly, via the function's non-const arguments, including the this pointer.
# Different elements in the same container can be modified concurrently by different threads, except for the elements of `std::vector<bool>` (for example, a vector of `std::future` objects can be receiving values from multiple threads).
# Iterator operations (e.g. incrementing an iterator) read, but do not modify the underlying container, and may be executed concurrently with operations on other iterators on the same container, with the const member functions, or reads from the elements. Container operations that invalidate any iterators modify the container and cannot be executed concurrently with any operations on existing iterators even if those iterators are not invalidated.
# Elements of the same container can be modified concurrently with those member functions that are not specified to access these elements. More generally, the C++ standard library functions do not read objects indirectly accessible through their arguments (including other elements of a container) except when required by its specification.
# In any case, container operations (as well as algorithms, or any other C++ standard library functions) may be parallelized internally as long as this does not change the user-visible results (e.g. `std::transform` may be parallelized, but not `std::for_each` which is specified to visit each element of a sequence in order).

## Function table

Note: `std::basic_string` is not treated as a container by the standard but behaves much like one due to its similarity. It is listed as 'Pseudo container' here for convenience.


| - |
| style="width:4em; background:#bcbcff;" |  |
| - functions present in C++03 |
| - |
| style="width:4em; background:#bcffbc;" |  |
| - functions present since C++11 |
| - |
| style="width:4em; background:#ffeebc;" |  |
| - functions present since C++17 |
| - |
| style="width:4em; background:#ffdb99;" |  |
| - functions present since C++20 |
| - |
| style="width:4em; background:#ff9966;" |  |
| - functions present since C++23 |

> **TODO:** Add C++26 "color" and fill member/non-member function table for `std::inplace_vector`

### Member function table

<div style="max-width: 100%; max-height: 80vh; overflow: scroll;">


| - |
| colspan="2" |  |
| colspan="1" | Pseudo container |
| colspan="5" | Sequence containers |
| colspan="4" | Associative containers |
| colspan="4" | Unordered associative containers |
| colspan="7" | Container adaptors |
| colspan="2" |  |
| - |
| colspan="2" | Header |
| tt | header | string |
| tt | header | array |
| tt | header | vector |
| tt | header | deque |
| tt | header | forward_list |
| tt | header | list |
| colspan="2" | tt | header | set |
| colspan="2" | tt | header | map |
| colspan="2" | tt | header | unordered_set |
| colspan="2" | tt | header | unordered_map |
| tt | header | stack |
| colspan="2" | tt | header | queue |
| colspan="2" | tt | header | flat_set |
| colspan="2" | tt | header | flat_map |
| colspan="2" | Header |
| - |
| colspan="2" | Container |
| cpp/container/table cell ho | cpp/string/basic_string |
| cpp/container/table cell hn | /array |
| cpp/container/table cell ho | /vector |
| cpp/container/table cell ho | /deque |
| cpp/container/table cell hn | /forward_list |
| cpp/container/table cell ho | /list |
| cpp/container/table cell ho | /set |
| cpp/container/table cell ho | /multiset |
| cpp/container/table cell ho | /map |
| cpp/container/table cell ho | /multimap |
| cpp/container/table cell hn | /unordered_set |
| cpp/container/table cell hn | /unordered_multiset |
| cpp/container/table cell hn | /unordered_map |
| cpp/container/table cell hn | /unordered_multimap |
| cpp/container/table cell ho | /stack |
| cpp/container/table cell ho | /queue |
| cpp/container/table cell ho | /priority_queue |
| cpp/container/table cell h23 | /flat_set |
| cpp/container/table cell h23 | /flat_multiset |
| cpp/container/table cell h23 | /flat_map |
| cpp/container/table cell h23 | /flat_multimap |
| colspan="2" | Container |
| - |
| rowspan="5" |  |
| cpp/container/table cell lo | (constructor) |
| cpp/container/table cell o | cpp/string/basic_string/basic_string |
| cpp/container/table cell | (implicit) |
| cpp/container/table cell o | /vector/vector |
| cpp/container/table cell o | /deque/deque |
| cpp/container/table cell n | /forward_list/forward_list |
| cpp/container/table cell o | /list/list |
| cpp/container/table cell o | /set/set |
| cpp/container/table cell o | /multiset/multiset |
| cpp/container/table cell o | /map/map |
| cpp/container/table cell o | /multimap/multimap |
| cpp/container/table cell n | /unordered_set/unordered_set |
| cpp/container/table cell n | /unordered_multiset/unordered_multiset |
| cpp/container/table cell n | /unordered_map/unordered_map |
| cpp/container/table cell n | /unordered_multimap/unordered_multimap |
| cpp/container/table cell o | /stack/stack |
| cpp/container/table cell o | /queue/queue |
| cpp/container/table cell o | /priority_queue/priority_queue |
| cpp/container/table cell 23 | /flat_set/flat_set |
| cpp/container/table cell 23 | /flat_multiset/flat_multiset |
| cpp/container/table cell 23 | /flat_map/flat_map |
| cpp/container/table cell 23 | /flat_multimap/flat_multimap |
| cpp/container/table cell lo | (constructor) |
| rowspan="5" |  |
| - |
| cpp/container/table cell lo | (destructor) |
| cpp/container/table cell o | cpp/string/basic_string/~basic_string |
| cpp/container/table cell | (implicit) |
| cpp/container/table cell o | /vector/~vector |
| cpp/container/table cell o | /deque/~deque |
| cpp/container/table cell n | /forward_list/~forward_list |
| cpp/container/table cell o | /list/~list |
| cpp/container/table cell o | /set/~set |
| cpp/container/table cell o | /multiset/~multiset |
| cpp/container/table cell o | /map/~map |
| cpp/container/table cell o | /multimap/~multimap |
| cpp/container/table cell n | /unordered_set/~unordered_set |
| cpp/container/table cell n | /unordered_multiset/~unordered_multiset |
| cpp/container/table cell n | /unordered_map/~unordered_map |
| cpp/container/table cell n | /unordered_multimap/~unordered_multimap |
| cpp/container/table cell o | /stack/~stack |
| cpp/container/table cell o | /queue/~queue |
| cpp/container/table cell o | /priority_queue/~priority_queue |
| cpp/container/table cell 23 | /flat_set/~flat_set |
| cpp/container/table cell 23 | /flat_multiset/~flat_multiset |
| cpp/container/table cell 23 | /flat_map/~flat_map |
| cpp/container/table cell 23 | /flat_multimap/~flat_multimap |
| cpp/container/table cell lo | (destructor) |
| - |
| cpp/container/table cell lo | operator |
| cpp/container/table cell o | cpp/string/basic_string/operator |
| cpp/container/table cell | (implicit) |
| cpp/container/table cell o | /vector/operator |
| cpp/container/table cell o | /deque/operator |
| cpp/container/table cell n | /forward_list/operator |
| cpp/container/table cell o | /list/operator |
| cpp/container/table cell o | /set/operator |
| cpp/container/table cell o | /multiset/operator |
| cpp/container/table cell o | /map/operator |
| cpp/container/table cell o | /multimap/operator |
| cpp/container/table cell n | /unordered_set/operator |
| cpp/container/table cell n | /unordered_multiset/operator |
| cpp/container/table cell n | /unordered_map/operator |
| cpp/container/table cell n | /unordered_multimap/operator |
| cpp/container/table cell o | /stack/operator |
| cpp/container/table cell o | /queue/operator |
| cpp/container/table cell o | /priority_queue/operator |
| cpp/container/table cell 23 | /flat_set/operator |
| cpp/container/table cell 23 | /flat_multiset/operator |
| cpp/container/table cell 23 | /flat_map/operator |
| cpp/container/table cell 23 | /flat_multimap/operator |
| cpp/container/table cell lo | operator |
| - |
| cpp/container/table cell lo | assign |
| cpp/container/table cell o | cpp/string/basic_string/assign |
| n/a |  |
| cpp/container/table cell o | /vector/assign |
| cpp/container/table cell o | /deque/assign |
| cpp/container/table cell n | /forward_list/assign |
| cpp/container/table cell o | /list/assign |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | assign |
| - |
| cpp/container/table cell l23 | assign_range |
| cpp/container/table cell 23 | cpp/string/basic_string/assign_range |
| n/a |  |
| cpp/container/table cell 23 | /vector/assign_range |
| cpp/container/table cell 23 | /deque/assign_range |
| cpp/container/table cell 23 | /forward_list/assign_range |
| cpp/container/table cell 23 | /list/assign_range |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell l23 | assign_range |
| - |
| rowspan="4" | Iterators |
| cpp/container/table cell lon | begin | cbegin |
| cpp/container/table cell on | cpp/string/basic_string/begin | begin | cbegin |
| cpp/container/table cell nn | /array/begin | begin | cbegin |
| cpp/container/table cell on | /vector/begin | begin | cbegin |
| cpp/container/table cell on | /deque/begin | begin | cbegin |
| cpp/container/table cell nn | /forward_list/begin | begin | cbegin |
| cpp/container/table cell on | /list/begin | begin | cbegin |
| cpp/container/table cell on | /set/begin | begin | cbegin |
| cpp/container/table cell on | /multiset/begin | begin | cbegin |
| cpp/container/table cell on | /map/begin | begin | cbegin |
| cpp/container/table cell on | /multimap/begin | begin | cbegin |
| cpp/container/table cell nn | /unordered_set/begin | begin | cbegin |
| cpp/container/table cell nn | /unordered_multiset/begin | begin | cbegin |
| cpp/container/table cell nn | /unordered_map/begin | begin | cbegin |
| cpp/container/table cell nn | /unordered_multimap/begin | begin | cbegin |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 2323 | /flat_set/begin | begin | cbegin |
| cpp/container/table cell 2323 | /flat_multiset/begin | begin | cbegin |
| cpp/container/table cell 2323 | /flat_map/begin | begin | cbegin |
| cpp/container/table cell 2323 | /flat_multimap/begin | begin | cbegin |
| cpp/container/table cell lon | begin | cbegin |
| rowspan="4" | Iterators |
| - |
| cpp/container/table cell lon | end | cend |
| cpp/container/table cell on | cpp/string/basic_string/end | end | cend |
| cpp/container/table cell nn | /array/end | end | cend |
| cpp/container/table cell on | /vector/end | end | cend |
| cpp/container/table cell on | /deque/end | end | cend |
| cpp/container/table cell nn | /forward_list/end | end | cend |
| cpp/container/table cell on | /list/end | end | cend |
| cpp/container/table cell on | /set/end | end | cend |
| cpp/container/table cell on | /multiset/end | end | cend |
| cpp/container/table cell on | /map/end | end | cend |
| cpp/container/table cell on | /multimap/end | end | cend |
| cpp/container/table cell nn | /unordered_set/end | end | cend |
| cpp/container/table cell nn | /unordered_multiset/end | end | cend |
| cpp/container/table cell nn | /unordered_map/end | end | cend |
| cpp/container/table cell nn | /unordered_multimap/end | end | cend |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 2323 | /flat_set/end | end | cend |
| cpp/container/table cell 2323 | /flat_multiset/end | end | cend |
| cpp/container/table cell 2323 | /flat_map/end | end | cend |
| cpp/container/table cell 2323 | /flat_multimap/end | end | cend |
| cpp/container/table cell lon | end | cend |
| - |
| cpp/container/table cell lon | rbegin | crbegin |
| cpp/container/table cell on | cpp/string/basic_string/rbegin | rbegin | crbegin |
| cpp/container/table cell nn | /array/rbegin | rbegin | crbegin |
| cpp/container/table cell on | /vector/rbegin | rbegin | crbegin |
| cpp/container/table cell on | /deque/rbegin | rbegin | crbegin |
| n/a |  |
| cpp/container/table cell on | /list/rbegin | rbegin | crbegin |
| cpp/container/table cell on | /set/rbegin | rbegin | crbegin |
| cpp/container/table cell on | /multiset/rbegin | rbegin | crbegin |
| cpp/container/table cell on | /map/rbegin | rbegin | crbegin |
| cpp/container/table cell on | /multimap/rbegin | rbegin | crbegin |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 2323 | /flat_set/rbegin | rbegin | crbegin |
| cpp/container/table cell 2323 | /flat_multiset/rbegin | rbegin | crbegin |
| cpp/container/table cell 2323 | /flat_map/rbegin | rbegin | crbegin |
| cpp/container/table cell 2323 | /flat_multimap/rbegin | rbegin | crbegin |
| cpp/container/table cell lon | rbegin | crbegin |
| - |
| cpp/container/table cell lon | rend | crend |
| cpp/container/table cell on | cpp/string/basic_string/rend | rend | crend |
| cpp/container/table cell nn | /array/rend | rend | crend |
| cpp/container/table cell on | /vector/rend | rend | crend |
| cpp/container/table cell on | /deque/rend | rend | crend |
| n/a |  |
| cpp/container/table cell on | /list/rend | rend | crend |
| cpp/container/table cell on | /set/rend | rend | crend |
| cpp/container/table cell on | /multiset/rend | rend | crend |
| cpp/container/table cell on | /map/rend | rend | crend |
| cpp/container/table cell on | /multimap/rend | rend | crend |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 2323 | /flat_set/rend | rend | crend |
| cpp/container/table cell 2323 | /flat_multiset/rend | rend | crend |
| cpp/container/table cell 2323 | /flat_map/rend | rend | crend |
| cpp/container/table cell 2323 | /flat_multimap/rend | rend | crend |
| cpp/container/table cell lon | rend | crend |
| - |
| rowspan="5" | Element <br> access |
| cpp/container/table cell lo | at |
| cpp/container/table cell o | cpp/string/basic_string/at |
| cpp/container/table cell n | /array/at |
| cpp/container/table cell o | /vector/at |
| cpp/container/table cell o | /deque/at |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /map/at |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /unordered_map/at |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_map/at |
| n/a |  |
| cpp/container/table cell lo | at |
| rowspan="5" | Element <br> access |
| - |
| cpp/container/table cell lo | operator[] |
| cpp/container/table cell o | cpp/string/basic_string/operator_at | operator[] |
| cpp/container/table cell n | /array/operator_at | operator[] |
| cpp/container/table cell o | /vector/operator_at | operator[] |
| cpp/container/table cell o | /deque/operator_at | operator[] |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /map/operator_at | operator[] |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /unordered_map/operator_at | operator[] |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_map/operator_at | operator[] |
| n/a |  |
| cpp/container/table cell lo | operator[] |
| - |
| cpp/container/table cell ln | data |
| cpp/container/table cell o | cpp/string/basic_string/data |
| cpp/container/table cell n | /array/data |
| cpp/container/table cell n | /vector/data |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell ln | data |
| - |
| cpp/container/table cell lo | front |
| cpp/container/table cell n | cpp/string/basic_string/front |
| cpp/container/table cell n | /array/front |
| cpp/container/table cell o | /vector/front |
| cpp/container/table cell o | /deque/front |
| cpp/container/table cell n | /forward_list/front |
| cpp/container/table cell o | /list/front |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /queue/front |
| cpp/container/table cell o | /priority_queue/top | top |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | front |
| - |
| cpp/container/table cell lo | back |
| cpp/container/table cell n | cpp/string/basic_string/back |
| cpp/container/table cell n | /array/back |
| cpp/container/table cell o | /vector/back |
| cpp/container/table cell o | /deque/back |
| n/a |  |
| cpp/container/table cell o | /list/back |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /stack/top | top |
| cpp/container/table cell o | /queue/back |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | back |
| - |
| rowspan="7" | Capacity |
| cpp/container/table cell lo | empty |
| cpp/container/table cell o | cpp/string/basic_string/empty |
| cpp/container/table cell n | /array/empty |
| cpp/container/table cell o | /vector/empty |
| cpp/container/table cell o | /deque/empty |
| cpp/container/table cell n | /forward_list/empty |
| cpp/container/table cell o | /list/empty |
| cpp/container/table cell o | /set/empty |
| cpp/container/table cell o | /multiset/empty |
| cpp/container/table cell o | /map/empty |
| cpp/container/table cell o | /multimap/empty |
| cpp/container/table cell n | /unordered_set/empty |
| cpp/container/table cell n | /unordered_multiset/empty |
| cpp/container/table cell n | /unordered_map/empty |
| cpp/container/table cell n | /unordered_multimap/empty |
| cpp/container/table cell o | /stack/empty |
| cpp/container/table cell o | /queue/empty |
| cpp/container/table cell o | /priority_queue/empty |
| cpp/container/table cell 23 | /flat_set/empty |
| cpp/container/table cell 23 | /flat_multiset/empty |
| cpp/container/table cell 23 | /flat_map/empty |
| cpp/container/table cell 23 | /flat_multimap/empty |
| cpp/container/table cell lo | empty |
| rowspan="7" | Capacity |
| - |
| cpp/container/table cell lo | size |
| cpp/container/table cell o | cpp/string/basic_string/size |
| cpp/container/table cell n | /array/size |
| cpp/container/table cell o | /vector/size |
| cpp/container/table cell o | /deque/size |
| n/a |  |
| cpp/container/table cell o | /list/size |
| cpp/container/table cell o | /set/size |
| cpp/container/table cell o | /multiset/size |
| cpp/container/table cell o | /map/size |
| cpp/container/table cell o | /multimap/size |
| cpp/container/table cell n | /unordered_set/size |
| cpp/container/table cell n | /unordered_multiset/size |
| cpp/container/table cell n | /unordered_map/size |
| cpp/container/table cell n | /unordered_multimap/size |
| cpp/container/table cell o | /stack/size |
| cpp/container/table cell o | /queue/size |
| cpp/container/table cell o | /priority_queue/size |
| cpp/container/table cell 23 | /flat_set/size |
| cpp/container/table cell 23 | /flat_multiset/size |
| cpp/container/table cell 23 | /flat_map/size |
| cpp/container/table cell 23 | /flat_multimap/size |
| cpp/container/table cell lo | size |
| - |
| cpp/container/table cell lo | max_size |
| cpp/container/table cell o | cpp/string/basic_string/max_size |
| cpp/container/table cell n | /array/max_size |
| cpp/container/table cell o | /vector/max_size |
| cpp/container/table cell o | /deque/max_size |
| cpp/container/table cell n | /forward_list/max_size |
| cpp/container/table cell o | /list/max_size |
| cpp/container/table cell o | /set/max_size |
| cpp/container/table cell o | /multiset/max_size |
| cpp/container/table cell o | /map/max_size |
| cpp/container/table cell o | /multimap/max_size |
| cpp/container/table cell n | /unordered_set/max_size |
| cpp/container/table cell n | /unordered_multiset/max_size |
| cpp/container/table cell n | /unordered_map/max_size |
| cpp/container/table cell n | /unordered_multimap/max_size |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/max_size |
| cpp/container/table cell 23 | /flat_multiset/max_size |
| cpp/container/table cell 23 | /flat_map/max_size |
| cpp/container/table cell 23 | /flat_multimap/max_size |
| cpp/container/table cell lo | max_size |
| - |
| cpp/container/table cell lo | resize |
| cpp/container/table cell o | cpp/string/basic_string/resize |
| n/a |  |
| cpp/container/table cell o | /vector/resize |
| cpp/container/table cell o | /deque/resize |
| cpp/container/table cell n | /forward_list/resize |
| cpp/container/table cell o | /list/resize |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | resize |
| - |
| cpp/container/table cell lo | capacity |
| cpp/container/table cell o | cpp/string/basic_string/capacity |
| n/a |  |
| cpp/container/table cell o | /vector/capacity |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | capacity |
| - |
| cpp/container/table cell lo | reserve |
| cpp/container/table cell o | cpp/string/basic_string/reserve |
| n/a |  |
| cpp/container/table cell o | /vector/reserve |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /unordered_set/reserve |
| cpp/container/table cell n | /unordered_multiset/reserve |
| cpp/container/table cell n | /unordered_map/reserve |
| cpp/container/table cell n | /unordered_multimap/reserve |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | reserve |
| - |
| cpp/container/table cell ln | shrink_to_fit |
| cpp/container/table cell n | cpp/string/basic_string/shrink_to_fit |
| n/a |  |
| cpp/container/table cell n | /vector/shrink_to_fit |
| cpp/container/table cell n | /deque/shrink_to_fit |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell ln | shrink_to_fit |
| - |
| rowspan="19" | Modifiers |
| cpp/container/table cell lo | clear |
| cpp/container/table cell o | cpp/string/basic_string/clear |
| n/a |  |
| cpp/container/table cell o | /vector/clear |
| cpp/container/table cell o | /deque/clear |
| cpp/container/table cell n | /forward_list/clear |
| cpp/container/table cell o | /list/clear |
| cpp/container/table cell o | /set/clear |
| cpp/container/table cell o | /multiset/clear |
| cpp/container/table cell o | /map/clear |
| cpp/container/table cell o | /multimap/clear |
| cpp/container/table cell n | /unordered_set/clear |
| cpp/container/table cell n | /unordered_multiset/clear |
| cpp/container/table cell n | /unordered_map/clear |
| cpp/container/table cell n | /unordered_multimap/clear |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/clear |
| cpp/container/table cell 23 | /flat_multiset/clear |
| cpp/container/table cell 23 | /flat_map/clear |
| cpp/container/table cell 23 | /flat_multimap/clear |
| cpp/container/table cell lo | clear |
| rowspan="19" | Modifiers |
| - |
| cpp/container/table cell lo | insert |
| cpp/container/table cell o | cpp/string/basic_string/insert |
| n/a |  |
| cpp/container/table cell o | /vector/insert |
| cpp/container/table cell o | /deque/insert |
| cpp/container/table cell n | /forward_list/insert_after | insert_after |
| cpp/container/table cell o | /list/insert |
| cpp/container/table cell o | /set/insert |
| cpp/container/table cell o | /multiset/insert |
| cpp/container/table cell o | /map/insert |
| cpp/container/table cell o | /multimap/insert |
| cpp/container/table cell n | /unordered_set/insert |
| cpp/container/table cell n | /unordered_multiset/insert |
| cpp/container/table cell n | /unordered_map/insert |
| cpp/container/table cell n | /unordered_multimap/insert |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/insert |
| cpp/container/table cell 23 | /flat_multiset/insert |
| cpp/container/table cell 23 | /flat_map/insert |
| cpp/container/table cell 23 | /flat_multimap/insert |
| cpp/container/table cell lo | insert |
| - |
| cpp/container/table cell l23 | insert_range |
| cpp/container/table cell 23 | cpp/string/basic_string/insert_range |
| n/a |  |
| cpp/container/table cell 23 | /vector/insert_range |
| cpp/container/table cell 23 | /deque/insert_range |
| cpp/container/table cell 23 | /forward_list/insert_range_after | insert_range_after |
| cpp/container/table cell 23 | /list/insert_range |
| cpp/container/table cell 23 | /set/insert_range |
| cpp/container/table cell 23 | /multiset/insert_range |
| cpp/container/table cell 23 | /map/insert_range |
| cpp/container/table cell 23 | /multimap/insert_range |
| cpp/container/table cell 23 | /unordered_set/insert_range |
| cpp/container/table cell 23 | /unordered_multiset/insert_range |
| cpp/container/table cell 23 | /unordered_map/insert_range |
| cpp/container/table cell 23 | /unordered_multimap/insert_range |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/insert_range |
| cpp/container/table cell 23 | /flat_multiset/insert_range |
| cpp/container/table cell 23 | /flat_map/insert_range |
| cpp/container/table cell 23 | /flat_multimap/insert_range |
| cpp/container/table cell l23 | insert_range |
| - |
| cpp/container/table cell l17 | insert_or_assign |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 17 | /map/insert_or_assign |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 17 | /unordered_map/insert_or_assign |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_map/insert_or_assign |
| n/a |  |
| cpp/container/table cell l17 | insert_or_assign |
| - |
| cpp/container/table cell ln | emplace |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /vector/emplace |
| cpp/container/table cell n | /deque/emplace |
| cpp/container/table cell n | /forward_list/emplace_after | emplace_after |
| cpp/container/table cell n | /list/emplace |
| cpp/container/table cell n | /set/emplace |
| cpp/container/table cell n | /multiset/emplace |
| cpp/container/table cell n | /map/emplace |
| cpp/container/table cell n | /multimap/emplace |
| cpp/container/table cell n | /unordered_set/emplace |
| cpp/container/table cell n | /unordered_multiset/emplace |
| cpp/container/table cell n | /unordered_map/emplace |
| cpp/container/table cell n | /unordered_multimap/emplace |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/emplace |
| cpp/container/table cell 23 | /flat_multiset/emplace |
| cpp/container/table cell 23 | /flat_map/emplace |
| cpp/container/table cell 23 | /flat_multimap/emplace |
| cpp/container/table cell ln | emplace |
| - |
| cpp/container/table cell ln | emplace_hint |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /set/emplace_hint |
| cpp/container/table cell n | /multiset/emplace_hint |
| cpp/container/table cell n | /map/emplace_hint |
| cpp/container/table cell n | /multimap/emplace_hint |
| cpp/container/table cell n | /unordered_set/emplace_hint |
| cpp/container/table cell n | /unordered_multiset/emplace_hint |
| cpp/container/table cell n | /unordered_map/emplace_hint |
| cpp/container/table cell n | /unordered_multimap/emplace_hint |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/emplace_hint |
| cpp/container/table cell 23 | /flat_multiset/emplace_hint |
| cpp/container/table cell 23 | /flat_map/emplace_hint |
| cpp/container/table cell 23 | /flat_multimap/emplace_hint |
| cpp/container/table cell ln | emplace_hint |
| - |
| cpp/container/table cell l17 | try_emplace |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 17 | /map/try_emplace |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 17 | /unordered_map/try_emplace |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_map/try_emplace |
| n/a |  |
| cpp/container/table cell l17 | try_emplace |
| - |
| cpp/container/table cell lo | erase |
| cpp/container/table cell o | cpp/string/basic_string/erase |
| n/a |  |
| cpp/container/table cell o | /vector/erase |
| cpp/container/table cell o | /deque/erase |
| cpp/container/table cell n | /forward_list/erase_after | erase_after |
| cpp/container/table cell o | /list/erase |
| cpp/container/table cell o | /set/erase |
| cpp/container/table cell o | /multiset/erase |
| cpp/container/table cell o | /map/erase |
| cpp/container/table cell o | /multimap/erase |
| cpp/container/table cell n | /unordered_set/erase |
| cpp/container/table cell n | /unordered_multiset/erase |
| cpp/container/table cell n | /unordered_map/erase |
| cpp/container/table cell n | /unordered_multimap/erase |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/erase |
| cpp/container/table cell 23 | /flat_multiset/erase |
| cpp/container/table cell 23 | /flat_map/erase |
| cpp/container/table cell 23 | /flat_multimap/erase |
| cpp/container/table cell lo | erase |
| - |
| cpp/container/table cell lo | push_front |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /deque/push_front |
| cpp/container/table cell n | /forward_list/push_front |
| cpp/container/table cell o | /list/push_front |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | push_front |
| - |
| cpp/container/table cell l23 | prepend_range |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /deque/prepend_range |
| cpp/container/table cell 23 | /forward_list/prepend_range |
| cpp/container/table cell 23 | /list/prepend_range |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell l23 | prepend_range |
| - |
| cpp/container/table cell ln | emplace_front |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /deque/emplace_front |
| cpp/container/table cell n | /forward_list/emplace_front |
| cpp/container/table cell n | /list/emplace_front |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell ln | emplace_front |
| - |
| cpp/container/table cell lo | pop_front |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /deque/pop_front |
| cpp/container/table cell n | /forward_list/pop_front |
| cpp/container/table cell o | /list/pop_front |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /queue/pop |
| cpp/container/table cell o | /priority_queue/pop |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | pop_front |
| - |
| cpp/container/table cell lo | push_back |
| cpp/container/table cell o | cpp/string/basic_string/push_back |
| n/a |  |
| cpp/container/table cell o | /vector/push_back |
| cpp/container/table cell o | /deque/push_back |
| n/a |  |
| cpp/container/table cell o | /list/push_back |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /stack/push |
| cpp/container/table cell o | /queue/push |
| cpp/container/table cell o | /priority_queue/push |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | push_back |
| - |
| cpp/container/table cell l23 | append_range |
| cpp/container/table cell 23 | cpp/string/basic_string/append_range |
| n/a |  |
| cpp/container/table cell 23 | /vector/append_range |
| cpp/container/table cell 23 | /deque/append_range |
| n/a |  |
| cpp/container/table cell 23 | /list/append_range |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /stack/push_range |
| cpp/container/table cell 23 | /queue/push_range |
| cpp/container/table cell 23 | /priority_queue/push_range |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell l23 | append_range |
| - |
| cpp/container/table cell ln | emplace_back |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /vector/emplace_back |
| cpp/container/table cell n | /deque/emplace_back |
| n/a |  |
| cpp/container/table cell n | /list/emplace_back |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /stack/emplace |
| cpp/container/table cell n | /queue/emplace |
| cpp/container/table cell n | /priority_queue/emplace |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell ln | emplace_back |
| - |
| cpp/container/table cell lo | pop_back |
| cpp/container/table cell n | cpp/string/basic_string/pop_back |
| n/a |  |
| cpp/container/table cell o | /vector/pop_back |
| cpp/container/table cell o | /deque/pop_back |
| n/a |  |
| cpp/container/table cell o | /list/pop_back |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /stack/pop |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | pop_back |
| - |
| cpp/container/table cell lo | swap |
| cpp/container/table cell o | cpp/string/basic_string/swap |
| cpp/container/table cell n | /array/swap |
| cpp/container/table cell o | /vector/swap |
| cpp/container/table cell o | /deque/swap |
| cpp/container/table cell n | /forward_list/swap |
| cpp/container/table cell o | /list/swap |
| cpp/container/table cell o | /set/swap |
| cpp/container/table cell o | /multiset/swap |
| cpp/container/table cell o | /map/swap |
| cpp/container/table cell o | /multimap/swap |
| cpp/container/table cell n | /unordered_set/swap |
| cpp/container/table cell n | /unordered_multiset/swap |
| cpp/container/table cell n | /unordered_map/swap |
| cpp/container/table cell n | /unordered_multimap/swap |
| cpp/container/table cell n | /stack/swap |
| cpp/container/table cell n | /queue/swap |
| cpp/container/table cell n | /priority_queue/swap |
| cpp/container/table cell 23 | /unordered_set/swap |
| cpp/container/table cell 23 | /unordered_multiset/swap |
| cpp/container/table cell 23 | /unordered_map/swap |
| cpp/container/table cell 23 | /unordered_multimap/swap |
| cpp/container/table cell lo | swap |
| - |
| cpp/container/table cell lo | merge |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /forward_list/merge |
| cpp/container/table cell o | /list/merge |
| cpp/container/table cell 17 | /set/merge |
| cpp/container/table cell 17 | /multiset/merge |
| cpp/container/table cell 17 | /map/merge |
| cpp/container/table cell 17 | /multimap/merge |
| cpp/container/table cell 17 | /unordered_set/merge |
| cpp/container/table cell 17 | /unordered_multiset/merge |
| cpp/container/table cell 17 | /unordered_map/merge |
| cpp/container/table cell 17 | /unordered_multimap/merge |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | merge |
| - |
| cpp/container/table cell l17 | extract <ref>e.g., c | node_type extract(const_iterator) or c | node_type extract(Key&)</ref> |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 17 | /set/extract |
| cpp/container/table cell 17 | /multiset/extract |
| cpp/container/table cell 17 | /map/extract |
| cpp/container/table cell 17 | /multimap/extract |
| cpp/container/table cell 17 | /unordered_set/extract |
| cpp/container/table cell 17 | /unordered_multiset/extract |
| cpp/container/table cell 17 | /unordered_map/extract |
| cpp/container/table cell 17 | /unordered_multimap/extract |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell l17 | extract |
| - |
| rowspan="6" | List operations |
| cpp/container/table cell lo | splice |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /forward_list/splice_after | splice_after |
| cpp/container/table cell o | /list/splice |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | splice |
| rowspan="6" | List operations |
| - |
| cpp/container/table cell lo | remove |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /forward_list/remove |
| cpp/container/table cell o | /list/remove |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | remove |
| - |
| cpp/container/table cell lo | remove_if |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /forward_list/remove | remove_if |
| cpp/container/table cell o | /list/remove | remove_if |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | remove_if |
| - |
| cpp/container/table cell lo | reverse |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /forward_list/reverse |
| cpp/container/table cell o | /list/reverse |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | reverse |
| - |
| cpp/container/table cell lo | unique |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /forward_list/unique |
| cpp/container/table cell o | /list/unique |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | unique |
| - |
| cpp/container/table cell lo | sort |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /forward_list/sort |
| cpp/container/table cell o | /list/sort |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | sort |
| - |
| rowspan="9" | Bucket and Hash |
| cpp/container/table cell lnn | begin(size_type) | cbegin(size_type) |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell nn | /unordered_set/begin2 | begin(size_type) | cbegin(size_type) |
| cpp/container/table cell nn | /unordered_multiset/begin2 | begin(size_type) | cbegin(size_type) |
| cpp/container/table cell nn | /unordered_map/begin2 | begin(size_type) | cbegin(size_type) |
| cpp/container/table cell nn | /unordered_multimap/begin2 | begin(size_type) | cbegin(size_type) |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lnn | begin(size_type) | cbegin(size_type) |
| rowspan="9" | Bucket and Hash |
| - |
| cpp/container/table cell lnn | end(size_type) | cend(size_type) |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell nn | /unordered_set/end2 | end(size_type) | cend(size_type) |
| cpp/container/table cell nn | /unordered_multiset/end2 | end(size_type) | cend(size_type) |
| cpp/container/table cell nn | /unordered_map/end2 | end(size_type) | cend(size_type) |
| cpp/container/table cell nn | /unordered_multimap/end | end(size_type) | cend(size_type) |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lnn | end(size_type) | cend(size_type) |
| - |
| cpp/container/table cell ln | bucket_count |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /unordered_set/bucket_count |
| cpp/container/table cell n | /unordered_multiset/bucket_count |
| cpp/container/table cell n | /unordered_map/bucket_count |
| cpp/container/table cell n | /unordered_multimap/bucket_count |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell ln | bucket_count |
| - |
| cpp/container/table cell ln | max_bucket_count |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /unordered_set/max_bucket_count |
| cpp/container/table cell n | /unordered_multiset/max_bucket_count |
| cpp/container/table cell n | /unordered_map/max_bucket_count |
| cpp/container/table cell n | /unordered_multimap/max_bucket_count |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell ln | max_bucket_count |
| - |
| cpp/container/table cell ln | bucket_size |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /unordered_set/bucket_size |
| cpp/container/table cell n | /unordered_multiset/bucket_size |
| cpp/container/table cell n | /unordered_map/bucket_size |
| cpp/container/table cell n | /unordered_multimap/bucket_size |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell ln | bucket_size |
| - |
| cpp/container/table cell ln | bucket |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /unordered_set/bucket |
| cpp/container/table cell n | /unordered_multiset/bucket |
| cpp/container/table cell n | /unordered_map/bucket |
| cpp/container/table cell n | /unordered_multimap/bucket |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell ln | bucket |
| - |
| cpp/container/table cell ln | load_factor |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /unordered_set/load_factor |
| cpp/container/table cell n | /unordered_multiset/load_factor |
| cpp/container/table cell n | /unordered_map/load_factor |
| cpp/container/table cell n | /unordered_multimap/load_factor |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell ln | load_factor |
| - |
| cpp/container/table cell ln | max_load_factor |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /unordered_set/max_load_factor |
| cpp/container/table cell n | /unordered_multiset/max_load_factor |
| cpp/container/table cell n | /unordered_map/max_load_factor |
| cpp/container/table cell n | /unordered_multimap/max_load_factor |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell ln | max_load_factor |
| - |
| cpp/container/table cell ln | rehash |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /unordered_set/rehash |
| cpp/container/table cell n | /unordered_multiset/rehash |
| cpp/container/table cell n | /unordered_map/rehash |
| cpp/container/table cell n | /unordered_multimap/rehash |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell ln | rehash |
| - |
| rowspan="6" | Lookup |
| cpp/container/table cell lo | count |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /set/count |
| cpp/container/table cell o | /multiset/count |
| cpp/container/table cell o | /map/count |
| cpp/container/table cell o | /multimap/count |
| cpp/container/table cell n | /unordered_set/count |
| cpp/container/table cell n | /unordered_multiset/count |
| cpp/container/table cell n | /unordered_map/count |
| cpp/container/table cell n | /unordered_multimap/count |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/count |
| cpp/container/table cell 23 | /flat_multiset/count |
| cpp/container/table cell 23 | /flat_map/count |
| cpp/container/table cell 23 | /flat_multimap/count |
| cpp/container/table cell lo | count |
| rowspan="6" | Lookup |
| - |
| cpp/container/table cell lo | find |
| cpp/container/table cell o | cpp/string/basic_string/find |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /set/find |
| cpp/container/table cell o | /multiset/find |
| cpp/container/table cell o | /map/find |
| cpp/container/table cell o | /multimap/find |
| cpp/container/table cell n | /unordered_set/find |
| cpp/container/table cell n | /unordered_multiset/find |
| cpp/container/table cell n | /unordered_map/find |
| cpp/container/table cell n | /unordered_multimap/find |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/find |
| cpp/container/table cell 23 | /flat_multiset/find |
| cpp/container/table cell 23 | /flat_map/find |
| cpp/container/table cell 23 | /flat_multimap/find |
| cpp/container/table cell lo | find |
| - |
| cpp/container/table cell l20 | contains |
| cpp/container/table cell 23 | cpp/string/basic_string/contains |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 20 | /set/contains |
| cpp/container/table cell 20 | /multiset/contains |
| cpp/container/table cell 20 | /map/contains |
| cpp/container/table cell 20 | /multimap/contains |
| cpp/container/table cell 20 | /unordered_set/contains |
| cpp/container/table cell 20 | /unordered_multiset/contains |
| cpp/container/table cell 20 | /unordered_map/contains |
| cpp/container/table cell 20 | /unordered_multimap/contains |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/contains |
| cpp/container/table cell 23 | /flat_multiset/contains |
| cpp/container/table cell 23 | /flat_map/contains |
| cpp/container/table cell 23 | /flat_multimap/contains |
| cpp/container/table cell l20 | contains |
| - |
| cpp/container/table cell lo | lower_bound |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /set/lower_bound |
| cpp/container/table cell o | /multiset/lower_bound |
| cpp/container/table cell o | /map/lower_bound |
| cpp/container/table cell o | /multimap/lower_bound |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/lower_bound |
| cpp/container/table cell 23 | /flat_multiset/lower_bound |
| cpp/container/table cell 23 | /flat_map/lower_bound |
| cpp/container/table cell 23 | /flat_multimap/lower_bound |
| cpp/container/table cell lo | lower_bound |
| - |
| cpp/container/table cell lo | upper_bound |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /set/upper_bound |
| cpp/container/table cell o | /multiset/upper_bound |
| cpp/container/table cell o | /map/upper_bound |
| cpp/container/table cell o | /multimap/upper_bound |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/upper_bound |
| cpp/container/table cell 23 | /flat_multiset/upper_bound |
| cpp/container/table cell 23 | /flat_map/upper_bound |
| cpp/container/table cell 23 | /flat_multimap/upper_bound |
| cpp/container/table cell lo | upper_bound |
| - |
| cpp/container/table cell lo | equal_range |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /set/equal_range |
| cpp/container/table cell o | /multiset/equal_range |
| cpp/container/table cell o | /map/equal_range |
| cpp/container/table cell o | /multimap/equal_range |
| cpp/container/table cell n | /unordered_set/equal_range |
| cpp/container/table cell n | /unordered_multiset/equal_range |
| cpp/container/table cell n | /unordered_map/equal_range |
| cpp/container/table cell n | /unordered_multimap/equal_range |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/equal_range |
| cpp/container/table cell 23 | /flat_multiset/equal_range |
| cpp/container/table cell 23 | /flat_map/equal_range |
| cpp/container/table cell 23 | /flat_multimap/equal_range |
| cpp/container/table cell lo | equal_range |
| - |
| rowspan="4" | Observers |
| cpp/container/table cell lo | key_comp |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /set/key_comp |
| cpp/container/table cell o | /multiset/key_comp |
| cpp/container/table cell o | /map/key_comp |
| cpp/container/table cell o | /multimap/key_comp |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/key_comp |
| cpp/container/table cell 23 | /flat_multiset/key_comp |
| cpp/container/table cell 23 | /flat_map/key_comp |
| cpp/container/table cell 23 | /flat_multimap/key_comp |
| cpp/container/table cell lo | key_comp |
| rowspan="4" | Observers |
| - |
| cpp/container/table cell lo | value_comp |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /set/value_comp |
| cpp/container/table cell o | /multiset/value_comp |
| cpp/container/table cell o | /map/value_comp |
| cpp/container/table cell o | /multimap/value_comp |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/value_comp |
| cpp/container/table cell 23 | /flat_multiset/value_comp |
| cpp/container/table cell 23 | /flat_map/value_comp |
| cpp/container/table cell 23 | /flat_multimap/value_comp |
| cpp/container/table cell lo | value_comp |
| - |
| cpp/container/table cell ln | hash_function |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /unordered_set/hash_function |
| cpp/container/table cell n | /unordered_multiset/hash_function |
| cpp/container/table cell n | /unordered_map/hash_function |
| cpp/container/table cell n | /unordered_multimap/hash_function |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell ln | hash_function |
| - |
| cpp/container/table cell ln | key_eq |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell n | /unordered_set/key_eq |
| cpp/container/table cell n | /unordered_multiset/key_eq |
| cpp/container/table cell n | /unordered_map/key_eq |
| cpp/container/table cell n | /unordered_multimap/key_eq |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell ln | key_eq |
| - |
| Allocator |
| cpp/container/table cell lo | get_allocator |
| cpp/container/table cell o | cpp/string/basic_string/get_allocator |
| n/a |  |
| cpp/container/table cell o | /vector/get_allocator |
| cpp/container/table cell o | /deque/get_allocator |
| cpp/container/table cell n | /forward_list/get_allocator |
| cpp/container/table cell o | /list/get_allocator |
| cpp/container/table cell o | /set/get_allocator |
| cpp/container/table cell o | /multiset/get_allocator |
| cpp/container/table cell o | /map/get_allocator |
| cpp/container/table cell o | /multimap/get_allocator |
| cpp/container/table cell n | /unordered_set/get_allocator |
| cpp/container/table cell n | /unordered_multiset/get_allocator |
| cpp/container/table cell n | /unordered_map/get_allocator |
| cpp/container/table cell n | /unordered_multimap/get_allocator |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | get_allocator |
| Allocator |
| - |
| rowspan="2" | Adaptors |
| cpp/container/table cell l23 | extract <ref>e.g., c | container_type extract() && |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/extract |
| cpp/container/table cell 23 | /flat_multiset/extract |
| cpp/container/table cell 23 | /flat_map/extract |
| cpp/container/table cell 23 | /flat_multimap/extract |
| cpp/container/table cell l23 | extract |
| rowspan="2" | Adaptors |
| - |
| cpp/container/table cell l23 | replace |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/replace |
| cpp/container/table cell 23 | /flat_multiset/replace |
| cpp/container/table cell 23 | /flat_map/replace |
| cpp/container/table cell 23 | /flat_multimap/replace |
| cpp/container/table cell l23 | replace |
| - |
| colspan="2" | Container |
| cpp/container/table cell ho | cpp/string/basic_string |
| cpp/container/table cell hn | /array |
| cpp/container/table cell ho | /vector |
| cpp/container/table cell ho | /deque |
| cpp/container/table cell hn | /forward_list |
| cpp/container/table cell ho | /list |
| cpp/container/table cell ho | /set |
| cpp/container/table cell ho | /multiset |
| cpp/container/table cell ho | /map |
| cpp/container/table cell ho | /multimap |
| cpp/container/table cell hn | /unordered_set |
| cpp/container/table cell hn | /unordered_multiset |
| cpp/container/table cell hn | /unordered_map |
| cpp/container/table cell hn | /unordered_multimap |
| cpp/container/table cell ho | /stack |
| cpp/container/table cell ho | /queue |
| cpp/container/table cell ho | /priority_queue |
| cpp/container/table cell h23 | /flat_set |
| cpp/container/table cell h23 | /flat_multiset |
| cpp/container/table cell h23 | /flat_map |
| cpp/container/table cell h23 | /flat_multimap |
| colspan="2" | Container |
| - |
| colspan="2" | Header |
| tt | header | string |
| tt | header | array |
| tt | header | vector |
| tt | header | deque |
| tt | header | forward_list |
| tt | header | list |
| colspan="2" | tt | header | set |
| colspan="2" | tt | header | map |
| colspan="2" | tt | header | unordered_set |
| colspan="2" | tt | header | unordered_map |
| tt | header | stack |
| colspan="2" | tt | header | queue |
| colspan="2" | tt | header | flat_set |
| colspan="2" | tt | header | flat_map |
| colspan="2" | Header |
| - |
| colspan="2" |  |
| colspan="1" | Pseudo container |
| colspan="5" | Sequence containers |
| colspan="4" | Associative containers |
| colspan="4" | Unordered associative containers |
| colspan="7" | Container adaptors |
| colspan="2" |  |

</div>
* Note: functions in two different `extract` lines have different meanings and syntax:

### Non-member function table

<div style="max-width: 100%; max-height: 80vh; overflow: scroll;">


| - |
| colspan="2" |  |
| colspan="1" | Pseudo container |
| colspan="5" | Sequence containers |
| colspan="4" | Associative containers |
| colspan="4" | Unordered associative containers |
| colspan="7" | Container adaptors |
| colspan="2" |  |
| - |
| colspan="2" | Header |
| tt | header | string |
| tt | header | array |
| tt | header | vector |
| tt | header | deque |
| tt | header | forward_list |
| tt | header | list |
| colspan="2" | tt | header | set |
| colspan="2" | tt | header | map |
| colspan="2" | tt | header | unordered_set |
| colspan="2" | tt | header | unordered_map |
| tt | header | stack |
| colspan="2" | tt | header | queue |
| colspan="2" | tt | header | flat_set |
| colspan="2" | tt | header | flat_map |
| colspan="2" | Header |
| - |
| colspan="2" | Container |
| cpp/container/table cell ho | cpp/string/basic_string |
| cpp/container/table cell hn | /array |
| cpp/container/table cell ho | /vector |
| cpp/container/table cell ho | /deque |
| cpp/container/table cell hn | /forward_list |
| cpp/container/table cell ho | /list |
| cpp/container/table cell ho | /set |
| cpp/container/table cell ho | /multiset |
| cpp/container/table cell ho | /map |
| cpp/container/table cell ho | /multimap |
| cpp/container/table cell hn | /unordered_set |
| cpp/container/table cell hn | /unordered_multiset |
| cpp/container/table cell hn | /unordered_map |
| cpp/container/table cell hn | /unordered_multimap |
| cpp/container/table cell ho | /stack |
| cpp/container/table cell ho | /queue |
| cpp/container/table cell ho | /priority_queue |
| cpp/container/table cell h23 | /flat_set |
| cpp/container/table cell h23 | /flat_multiset |
| cpp/container/table cell h23 | /flat_map |
| cpp/container/table cell h23 | /flat_multimap |
| colspan="2" | Container |
| - |
| rowspan="10" | Non-member function |
| cpp/container/table cell lo | operator |
| cpp/container/table cell o | cpp/string/basic_string/operator_cmp | operator |
| cpp/container/table cell n | /array/operator_cmp | operator |
| cpp/container/table cell o | /vector/operator_cmp | operator |
| cpp/container/table cell o | /deque/operator_cmp | operator |
| cpp/container/table cell n | /forward_list/operator_cmp | operator |
| cpp/container/table cell o | /list/operator_cmp | operator |
| cpp/container/table cell o | /set/operator_cmp | operator |
| cpp/container/table cell o | /multiset/operator_cmp | operator |
| cpp/container/table cell o | /map/operator_cmp | operator |
| cpp/container/table cell o | /multimap/operator_cmp | operator |
| cpp/container/table cell n | /unordered_set/operator_cmp | operator |
| cpp/container/table cell n | /unordered_multiset/operator_cmp | operator |
| cpp/container/table cell n | /unordered_map/operator_cmp | operator |
| cpp/container/table cell n | /unordered_multimap/operator_cmp | operator |
| cpp/container/table cell o | /stack/operator_cmp | operator |
| cpp/container/table cell o | /queue/operator_cmp | operator |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/operator_cmp | operator |
| cpp/container/table cell 23 | /flat_multiset/operator_cmp | operator |
| cpp/container/table cell 23 | /flat_map/operator_cmp | operator |
| cpp/container/table cell 23 | /flat_multimap/operator_cmp | operator |
| cpp/container/table cell lo | operator |
| rowspan="10" | Non-member function |
| - |
| cpp/container/table cell lo | operator! mark until c++20 | removed=yes |
| cpp/container/table cell o | cpp/string/basic_string/operator_cmp | operator! |
| cpp/container/table cell n | /array/operator_cmp | operator! |
| cpp/container/table cell o | /vector/operator_cmp | operator! |
| cpp/container/table cell o | /deque/operator_cmp | operator! |
| cpp/container/table cell n | /forward_list/operator_cmp | operator! |
| cpp/container/table cell o | /list/operator_cmp | operator! |
| cpp/container/table cell o | /set/operator_cmp | operator! |
| cpp/container/table cell o | /multiset/operator_cmp | operator! |
| cpp/container/table cell o | /map/operator_cmp | operator! |
| cpp/container/table cell o | /multimap/operator_cmp | operator! |
| cpp/container/table cell n | /unordered_set/operator_cmp | operator! |
| cpp/container/table cell n | /unordered_multiset/operator_cmp | operator! |
| cpp/container/table cell n | /unordered_map/operator_cmp | operator! |
| cpp/container/table cell n | /unordered_multimap/operator_cmp | operator! |
| cpp/container/table cell o | /stack/operator_cmp | operator! |
| cpp/container/table cell o | /queue/operator_cmp | operator! |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | operator! mark until c++20 | removed=yes |
| - |
| cpp/container/table cell lo | operator< mark until c++20 | removed=yes |
| cpp/container/table cell o | cpp/string/basic_string/operator_cmp | operator< |
| cpp/container/table cell n | /array/operator_cmp | operator< |
| cpp/container/table cell o | /vector/operator_cmp | operator< |
| cpp/container/table cell o | /deque/operator_cmp | operator< |
| cpp/container/table cell n | /forward_list/operator_cmp | operator< |
| cpp/container/table cell o | /list/operator_cmp | operator< |
| cpp/container/table cell o | /set/operator_cmp | operator< |
| cpp/container/table cell o | /multiset/operator_cmp | operator< |
| cpp/container/table cell o | /map/operator_cmp | operator< |
| cpp/container/table cell o | /multimap/operator_cmp | operator< |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /stack/operator_cmp | operator< |
| cpp/container/table cell o | /queue/operator_cmp | operator< |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | operator< mark until c++20 | removed=yes |
| - |
| cpp/container/table cell lo | operator< mark until c++20 | removed=yes |
| cpp/container/table cell o | cpp/string/basic_string/operator_cmp | operator< |
| cpp/container/table cell n | /array/operator_cmp | operator< |
| cpp/container/table cell o | /vector/operator_cmp | operator< |
| cpp/container/table cell o | /deque/operator_cmp | operator< |
| cpp/container/table cell n | /forward_list/operator_cmp | operator< |
| cpp/container/table cell o | /list/operator_cmp | operator< |
| cpp/container/table cell o | /set/operator_cmp | operator< |
| cpp/container/table cell o | /multiset/operator_cmp | operator< |
| cpp/container/table cell o | /map/operator_cmp | operator< |
| cpp/container/table cell o | /multimap/operator_cmp | operator< |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /stack/operator_cmp | operator< |
| cpp/container/table cell o | /queue/operator_cmp | operator< |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | operator< mark until c++20 | removed=yes |
| - |
| cpp/container/table cell lo | operator> mark until c++20 | removed=yes |
| cpp/container/table cell o | cpp/string/basic_string/operator_cmp | operator> |
| cpp/container/table cell n | /array/operator_cmp | operator> |
| cpp/container/table cell o | /vector/operator_cmp | operator> |
| cpp/container/table cell o | /deque/operator_cmp | operator> |
| cpp/container/table cell n | /forward_list/operator_cmp | operator> |
| cpp/container/table cell o | /list/operator_cmp | operator> |
| cpp/container/table cell o | /set/operator_cmp | operator> |
| cpp/container/table cell o | /multiset/operator_cmp | operator> |
| cpp/container/table cell o | /map/operator_cmp | operator> |
| cpp/container/table cell o | /multimap/operator_cmp | operator> |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /stack/operator_cmp | operator> |
| cpp/container/table cell o | /queue/operator_cmp | operator> |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | operator> mark until c++20 | removed=yes |
| - |
| cpp/container/table cell lo | operator> mark until c++20 | removed=yes |
| cpp/container/table cell o | cpp/string/basic_string/operator_cmp | operator> |
| cpp/container/table cell n | /array/operator_cmp | operator> |
| cpp/container/table cell o | /vector/operator_cmp | operator> |
| cpp/container/table cell o | /deque/operator_cmp | operator> |
| cpp/container/table cell n | /forward_list/operator_cmp | operator> |
| cpp/container/table cell o | /list/operator_cmp | operator> |
| cpp/container/table cell o | /set/operator_cmp | operator> |
| cpp/container/table cell o | /multiset/operator_cmp | operator> |
| cpp/container/table cell o | /map/operator_cmp | operator> |
| cpp/container/table cell o | /multimap/operator_cmp | operator> |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell o | /stack/operator_cmp | operator> |
| cpp/container/table cell o | /queue/operator_cmp | operator> |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell lo | operator> mark until c++20 | removed=yes |
| - |
| cpp/container/table cell l20 | operator<> |
| cpp/container/table cell 20 | cpp/string/basic_string/operator_cmp | operator<> |
| cpp/container/table cell 20 | /array/operator_cmp | operator<> |
| cpp/container/table cell 20 | /vector/operator_cmp | operator<> |
| cpp/container/table cell 20 | /deque/operator_cmp | operator<> |
| cpp/container/table cell 20 | /forward_list/operator_cmp | operator<> |
| cpp/container/table cell 20 | /list/operator_cmp | operator<> |
| cpp/container/table cell 20 | /set/operator_cmp | operator<> |
| cpp/container/table cell 20 | /multiset/operator_cmp | operator<> |
| cpp/container/table cell 20 | /map/operator_cmp | operator<> |
| cpp/container/table cell 20 | /multimap/operator_cmp | operator<> |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 20 | /stack/operator_cmp | operator<> |
| cpp/container/table cell 20 | /queue/operator_cmp | operator<> |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/operator_cmp | operator<> |
| cpp/container/table cell 23 | /flat_multiset/operator_cmp | operator<> |
| cpp/container/table cell 23 | /flat_map/operator_cmp | operator<> |
| cpp/container/table cell 23 | /flat_multimap/operator_cmp | operator<> |
| cpp/container/table cell l20 | operator<> |
| - |
| cpp/container/table cell lo | swap |
| cpp/container/table cell o | cpp/string/basic_string/swap |
| cpp/container/table cell n | /array/swap |
| cpp/container/table cell o | /vector/swap |
| cpp/container/table cell o | /deque/swap |
| cpp/container/table cell n | /forward_list/swap |
| cpp/container/table cell o | /list/swap |
| cpp/container/table cell o | /set/swap |
| cpp/container/table cell o | /multiset/swap |
| cpp/container/table cell o | /map/swap |
| cpp/container/table cell o | /multimap/swap |
| cpp/container/table cell n | /unordered_set/swap |
| cpp/container/table cell n | /unordered_multiset/swap |
| cpp/container/table cell n | /unordered_map/swap |
| cpp/container/table cell n | /unordered_multimap/swap |
| cpp/container/table cell o | /stack/swap |
| cpp/container/table cell o | /queue/swap |
| cpp/container/table cell o | /priority_queue/swap |
| cpp/container/table cell 23 | /flat_set/swap |
| cpp/container/table cell 23 | /flat_multiset/swap |
| cpp/container/table cell 23 | /flat_map/swap |
| cpp/container/table cell 23 | /flat_multimap/swap |
| cpp/container/table cell lo | swap |
| - |
| cpp/container/table cell l20 | erase |
| cpp/container/table cell 20 | cpp/string/basic_string/erase2 | erase |
| n/a |  |
| cpp/container/table cell 20 | /vector/erase2 | erase |
| cpp/container/table cell 20 | /deque/erase2 | erase |
| cpp/container/table cell 20 | /forward_list/erase2 | erase |
| cpp/container/table cell 20 | /list/erase2 | erase |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell l20 | erase |
| - |
| cpp/container/table cell l20 | erase_if |
| cpp/container/table cell 20 | cpp/string/basic_string/erase2 | erase_if |
| n/a |  |
| cpp/container/table cell 20 | /vector/erase2 | erase_if |
| cpp/container/table cell 20 | /deque/erase2 | erase_if |
| cpp/container/table cell 20 | /forward_list/erase2 | erase_if |
| cpp/container/table cell 20 | /list/erase2 | erase_if |
| cpp/container/table cell 20 | /set/erase_if | erase_if |
| cpp/container/table cell 20 | /multiset/erase_if | erase_if |
| cpp/container/table cell 20 | /map/erase_if | erase_if |
| cpp/container/table cell 20 | /multimap/erase_if | erase_if |
| cpp/container/table cell 20 | /unordered_set/erase_if | erase_if |
| cpp/container/table cell 20 | /unordered_multiset/erase_if | erase_if |
| cpp/container/table cell 20 | /unordered_map/erase_if | erase_if |
| cpp/container/table cell 20 | /unordered_multimap/erase_if | erase_if |
| n/a |  |
| n/a |  |
| n/a |  |
| cpp/container/table cell 23 | /flat_set/erase_if | erase_if |
| cpp/container/table cell 23 | /flat_multiset/erase_if | erase_if |
| cpp/container/table cell 23 | /flat_map/erase_if | erase_if |
| cpp/container/table cell 23 | /flat_multimap/erase_if | erase_if |
| cpp/container/table cell l20 | erase_if |
| - |
| colspan="2" | Container |
| cpp/container/table cell ho | cpp/string/basic_string |
| cpp/container/table cell hn | /array |
| cpp/container/table cell ho | /vector |
| cpp/container/table cell ho | /deque |
| cpp/container/table cell hn | /forward_list |
| cpp/container/table cell ho | /list |
| cpp/container/table cell ho | /set |
| cpp/container/table cell ho | /multiset |
| cpp/container/table cell ho | /map |
| cpp/container/table cell ho | /multimap |
| cpp/container/table cell hn | /unordered_set |
| cpp/container/table cell hn | /unordered_multiset |
| cpp/container/table cell hn | /unordered_map |
| cpp/container/table cell hn | /unordered_multimap |
| cpp/container/table cell ho | /stack |
| cpp/container/table cell ho | /queue |
| cpp/container/table cell ho | /priority_queue |
| cpp/container/table cell h23 | /flat_set |
| cpp/container/table cell h23 | /flat_multiset |
| cpp/container/table cell h23 | /flat_map |
| cpp/container/table cell h23 | /flat_multimap |
| colspan="2" | Container |
| - |
| colspan="2" | Header |
| tt | header | string |
| tt | header | array |
| tt | header | vector |
| tt | header | deque |
| tt | header | forward_list |
| tt | header | list |
| colspan="2" | tt | header | set |
| colspan="2" | tt | header | map |
| colspan="2" | tt | header | unordered_set |
| colspan="2" | tt | header | unordered_map |
| tt | header | stack |
| colspan="2" | tt | header | queue |
| colspan="2" | tt | header | flat_set |
| colspan="2" | tt | header | flat_map |
| colspan="2" | Header |
| - |
| colspan="2" |  |
| colspan="1" | Pseudo container |
| colspan="5" | Sequence containers |
| colspan="4" | Associative containers |
| colspan="4" | Unordered associative containers |
| colspan="7" | Container adaptors |
| colspan="2" |  |

</div>
rrev|since=c++20|

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-51 | C++98 | container iterators might be invalidated<br>by arbitrary library operation | they are only invalidated<br>when specified |


## See also

C++ named requirements:
* *Container*
* *SequenceContainer*
* *ContiguousContainer*
* *ReversibleContainer*
* *AssociativeContainer*
* *AllocatorAwareContainer*
* *UnorderedAssociativeContainer*


| cpp/numeric/dsc valarray | (see dedicated page) |
| cpp/string/dsc basic string | (see dedicated page) |
| cpp/string/dsc basic string view | (see dedicated page) |


---
title: std::match_results
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/match_results
---


```cpp
**Header:** `<`regex`>`
dcl|num=1|since=c++11|1=
template<
class BidirIt,
class Alloc = std::allocator<std::sub_match<BidirIt>>
> class match_results;
dcl|num=2|since=c++17|1=
namespace pmr {
template <class BidirIt>
using match_results = std::match_results<BidirIt,
std::pmr::polymorphic_allocator<
std::sub_match<BidirIt>>>;
}
```

The class template `std::match_results` holds a collection of character sequences that represent the result of a regular expression match.
This is a specialized allocator-aware container. It can only be default created, obtained from `std::regex_iterator`, or modified by `std::regex_search` or `std::regex_match`. Because `std::match_results` holds `std::sub_match`es, each of which is a pair of iterators into the original character sequence that was matched, it's undefined behavior to examine `std::match_results` if the original character sequence was destroyed or iterators to it were invalidated for other reasons.
The first `std::sub_match` (index 0) contained in a `std::match_result` always represents the full match within a target sequence made by a regex, and subsequent `std::sub_match`es represent sub-expression matches corresponding in sequence to the left parenthesis delimiting the sub-expression in the regex.
`std::match_results` meets the requirements of a *AllocatorAwareContainer* and of a *SequenceContainer*, except that only copy assignment, move assignment, and operations defined for a constant containers are supported, and that the semantics of comparison functions are different from those required for a container.

## Type requirements


### Parameters

- `BidirIt`
- `Alloc`

## Specializations

Several specializations for common character sequence types are provided:


| Item | Description |
|------|-------------|
| regex | |
| **Type** | Definition |


## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/regex/match_results/dsc constructor | (see dedicated page) |
| cpp/regex/match_results/dsc destructor | (see dedicated page) |
| cpp/regex/match_results/dsc operator{{= | (see dedicated page) |
| cpp/regex/match_results/dsc get_allocator | (see dedicated page) |

#### State


#### Size

| cpp/regex/match_results/dsc empty | (see dedicated page) |
| cpp/regex/match_results/dsc size | (see dedicated page) |
| cpp/regex/match_results/dsc max_size | (see dedicated page) |

#### Element access

| cpp/regex/match_results/dsc length | (see dedicated page) |
| cpp/regex/match_results/dsc position | (see dedicated page) |
| cpp/regex/match_results/dsc str | (see dedicated page) |
| cpp/regex/match_results/dsc operator_at | (see dedicated page) |
| cpp/regex/match_results/dsc prefix | (see dedicated page) |
| cpp/regex/match_results/dsc suffix | (see dedicated page) |

#### Iterators

| cpp/regex/match_results/dsc begin | (see dedicated page) |
| cpp/regex/match_results/dsc end | (see dedicated page) |

#### Format

| cpp/regex/match_results/dsc format | (see dedicated page) |

#### Modifiers

| cpp/regex/match_results/dsc swap | (see dedicated page) |


## Non-member functions


| cpp/regex/match_results/dsc operator_cmp | (see dedicated page) |
| cpp/regex/match_results/dsc swap2 | (see dedicated page) |


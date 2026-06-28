---
title: operators (std::match_results)
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/match_results/operator_cmp
---


# 1=operator==,!=small|(std::match_results)


```cpp
**Header:** `<`regex`>`
dcl|num=1|since=c++11|1=
template< class BidirIt, class Alloc >
bool operator==( match_results<BidirIt,Alloc>& lhs,
match_results<BidirIt,Alloc>& rhs );
dcl|num=2|since=c++11|until=c++20|1=
template< class BidirIt, class Alloc >
bool operator!=( match_results<BidirIt,Alloc>& lhs,
match_results<BidirIt,Alloc>& rhs );
```

Compares two `match_results` objects.
Two `match_results` are equal if the following conditions are met:
* neither of the objects is ''ready'', ''or''
* both match results are ''ready'' and the following conditions are met:
:* `lhs.empty()` and `rhs.empty()`, ''or''
:* `!lhs.empty()` and `!rhs.empty()` and the following conditions are met:
::* `1=lhs.prefix() == rhs.prefix()`
::* `1=lhs.size() == rhs.size() && std::equal(lhs.begin(), lhs.end(), rhs.begin())`
::* `1=lhs.suffix() == rhs.suffix()`
1. Checks if `lhs` and `rhs` are equal.
2. Checks if `lhs` and `rhs` are not equal.
rrev|since=c++20|

## Parameters


### Parameters

- `lhs, rhs` - match results to compare

**Type requirements:**

- `BidirIt`
- `Alloc`

## Return value

1. `true` if `lhs` and `rhs` are equal, `false` otherwise.
2. `true` if `lhs` and `rhs` are not equal, `false` otherwise.

## Example


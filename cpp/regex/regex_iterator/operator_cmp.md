---
title: std::regex_iterator::operators
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_iterator/operator_cmp
---


```cpp
dcl|num=1|since=c++11|1=
bool operator==( const regex_iterator& rhs ) const;
dcl|num=2|since=c++11|until=c++20|1=
bool operator!=( const regex_iterator& rhs ) const;
```

Compares two `regex_iterator`s.
rrev|since=c++20|

## Parameters


### Parameters

- `rhs` - a `regex_iterator` to compare to

## Return value

For the sake of exposition, assume that `regex_iterator` contains the following members:
* `BidirIt begin`;
* `BidirIt end`;
* `const regex_type *pregex;`
* `std::regex_constants::match_flag_type flags;`
* `std::match_results<BidirIt> match;`
1. Returns `true` if `*this` and `rhs` are both end-of-sequence iterators, or if all of the following conditions are true:
* `begin
* `end
* `pregex
* `flags
* `match[0]
2. Returns `!(*this .

## Example


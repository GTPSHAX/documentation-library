---
title: std::is_neq
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/compare/named_comparison_functions
---


```cpp
dcl |num=1|since=c++20|
constexpr bool is_eq( std::partial_ordering cmp ) noexcept;
dcl |num=2|since=c++20|
constexpr bool is_neq( std::partial_ordering cmp ) noexcept;
dcl |num=3|since=c++20|
constexpr bool is_lt( std::partial_ordering cmp ) noexcept;
dcl |num=4|since=c++20|
constexpr bool is_lteq( std::partial_ordering cmp ) noexcept;
dcl |num=5|since=c++20|
constexpr bool is_gt( std::partial_ordering cmp ) noexcept;
dcl |num=6|since=c++20|
constexpr bool is_gteq( std::partial_ordering cmp ) noexcept;
```

These functions take a result of 3-way comparison and convert it to the result of one of the six relational operators
Specifically, these functions return
1. `1=cmp == 0`
2. `1=cmp != 0`
3. `1=cmp < 0`
4. `1=cmp <= 0`
5. `1=cmp > 0`
6. `1=cmp >= 0`

## Parameters


### Parameters


## Return value

`bool` result of the corresponding relational operation

## Example


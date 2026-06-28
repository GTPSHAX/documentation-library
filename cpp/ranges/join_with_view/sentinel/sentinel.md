---
title: std::ranges::join_with_view::sentinel<Const>::sentinel
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_with_view/sentinel/sentinel
---


```cpp
dcl|num=1|since=c++23|1=
/*sentinel*/() = default;
dcl|num=2|since=c++23|
constexpr /*sentinel*/( /*sentinel*/<!Const> i )
requires Const && std::convertible_to<ranges::sentinel_t<V>,
ranges::sentinel_t<const V>>;
dcla|num=3|since=c++23|expos=yes|
constexpr explicit /*sentinel*/ ( /*Parent*/& parent );
```

Constructs a sentinel. Overload  is called by  of `ranges::join_with_view`.


| Overload |
| style="font-weight: normal;" | rlpi | /#Data members | end_ |
| - |
| v | 1 |
| [[cpp/language/value initialization | value-initialized]] |
| - |
| v | 2 |
| initialized with box | c/core | std::move(s.rlpi | /#Data members | end_c/core | ) |
| - |
| v | 3 |
| initialized with box | c/core | ranges::end(parent.lti | cpp/ranges/join_with_view#Data members | base_c/core | ) |


## Parameters


### Parameters

- `i` - a sentinel corresponding to a mutable iterator
- `parent` - a `std::ranges::join_with_view` object

## Example


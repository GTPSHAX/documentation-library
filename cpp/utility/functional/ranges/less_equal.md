---
title: std::ranges::less_equal
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/ranges/less_equal
---


```cpp
**Header:** `<`functional`>`
dcl|since=c++20|
struct less_equal;
```

Function object for performing comparisons. Deduces the parameter types of the function call operator from the arguments (but not the return type).

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions

member|1=operator()|2=
ddcl|
template< class T, class U >
constexpr bool operator()( T&& t, U&& u ) const;
Equivalent to }.
.

## Notes

Unlike `std::less_equal`, `std::ranges::less_equal` requires all six comparison operators `<`, `1=<=`, `>`, `1=>=`, `1===` and `1=!=` to be valid (via the  constraint) and is entirely defined in terms of
`std::ranges::less`.

## Example


## See also


| cpp/utility/functional/dsc less_equal | (see dedicated page) |


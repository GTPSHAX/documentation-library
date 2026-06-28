---
title: std::ranges::not_equal_to
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/ranges/not_equal_to
---


```cpp
**Header:** `<`functional`>`
dcl|since=c++20|
struct not_equal_to;
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

Unlike `std::not_equal_to`, `std::ranges::not_equal_to` requires both `1===` and `1=!=` to be valid (via the  constraint), and is entirely defined in terms of `std::ranges::equal_to`.

## Example


## See also


| cpp/utility/functional/dsc not_equal_to | (see dedicated page) |


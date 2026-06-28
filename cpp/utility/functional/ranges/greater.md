---
title: std::ranges::greater
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/ranges/greater
---


```cpp
**Header:** `<`functional`>`
dcl|since=c++20|
struct greater;
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

Unlike `std::greater`, `std::ranges::greater` requires all six comparison operators `<`, `1=<=`, `>`, `1=>=`, `1===` and `1=!=` to be valid (via the   constraint) and is entirely defined in terms of
`std::ranges::less`.

## Example


## See also


| cpp/utility/functional/dsc greater | (see dedicated page) |


---
title: std::unexpect_t
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/expected/unexpect_t
---


```cpp
**Header:** `<`expected`>`
dcl|num=1|since=c++23|1=
struct unexpect_t { explicit unexpect_t() = default; };
dcl|num=2|since=c++23|1=
inline constexpr std::unexpect_t unexpect{};
```

1. A tag type for in-place construction of an unexpected value in an `std::expected` object.
2. A constant of type `const std::unexpect_t` which is usually directly passed to a constructor of `std::expected` to construct an unexpected value.

## Notes

Like other construction tag types, `unexpect_t` is a trivial, empty class with an explicit default constructor.

## See also


| cpp/utility/expected/dsc constructor | (see dedicated page) |
| cpp/utility/dsc in_place | (see dedicated page) |


---
title: std::nostopstate
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_source/nostopstate
---


```cpp
**Header:** `<`stop_token`>`
dcl|num=1|since=c++20|1=
struct nostopstate_t { explicit nostopstate_t() = default; };
dcl|num=2|since=c++20|1=
inline constexpr std::nostopstate_t nostopstate {};
```

1. Empty tag type intended for use as a placeholder in `std::stop_source` non-default constructor, that makes the constructed `std::stop_source` empty with no associated stop-state.
2. The corresponding constant object instance of `std::nostopstate_t` for use in constructing an empty `std::stop_source`, as a placeholder value in the non-default constructor.

## See also


| cpp/thread/dsc stop_source | (see dedicated page) |


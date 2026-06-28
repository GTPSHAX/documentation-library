---
title: std::from_range_t
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/from_range
---


```cpp
**Header:** `<`ranges`>`
dcl|since=c++23|1=
struct from_range_t { explicit from_range_t() = default; };
dcl|since=c++23|
inline constexpr std::from_range_t from_range {};
```

`std::from_range` is a disambiguation tag that can be passed to the constructors of the suitable containers to indicate that the contained member is range constructed.
The corresponding type `std::from_range_t` can be used in the constructor's parameter list to match the intended tag.

## Standard library

The following standard library types use `std::from_range_t` type in their constructors:


#### Containers library


#### Strings library


## Notes


## Example


### Example

```cpp
#include <cassert>
#include <string>

int main()
{
#ifdef __cpp_lib_containers_ranges
    auto const range = {0x43, 43, 43};
    std::string str{std::from_range, range}; // uses tagged constructor
    assert(str == "C++");
#endif
}
```


## See also


| cpp/utility/dsc in_place | (see dedicated page) |
| cpp/container/dsc sorted_equivalent | (see dedicated page) |
| cpp/container/dsc sorted_unique | (see dedicated page) |
| cpp/ranges/dsc to | (see dedicated page) |


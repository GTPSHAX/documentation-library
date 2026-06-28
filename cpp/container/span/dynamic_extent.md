---
title: std::dynamic_extent
type: Containers
source: https://en.cppreference.com/w/cpp/container/span/dynamic_extent
---


```cpp
**Header:** `<`span`>`
dcl|since=c++20|1=
inline constexpr std::size_t dynamic_extent = std::numeric_limits<std::size_t>::max();
```

`std::dynamic_extent` is a constant of type `std::size_t` that is generally used to indicate that any type using `std::dynamic_extent` will ''dynamically'' store its value (e.g., size) rather than having the value ''statically'' known in the type.
It is being used in several contexts:
* To differentiate `cpp/container/span|std::span` of static and dynamic extent.
rrev|since=c++23|1=
* To indicate that the extent at a certain rank index will be stored dynamically in `cpp/container/mdspan/extents|std::extents`.
rrev|since=c++26|1=
* To indicate that the padded layouts for `cpp/container/mdspan|std::mdspan` will dynamically store its padding value.

## Note

Since `std::size_t` is an unsigned type, an equivalent definition is:

```cpp
inline constexpr std::size_t dynamic_extent = -1;
```

See integral conversions.

## Example


### Example

```cpp
#include <array>
#include <cassert>
#include <cstddef>
#include <iostream>
#include <span>
#include <string_view>
#include <vector>

int main()
{
    auto print = [](std::string_view const name, std::size_t ex)
    {
        std::cout << name << ", ";
        if (std::dynamic_extent == ex)
            std::cout << "dynamic extent\n";
        else
            std::cout << "static extent = " << ex << '\n';
    };

    int a[]{1, 2, 3, 4, 5};

    std::span span1{a};
    print("span1", span1.extent);

    std::span<int, std::dynamic_extent> span2{a};
    print("span2", span2.extent);

    std::array ar{1, 2, 3, 4, 5};
    std::span span3{ar};
    print("span3", span3.extent);

    std::vector v{1, 2, 3, 4, 5};
    std::span span4{v};
    print("span4", span4.extent);
}
```


**Output:**
```
span1, static extent = 5
span2, dynamic extent
span3, static extent = 5
span4, dynamic extent
```


## See also


| cpp/container/dsc span | (see dedicated page) |
| cpp/container/mdspan/dsc extents | (see dedicated page) |


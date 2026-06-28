---
title: std::ranges::split_view::base
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/split_view/base
---


```cpp
dcl|num=1|since=c++20|
constexpr V base() const& requires std::copy_constructible<V>;
dcl|num=2|since=c++20|
constexpr V base() &&;
```

Returns a copy of the underlying view .
1. Copy constructs the result from the underlying view.
2. Move constructs the result from the underlying view.

## Return value

1. A copy of the underlying view.
2. A view move-constructed from the underlying view.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <ranges>
#include <string_view>

int main()
{
    constexpr std::string_view keywords{"this throw true try typedef typeid"};
    std::ranges::split_view split_view{keywords, ' '};
    std::cout << "base() = " << std::quoted(split_view.base()) << "\n"
                 "substrings: ";
    for (auto split : split_view)
        std::cout << std::quoted(std::string_view{split}) << ' ';
    std::cout << '\n';
}
```


**Output:**
```
base() = "this throw true try typedef typeid"
substrings: "this" "throw" "true" "try" "typedef" "typeid"
```


## Defect reports


## See also


| cpp/ranges/adaptor/dsc base|lazy_split_view | (see dedicated page) |


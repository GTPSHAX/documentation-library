---
title: std::ranges::lazy_split_view::base
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/lazy_split_view/base
---


```cpp
dcl|num=1|since=c++20|1=
constexpr V base() const& requires std::copy_constructible<V>;
dcl|num=2|since=c++20|1=
constexpr V base() &&;
```

Returns a copy of the underlying view .
1. Copy constructs the result from the underlying view .
2. Move constructs the result from the underlying view .

## Return value

A copy of the underlying view .

## Example


### Example

```cpp
#include <iostream>
#include <ranges>
#include <string_view>

void print(std::string_view rem, auto const& r, std::string_view post = "\n")
{
    for (std::cout << rem; auto const& e : r)
        std::cout << e;
    std::cout << post;
}

int main()
{
    constexpr std::string_view keywords{ "this,..throw,..true,..try,.." };
    constexpr std::string_view pattern{",.."};
    constexpr std::ranges::lazy_split_view lazy_split_view{keywords, pattern};
    print("base() = [", lazy_split_view.base(), "]\n"
          "substrings: ");
    for (auto const& split: lazy_split_view)
        print("[", split, "] ");
}
```


**Output:**
```
base() = [this,..throw,..true,..try,..]
substrings: [this] [throw] [true] [try] []
```


## See also


| cpp/ranges/adaptor/dsc base|split_view | (see dedicated page) |


---
title: std::ranges::transform_view::size
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/transform_view/size
---


```cpp
dcl|num=1|since=c++20|
constexpr auto size() requires ranges::sized_range<V>;
dcl|num=2|since=c++20|
constexpr auto size() const requires ranges::sized_range<const V>;
```

Returns the number of elements. Equivalent to .

## Return value

The number of elements.

## Notes

If `V` does not model , `size()` might not be well-defined after a call to .

## Example


### Example

```cpp
#include <cassert>
#include <cctype>
#include <iostream>
#include <ranges>
#include <string>

int main()
{
    std::string s{"The length of this string is 42 characters"};
    auto to_upper{[](unsigned char c) -> char { return std::toupper(c); }<!---->};
    auto tv{std::ranges::transform_view{s, to_upper}<!---->};
    for (assert(tv.size() == 42); const auto c : tv)
        std::cout << c;
}
```


**Output:**
```
THE LENGTH OF THIS STRING IS 42 CHARACTERS
```


## See also


| cpp/ranges/dsc size | (see dedicated page) |
| cpp/ranges/dsc ssize | (see dedicated page) |


---
title: std::basic_string_view::max_size
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/max_size
---

ddcl|since=c++17|
constexpr size_type max_size() const noexcept;
The largest possible number of char-like objects that can be referred to by a `basic_string_view`.

## Parameters

(none)

## Return value

Maximum number of characters.

## Complexity

Constant.

## Example


### Example

```cpp
#include <cstdint>
#include <iostream>
#include <limits>
#include <string_view>

int main()
{
    std::cout << std::numeric_limits<std::int64_t>::max()
              << " <- numeric_limits<int64_t>::max()\n"
              << std::string_view{}.max_size()
              << " <- string_view::max_size()\n"
              << std::basic_string_view<char>{}.max_size()
              << " <- basic_string_view<char>::max_size()\n"
              << std::basic_string_view<char16_t>{}.max_size()
              << " <- basic_string_view<char16_t>::max_size()\n"
              << std::wstring_view{}.max_size()
              << " <- wstring_view::max_size()\n"
              << std::basic_string_view<char32_t>{}.max_size()
              << " <- basic_string_view<char32_t>::max_size()\n";
}
```


**Output:**
```
9223372036854775807 <- numeric_limits<int64_t>::max()
4611686018427387899 <- string_view::max_size()
4611686018427387899 <- basic_string_view<char>::max_size()
2305843009213693949 <- basic_string_view<char16_t>::max_size()
1152921504606846974 <- wstring_view::max_size()
1152921504606846974 <- basic_string_view<char32_t>::max_size()
```


## See also


| cpp/string/basic_string_view/dsc size | (see dedicated page) |
| cpp/string/basic_string_view/dsc empty | (see dedicated page) |
| cpp/string/basic_string/dsc max_size | (see dedicated page) |


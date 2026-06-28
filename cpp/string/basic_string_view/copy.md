---
title: std::basic_string_view::copy
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/copy
---

ddcl|since=c++17|notes=<sup>(constexpr C++20)</sup>|1=
size_type copy( CharT* dest, size_type count, size_type pos = 0 ) const;
Copies the substring [pos, pos + rcount) to the character array pointed to by `dest`, where `rcount` is the smaller of `count` and `size() - pos`.
Equivalent to `Traits::copy(dest, data() + pos, rcount)`.

## Parameters


### Parameters

- `dest` - pointer to the destination character string
- `count` - requested substring length
- `pos` - position of the first character

## Return value

Number of characters copied.

## Exceptions

`std::out_of_range` if `1=pos > size()`.

## Complexity

Linear in `rcount`.

## Example


### Example

```cpp
#include <array>
#include <cstddef>
#include <iostream>
#include <stdexcept>
#include <string_view>

int main()
{
    constexpr std::basic_string_view<char> source{"ABCDEF"};
    std::array<char, 8> dest;
    std::size_t count{}, pos{};

    dest.fill('\0');
    source.copy(dest.data(), count = 4); // pos = 0
    std::cout << dest.data() << '\n'; // ABCD

    dest.fill('\0');
    source.copy(dest.data(), count = 4, pos = 1);
    std::cout << dest.data() << '\n'; // BCDE

    dest.fill('\0');
    source.copy(dest.data(), count = 42, pos = 2); // ok, count -> 4
    std::cout << dest.data() << '\n'; // CDEF

    try
    {
        source.copy(dest.data(), count = 1, pos = 666); // throws: pos > size()
    }
    catch (std::out_of_range const& ex)
    {
        std::cout << ex.what() << '\n';
    }
}
```


**Output:**
```
ABCD
BCDE
CDEF
basic_string_view::copy: __pos (which is 666) > __size (which is 6)
```


## See also


| cpp/string/basic_string_view/dsc substr | (see dedicated page) |
| cpp/string/basic_string/dsc copy | (see dedicated page) |
| cpp/algorithm/dsc copy | (see dedicated page) |
| cpp/string/byte/dsc memcpy | (see dedicated page) |


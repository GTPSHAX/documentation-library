---
title: std::basic_string::length
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/size
---


```cpp
<br><sup>(constexpr C++20)</sup>|
size_type size() const;
<br><sup>(constexpr C++20)</sup>|
size_type length() const;
```

Returns the number of `CharT` elements in the string, i.e. `std::distance(begin(), end())`.

## Parameters

(none)

## Return value

The number of `CharT` elements in the string.

## Complexity

rrev multi|until1=c++11
|rev1=Unspecified
|rev2=Constant

## Notes

For `std::string`, the elements are bytes (objects of type `char`), which are not the same as characters if a multibyte encoding such as UTF-8 is used.

## Example


### Example

```cpp
#include <cassert>
#include <iterator>
#include <string>

int main()
{
    std::string s("Exemplar");
    assert(8 == s.size());
    assert(s.size() == s.length());
    assert(s.size() == static_cast<std::string::size_type>(
        std::distance(s.begin(), s.end())));

    std::u32string a(U"ハロー・ワールド"); // 8 code points
    assert(8 == a.size()); // 8 code units in UTF-32

    std::u16string b(u"ハロー・ワールド"); // 8 code points
    assert(8 == b.size()); // 8 code units in UTF-16

    std::string c("ハロー・ワールド"); // 8 code points
    assert(24 == c.size()); // 24 code units in UTF-8

    #if __cpp_lib_char8_t >= 201907L
    std::u8string d(u8"ハロー・ワールド"); // 8 code points
    assert(24 == d.size()); // 24 code units in UTF-8
    #endif
}
```


## See also


| cpp/string/basic_string/dsc empty | (see dedicated page) |
| cpp/string/basic_string/dsc max_size | (see dedicated page) |
| cpp/string/basic_string_view/dsc size | (see dedicated page) |


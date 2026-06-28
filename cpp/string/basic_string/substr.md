---
title: std::basic_string::substr
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/substr
---


```cpp
dcl rev multi|num=1|until1=c++23|notes1=<sup>(constexpr C++20)</sup>|dcl1=
basic_string substr( size_type pos = 0, size_type count = npos ) const;
|dcl2=
constexpr basic_string
substr( size_type pos = 0, size_type count = npos ) const&;
dcl|num=2|since=c++23|1=
constexpr basic_string substr( size_type pos = 0, size_type count = npos ) &&;
```

Returns a substring [pos, pos + count). If the requested substring extends past the end of the string, i.e. the `count` is greater than `size() - pos` (e.g. if `1=count == npos`), the returned substring is .
1. Equivalent to `return basic_string(*this, pos, count);`.
2. Equivalent to `return basic_string(std::move(*this), pos, count);`.

## Parameters


### Parameters

- `pos` - position of the first character to include
- `count` - length of the substring

## Return value

String containing the substring [pos, pos + count) or .

## Exceptions

`std::out_of_range` if `pos > size()`.

## Complexity

Linear in `count`.

## Notes

The allocator of the returned string is default-constructed: the new allocator might ''not'' be a copy of .

## Example


### Example

```cpp
#include <iostream>
#include <string>

int main()
{
    std::string a = "0123456789abcdefghij";

    // count is npos, returns [pos, size())
    std::string sub1 = a.substr(10);
    std::cout << sub1 << '\n';

    // both pos and pos + count are within bounds, returns [pos, pos + count)
    std::string sub2 = a.substr(5, 3);
    std::cout << sub2 << '\n';

    // pos is within bounds, pos + count is not, returns [pos, size())
    std::string sub4 = a.substr(a.size() - 3, 50);
    // this is effectively equivalent to
    // std::string sub4 = a.substr(17, 3);
    // since a.size() == 20, pos == a.size() - 3 == 17, and a.size() - pos == 3

    std::cout << sub4 << '\n';

    try
    {
        // pos is out of bounds, throws
        std::string sub5 = a.substr(a.size() + 3, 50);
        std::cout << sub5 << '\n';
    }
    catch (const std::out_of_range& ex)
    {
        std::cout << ex.what() << '\n';
    }
}
```


**Output:**
```
abcdefghij
567
hij
basic_string::substr: __pos (which is 23) > this->size() (which is 20)
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-847 | C++98 | there was no exception safety guarantee | added strong exception safety guarantee |


## See also


| cpp/string/basic_string/dsc npos | (see dedicated page) |
| cpp/string/basic_string/dsc subview | (see dedicated page) |
| cpp/string/basic_string/dsc copy | (see dedicated page) |
| cpp/string/basic_string/dsc size | (see dedicated page) |
| cpp/string/basic_string/dsc find | (see dedicated page) |
| cpp/string/basic_string_view/dsc {{SUBPAGENAMEE | (see dedicated page) |


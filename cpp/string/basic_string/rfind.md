---
title: std::basic_string::rfind
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/rfind
---


```cpp
dcla|anchor=no|num=1|noexcept=c++11|constexpr=c++20|1=
size_type rfind( const basic_string& str, size_type pos = npos ) const;
dcla|anchor=no|num=2|constexpr=c++20|1=
size_type rfind( const CharT* s, size_type pos, size_type count ) const;
dcla|anchor=no|num=3|constexpr=c++20|1=
size_type rfind( const CharT* s, size_type pos = npos ) const;
dcla|anchor=no|num=4|noexcept=c++11|constexpr=c++20|1=
size_type rfind( CharT ch, size_type pos = npos ) const;
dcla|anchor=no|num=5|since=c++17|constexpr=c++20|1=
template< class StringViewLike >
size_type rfind( const StringViewLike& t,
size_type pos = npos ) const noexcept(/* see below */);
```

Finds the last substring that is equal to the given character sequence. The search begins at `pos` and proceeds from right to left (thus, the found substring, if any, cannot begin in a position following `pos`). If `npos` or any value not smaller than  is passed as `pos`, the whole string will be searched.
1. Finds the last substring equal to `str`.
2. Finds the last substring equal to the range [s, s + count). This range can include null characters.
@@ If [s, s + count) is not a valid range, the behavior is undefined.
3. Finds the last substring equal to the character string pointed to by `s`. The length of the string is determined by the first null character using `Traits::length(s)`.
@@ If [s, s + Traits::length(s)) is not a valid range, the behavior is undefined.
4. Finds the last character equal to `ch`.
5.
In all cases, equality is checked by calling `cpp/string/char_traits/cmp|Traits::eq`.

## Parameters


### Parameters

- `str` - string to search for
- `pos` - position at which to begin searching
- `count` - length of substring to search for
- `s` - pointer to a character string to search for
- `ch` - character to search for
- `t` - object (convertible to `std::basic_string_view`) to search for

## Return value

Position of the first character of the found substring or `npos` if no such substring is found. Note that this is an offset from the start of the string, not the end.
If searching for an empty string (i.e., `str.size()`, `count`, or `Traits::length(s)` is zero), the empty string is found immediately and `rfind` returns:
* `pos`, if `pos < size()`;
* `size()` otherwise, including the case where `1=pos == npos`.
Otherwise, if `size()` is zero, `npos` is always returned.

## Exceptions

@1,4@ Throws nothing.
5.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <string>

void print(std::string::size_type n,
           std::string::size_type len,
           std::string const &s)
{
    if (n == std::string::npos)
        std::cout << "not found\n";
    else
        std::cout << "found: " << std::quoted(s.substr(n, len)) << " at " << n << '\n';
}

int main()
{
    std::string::size_type n;
    std::string const s = "This is a string";

    // search backwards from end of string
    n = s.rfind("is");
    print(n, 2, s);

    // search backwards from position 4
    n = s.rfind("is", 4);
    print(n, 2, s);

    // find a single character
    n = s.rfind('s');
    print(n, 1, s);

    // find a single character
    n = s.rfind('q');
    print(n, 1, s);

    // find the prefix (see also s.starts_with("This"))
    n = s.rfind("This", 0);
    print(n, 4, s);
}
```


**Output:**
```
found: "is" at 5
found: "is" at 2
found: "s" at 10
not found
found: "This" at 0
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-847 | C++98 | there was no exception safety guarantee | added strong exception safety guarantee |


## See also


| cpp/string/basic_string/dsc find | (see dedicated page) |
| cpp/string/basic_string/dsc find_first_of | (see dedicated page) |
| cpp/string/basic_string/dsc find_first_not_of | (see dedicated page) |
| cpp/string/basic_string/dsc find_last_of | (see dedicated page) |
| cpp/string/basic_string/dsc find_last_not_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc rfind | (see dedicated page) |


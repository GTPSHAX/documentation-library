---
title: std::basic_string::find_last_of
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/find_last_of
---


```cpp
dcla|anchor=no|num=1|noexcept=c++11|constexpr=c++20|1=
size_type find_last_of( const basic_string& str,
size_type pos = npos ) const;
dcla|anchor=no|num=2|constexpr=c++20|1=
size_type find_last_of( const CharT* s,
size_type pos, size_type count ) const;
dcla|anchor=no|num=3|constexpr=c++20|1=
size_type find_last_of( const CharT* s, size_type pos = npos ) const;
dcla|anchor=no|num=4|noexcept=c++11|constexpr=c++20|1=
size_type find_last_of( CharT ch, size_type pos = npos ) const;
dcla|anchor=no|num=5|since=c++17|constexpr=c++20|1=
template< class StringViewLike >
size_type
find_last_of( const StringViewLike& t,
size_type pos = npos ) const noexcept(/* see below */);
```

Finds the last character equal to one of characters in the given character sequence. The exact search algorithm is not specified. The search considers only the range . If none of the characters in the given character sequence is present in the range, `npos` will be returned.
1. Finds the last character equal to one of characters in `str`.
2. Finds the last character equal to one of characters in range [s, s + count). This range can include null characters.
@@ If [s, s + count) is not a valid range, the behavior is undefined.
3. Finds the last character equal to one of characters in character string pointed to by `s`. The length of the string is determined by the first null character using `Traits::length(s)`.
@@ If [s, s + Traits::length(s)) is not a valid range, the behavior is undefined.
4. Finds the last character equal to `ch`.
5.
In all cases, equality is checked by calling .

## Parameters


### Parameters

- `str` - string identifying characters to search for
- `pos` - position at which the search is to finish
- `count` - length of character string identifying characters to search for
- `s` - pointer to a character string identifying characters to search for
- `ch` - character to search for
- `t` - object (convertible to `std::basic_string_view`) identifying characters to search for

## Return value

Position of the found character or `npos` if no such character is found.

## Exceptions

@1,4@ Throws nothing.
5.

## Example


### Example

```cpp
#include <iostream>
#include <string>

int main()
{
    const std::string path = "/root/config";
    auto const pos = path.find_last_of('/');
    const auto leaf = path.substr(pos + 1);

    std::cout << leaf << '\n';
}
```


**Output:**
```
config
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-847 | C++98 | there was no exception safety guarantee | added strong exception safety guarantee |


## See also


| cpp/string/basic_string/dsc find | (see dedicated page) |
| cpp/string/basic_string/dsc rfind | (see dedicated page) |
| cpp/string/basic_string/dsc find_first_of | (see dedicated page) |
| cpp/string/basic_string/dsc find_first_not_of | (see dedicated page) |
| cpp/string/basic_string/dsc find_last_not_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_last_of | (see dedicated page) |


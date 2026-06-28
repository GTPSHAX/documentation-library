---
title: std::basic_string::find_last_not_of
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/find_last_not_of
---


```cpp
dcla|anchor=no|num=1|noexcept=c++11|constexpr=c++20|1=
size_type find_last_not_of( const basic_string& str,
size_type pos = npos ) const;
dcla|anchor=no|num=2|constexpr=c++20|1=
size_type find_last_not_of( const CharT* s,
size_type pos, size_type count ) const;
dcla|anchor=no|num=3|constexpr=c++20|1=
size_type find_last_not_of( const CharT* s, size_type pos = npos ) const;
dcla|anchor=no|num=4|noexcept=c++11|constexpr=c++20|1=
size_type find_last_not_of( CharT ch, size_type pos = npos ) const;
dcla|anchor=no|num=5|since=c++17|constexpr=c++20|1=
template< class StringViewLike >
size_type
find_last_not_of( const StringViewLike& t,
size_type pos = npos ) const noexcept(/* see below */);
```

Finds the last character equal to none of the characters in the given character sequence. The search considers only the range . If all characters in the range can be found in the given character sequence, `npos` will be returned.
1. Finds the last character equal to none of characters in `str`.
2. Finds the last character equal to none of characters in the range [s, s + count). This range can include null characters.
@@ If [s, s + count) is not a valid range, the behavior is undefined.
3. Finds the last character equal to none of characters in character string pointed to by `s`. The length of the string is determined by the first null character using `Traits::length(s)`.
@@ If [s, s + Traits::length(s)) is not a valid range, the behavior is undefined.
4. Finds the last character not equal to `ch`.
5.
In all cases, equality is checked by calling .

## Parameters


### Parameters

- `str` - string identifying characters to search for
- `pos` - position at which to end search
- `count` - length of character string identifying characters to search for
- `s` - pointer to a character string identifying characters to search for
- `ch` - character identifying characters to search for
- `t` - object (convertible to `std::basic_string_view`) identifying characters to search for

## Return value

Position of the found character or `npos` if no such character is found.

## Exceptions

@1,4@ Throws nothing.
5. noexcept|std::is_nothrow_convertible_v<
const T&, std::basic_string_view<CharT, Traits>>

## Example


### Example

```cpp
#include <iostream>
#include <string>

void show_pos(const std::string& str, std::string::size_type found)
{
    if (found != std::string::npos)
        std::cout << '[' << found << "] = \'" << str[found] << "\'\n";
    else
        std::cout << "not found\n";
}

int main()
{
    std::string str{"abc_123"};
    char const* skip_set{"0123456789"};
    std::string::size_type str_last_pos{std::string::npos};

    show_pos(str, str.find_last_not_of(skip_set)); // [3] = '_'

    str_last_pos = 2;
    show_pos(str, str.find_last_not_of(skip_set, str_last_pos)); // [2] = 'c'

    str_last_pos = 2;
    show_pos(str, str.find_last_not_of('c', str_last_pos)); // [1] = 'b'

    const char arr[]{'3', '4', '5'};
    show_pos(str, str.find_last_not_of(arr)); // [5] = '2'

    str_last_pos = 2;
    std::string::size_type skip_set_size{4};
    show_pos(str, str.find_last_not_of(skip_set,
                                       str_last_pos,
                                       skip_set_size)); // [2] = 'c'

    show_pos(str, str.find_last_not_of("abc")); // [6] = '3'

    str_last_pos = 2;
    show_pos(str, str.find_last_not_of("abc", str_last_pos)); // not found
}
```


**Output:**
```
[3] = '_'
[2] = 'c'
[1] = 'b'
[5] = '2'
[2] = 'c'
[6] = '3'
not found
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
| cpp/string/basic_string/dsc find_last_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc {{SUBPAGENAMEE | (see dedicated page) |


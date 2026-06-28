---
title: std::basic_string::find_first_not_of
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/find_first_not_of
---


```cpp
dcla|anchor=no|num=1|noexcept=c++11|constexpr=c++20|1=
size_type find_first_not_of( const basic_string& str,
size_type pos = 0 ) const;
dcla|anchor=no|num=2|constexpr=c++20|1=
size_type find_first_not_of( const CharT* s,
size_type pos, size_type count ) const;
dcla|anchor=no|num=3|constexpr=c++20|1=
size_type find_first_not_of( const CharT* s,
size_type pos = 0 ) const;
dcla|anchor=no|num=4|noexcept=c++11|constexpr=c++20|1=
size_type find_first_not_of( CharT ch, size_type pos = 0 ) const;
dcla|anchor=no|num=5|since=c++17|constexpr=c++20|1=
template< class StringViewLike >
size_type
find_first_not_of( const StringViewLike& t,
size_type pos = 0 ) const noexcept(/* see below */);
```

Finds the first character equal to none of the characters in the given character sequence. The search considers only the range . If all characters in the range can be found in the given character sequence, `npos` will be returned.
1. Finds the first character equal to none of characters in `str`.
2. Finds the first character equal to none of characters in range [s, s + count). This range can include null characters.
@@ If [s, s + count) is not a valid range, the behavior is undefined.
3. Finds the first character equal to none of characters in character string pointed to by `s`. The length of the string is determined by the first null character using `Traits::length(s)`.
@@ If [s, s + Traits::length(s)) is not a valid range, the behavior is undefined.
4. Finds the first character not equal to `ch`.
5.
In all cases, equality is checked by calling `cpp/string/char_traits/cmp|Traits::eq`.

## Parameters


### Parameters

- `str` - string identifying characters to search for
- `pos` - position for the search to start from
- `count` - length of character string identifying characters to search for
- `s` - pointer to a character string identifying characters to search for
- `ch` - character identifying characters to search for
- `t` - object (convertible to `std::basic_string_view`) identifying characters to search for

## Return value

Position of the found character or `std::string::npos` if no such character is found.

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
    // Permit uppercase letters, lowercase letters and numbers in macro names
    const char* pattern = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                          "abcdefghijklmnopqrstuvwxyz"
                          "0123456789";

    std::string data = "1) %FIX, 2) %HACK, and 3) %TODO";
    const std::string replacement = "%DONE%";

    std::cout << "Before: " << data << '\n';

    for (std::string::size_type first{}, last{};
        (first = data.find('%', first)) != std::string::npos;
        first += replacement.size())
    {
        last = data.find_first_not_of(pattern, first + 1);
        if (last == std::string::npos)
            last = data.length();

        // Now first at '%' and last is one past end of the found substring
        data.replace(first, last - first, replacement);
    }

    std::cout << "After: " << data << '\n';
}
```


**Output:**
```
Before: 1) %FIX, 2) %HACK, and 3) %TODO
After: 1) %DONE%, 2) %DONE%, and 3) %DONE%
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
| cpp/string/basic_string/dsc find_last_of | (see dedicated page) |
| cpp/string/basic_string/dsc find_last_not_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_first_not_of | (see dedicated page) |


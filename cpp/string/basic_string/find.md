---
title: std::basic_string::find
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/find
---


```cpp
dcla|anchor=no|num=1|noexcept=c++11|constexpr=c++20|1=
size_type find( const basic_string& str, size_type pos = 0 ) const;
dcla|anchor=no|num=2|constexpr=c++20|1=
size_type find( const CharT* s, size_type pos, size_type count ) const;
dcla|anchor=no|num=3|constexpr=c++20|1=
size_type find( const CharT* s, size_type pos = 0 ) const;
dcla|anchor=no|num=4|noexcept=c++11|constexpr=c++20|1=
size_type find( CharT ch, size_type pos = 0 ) const;
dcla|anchor=no|num=5|since=c++17|constexpr=c++20|1=
template< class StringViewLike >
size_type find( const StringViewLike& t,
size_type pos = 0 ) const noexcept(/* see below */);
```

Finds the first substring equal to the given character sequence. Search begins at `pos`, i.e. the found substring must not begin in a position preceding `pos`.
1. Finds the first substring equal to `str`.
2. Finds the first substring equal to the range [s, s + count). This range may contain null characters.
@@ If [s, s + count) is not a valid range, the behavior is undefined.
3. Finds the first substring equal to the character string pointed to by `s`. The length of the string is determined by the first null character using `Traits::length(s)`.
@@ If [s, s + Traits::length(s)) is not a valid range, the behavior is undefined.
4. Finds the first character `ch` (treated as a single-character substring by the formal rules below).
5.
Formally, a substring `str` is said to be ''found'' at position `xpos` if all of the following are `true`:
* `1=xpos >= pos`
* `1=xpos + str.size() <= size()`
* for all positions `n` in `str`, `Traits::eq(at(xpos + n), str.at(n))`.
In particular, this implies that
* a substring can be found only if `1=pos <= size() - str.size()`
* an empty substring is found at `pos` if and only if `1=pos <= size()`
* for a non-empty substring, if `1=pos >= size()`, the function always returns `npos`.

## Parameters


### Parameters

- `str` - string to search for
- `pos` - position at which to start the search
- `count` - length of substring to search for
- `s` - pointer to a character string to search for
- `ch` - character to search for
- `t` - object (convertible to `std::basic_string_view`) to search for

## Return value

Position of the first character of the found substring or `npos` if no such substring is found.

## Exceptions

@1,4@ Throws nothing.
5.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <string>

void print(int id, std::string::size_type n, std::string const& s)
{
    std::cout << id << ") ";
    if (std::string::npos == n)
        std::cout << "not found! n == npos\n";
    else
        std::cout << "found @ n = " << n << ", substr(" << n << ") = "
                  << std::quoted(s.substr(n)) << '\n';
}

int main()
{
    std::string::size_type n;
    std::string const s = "This is a string"; /*
                             ^  ^  ^
                             1  2  3          */

    // search from beginning of string
    n = s.find("is");
    print(1, n, s);

    // search from position 5
    n = s.find("is", 5);
    print(2, n, s);

    // find a single character
    n = s.find('a');
    print(3, n, s);

    // find a single character
    n = s.find('q');
    print(4, n, s);
}
```


**Output:**
```
1) found @ n = 2, substr(2) = "is is a string"
2) found @ n = 5, substr(5) = "is a string"
3) found @ n = 8, substr(8) = "a string"
4) not found! n == npos
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-847 | C++98 | there was no exception safety guarantee | added strong exception safety guarantee |


## See also


| cpp/string/byte/dsc strstr | (see dedicated page) |
| cpp/string/wide/dsc wcsstr | (see dedicated page) |
| cpp/string/byte/dsc strchr | (see dedicated page) |
| cpp/string/wide/dsc wcschr | (see dedicated page) |
| cpp/string/basic_string/dsc rfind | (see dedicated page) |
| cpp/string/basic_string/dsc find_first_of | (see dedicated page) |
| cpp/string/basic_string/dsc find_first_not_of | (see dedicated page) |
| cpp/string/basic_string/dsc find_last_of | (see dedicated page) |
| cpp/string/basic_string/dsc find_last_not_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find | (see dedicated page) |
| cpp/algorithm/dsc search | (see dedicated page) |


---
title: std::basic_string::find_first_of
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/find_first_of
---


```cpp
dcla|anchor=no|num=1|noexcept=c++11|constexpr=c++20|1=
size_type find_first_of( const basic_string& str, size_type pos = 0 ) const;
dcla|anchor=no|num=2|constexpr=c++20|1=
size_type find_first_of( const CharT* s,
size_type pos, size_type count ) const;
dcla|anchor=no|num=3|constexpr=c++20|1=
size_type find_first_of( const CharT* s, size_type pos = 0 ) const;
dcla|anchor=no|num=4|noexcept=c++11|constexpr=c++20|1=
size_type find_first_of( CharT ch, size_type pos = 0 ) const;
dcla|anchor=no|num=5|since=c++17|constexpr=c++20|1=
template< class StringViewLike >
size_type
find_first_of( const StringViewLike& t,
size_type pos = 0 ) const noexcept(/* see below */);
```

Finds the first character equal to one of the characters in the given character sequence. The search considers only the range . If none of the characters in the given character sequence is present in the range, `npos` will be returned.
1. Finds the first character equal to one of the characters in `str`.
2. Finds the first character equal to one of the characters in the range [s, s + count). This range can include null characters.
@@ If [s, s + count) is not a valid range, the behavior is undefined.
3. Finds the first character equal to one of the characters in character string pointed to by `s`. The length of the string is determined by the first null character using `Traits::length(s)`.
@@ If [s, s + Traits::length(s)) is not a valid range, the behavior is undefined.
4. Finds the first character equal to `ch`.
5.

## Parameters


### Parameters

- `str` - string identifying characters to search for
- `pos` - position at which to begin searching
- `count` - length of character string identifying characters to search for
- `s` - pointer to a character string identifying characters to search for
- `ch` - character to search for
- `t` - object (convertible to `std::basic_string_view`) identifying characters to search for

## Return value

Position of the found character or `npos` if no such character is found.

## Exceptions

@1,4@ Throws nothing.
5.

## Notes

`Traits::eq()` is used to perform the comparison.

## Example


### Example

```cpp
#include <cassert>
#include <iostream>
#include <string>
#include <string_view>

int main()
{
    using namespace std::literals;
    std::string::size_type sz;

    // (1)
    sz = "alignas"s.find_first_of("klmn"s);
    //     └────────────────────────┘
    assert(sz == 1);

    sz = "alignof"s.find_first_of("wxyz"s);
    // no match
    assert(sz == std::string::npos);

    // (2)
    sz = "consteval"s.find_first_of("xyzabc", 0, 3);
    // no match (× are not targets)     ×××
    assert(sz == std::string::npos);

    sz = "consteval"s.find_first_of("xyzabc", 0, 6);
    //    └───────────────────────────────┘
    assert(sz == 0);

    // (3)
    sz = "decltype"s.find_first_of("xyzabc");
    //      └────────────────────────────┘
    assert(sz == 2);

    // (4)
    sz = "co_await"s.find_first_of('a');
    //       └──────────────────────┘
    assert(sz == 3);

    // (5)
    sz = "constinit"s.find_first_of("int"sv);
    //      └─────────────────────────┘
    assert(sz == 2);

    std::cout << "All tests passed.\n";
}
```


**Output:**
```
All tests passed.
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-847 | C++98 | there was no exception safety guarantee | added strong exception safety guarantee |


## See also


| cpp/string/basic_string/dsc find | (see dedicated page) |
| cpp/string/basic_string/dsc rfind | (see dedicated page) |
| cpp/string/basic_string/dsc find_first_not_of | (see dedicated page) |
| cpp/string/basic_string/dsc find_last_of | (see dedicated page) |
| cpp/string/basic_string/dsc find_last_not_of | (see dedicated page) |
| cpp/string/basic_string_view/dsc find_first_of | (see dedicated page) |
| cpp/string/byte/dsc strspn | (see dedicated page) |


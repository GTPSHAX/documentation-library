---
title: std::char_traits
type: Strings
source: https://en.cppreference.com/w/cpp/string/char_traits
---

ddcl|header=string|1=
template<
class CharT
> class char_traits;
The `char_traits` class is a traits class template that abstracts basic character and string operations for a given character type. The defined operation set is such that generic algorithms almost always can be implemented in terms of it. It is thus possible to use such algorithms with almost any possible character or string type, just by supplying a customized `char_traits` class.
The `char_traits` class template serves as a basis for explicit instantiations. The user can provide a specialization for any custom character types. Several explicit specializations are provided for the standard character types (see below), other specializations are not required to satisfy the requirements of *CharTraits*.

## Specializations

The standard library provides the following standard specializations:


| string | |

All these specializations satisfy the requirements of *CharTraits*.

### Member types

The standard specializations define the following member types required by *CharTraits*:


| rowspan=2 | tt | CharT |
| colspan=5 | Member type |
| - |
| tt | char_type |
| tt | int_type |
| tt | off_type |
| tt | pos_type |
| tt | state_type |
| - |
| c/core | char |
| c/core | char |
| c/core | int |
| rowspan=5 | lc | std::streamoff |
| lc | std::streampos |
| rowspan=5 | lc | std::mbstate_t |
| - |
| c/core | wchar_t |
| c/core | wchar_t |
| ltt | cpp/string/wide#Types | std::wint_t |
| lc | std::wstreampos |
| - |
| c/core | char8_t |
| c/core | char8_t |
| c/core | unsigned int |
| lc | std::u8streampos |
| - |
| c/core | char16_t |
| c/core | char16_t |
| lc | std::uint_least16_t |
| lc | std::u16streampos |
| - |
| c/core | char32_t |
| c/core | char32_t |
| lc | std::uint_least32_t |
| lc | std::u32streampos |

rrev|since=c++20|
On top of that, the standard specializations also define the member type `comparison_category` as .

### Member functions

The standard specializations define the following static member functions required by *CharTraits*:


| cpp/string/char_traits/dsc assign | (see dedicated page) |
| cpp/string/char_traits/dsc cmp | (see dedicated page) |
| cpp/string/char_traits/dsc move | (see dedicated page) |
| cpp/string/char_traits/dsc copy | (see dedicated page) |
| cpp/string/char_traits/dsc compare | (see dedicated page) |
| cpp/string/char_traits/dsc length | (see dedicated page) |
| cpp/string/char_traits/dsc find | (see dedicated page) |
| cpp/string/char_traits/dsc to_char_type | (see dedicated page) |
| cpp/string/char_traits/dsc to_int_type | (see dedicated page) |
| cpp/string/char_traits/dsc eq_int_type | (see dedicated page) |
| cpp/string/char_traits/dsc eof | (see dedicated page) |
| cpp/string/char_traits/dsc not_eof | (see dedicated page) |


## Notes

*CharTraits* does not require defining the types and functions listed above as direct members, it only requires types like `X::type` and expressions like `X::func(args)` are valid and have the required semantics. Users-defined character traits can be derived from other character traits classes and only override some of their members, see the example below.

## Example


### Example

```cpp
#include <cctype>
#include <iostream>
#include <string>
#include <string_view>

struct ci_char_traits : public std::char_traits<char>
{
    static char to_upper(char ch)
    {
        return std::toupper((unsigned char) ch);
    }

    static bool eq(char c1, char c2)
    {
        return to_upper(c1) == to_upper(c2);
    }

    static bool lt(char c1, char c2)
    {
         return to_upper(c1) < to_upper(c2);
    }

    static int compare(const char* s1, const char* s2, std::size_t n)
    {
        while (n-- != 0)
        {
            if (to_upper(*s1) < to_upper(*s2))
                return -1;
            if (to_upper(*s1) > to_upper(*s2))
                return 1;
            ++s1;
            ++s2;
        }
        return 0;
    }

    static const char* find(const char* s, std::size_t n, char a)
    {
        const auto ua{to_upper(a)};
        while (n-- != 0) 
        {
            if (to_upper(*s) == ua)
                return s;
            s++;
        }
        return nullptr;
    }
};

template<class DstTraits, class CharT, class SrcTraits>
constexpr std::basic_string_view<CharT, DstTraits>
    traits_cast(const std::basic_string_view<CharT, SrcTraits> src) noexcept
{
    return {src.data(), src.size()};
}

int main()
{
    using namespace std::literals;

    constexpr auto s1 = "Hello"sv;
    constexpr auto s2 = "heLLo"sv;

    if (traits_cast<ci_char_traits>(s1) == traits_cast<ci_char_traits>(s2))
        std::cout << s1 << " and " << s2 << " are equal\n";
}
```


**Output:**
```
Hello and heLLo are equal
```


## See also


| cpp/string/dsc basic_string | (see dedicated page) |
| cpp/string/dsc basic_string_view | (see dedicated page) |
| cpp/io/dsc basic_istream | (see dedicated page) |
| cpp/io/dsc basic_ostream | (see dedicated page) |
| cpp/io/dsc basic_streambuf | (see dedicated page) |


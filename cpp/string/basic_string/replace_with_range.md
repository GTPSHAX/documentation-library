---
title: std::basic_string::replace_with_range
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/replace_with_range
---

ddcl|since=c++23|1=
template< container-compatible-range<CharT> R >
constexpr std::basic_string& replace_with_range( const_iterator first,
const_iterator last,
R&& rg );
Replaces the characters in the range [first, last) with the characters from the range `rg`.
Equivalent to

```cpp
return replace(first,
               last,
               std::basic_string(
                   std::from_range,
                   std::forward<R>(rg),
                   get_allocator())
);
```


## Parameters


### Parameters

- `first, last` - range of characters that is going to be replaced
- `rg` - a 

## Return value

`*this`

## Complexity

Linear in size of `rg`.

## Exceptions


## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <forward_list>
#include <iterator>
#include <string>

int main()
{
    using namespace std::literals;

    auto s{"Today is today!"s};
    constexpr auto today{"today"sv};
    constexpr auto tomorrow{"tomorrow's yesterday"sv};
    std::forward_list<char> rg;
    std::ranges::reverse_copy(tomorrow, std::front_inserter(rg));

    const auto pos{s.rfind(today)};
    assert(pos != s.npos);
    const auto first{std::next(s.begin(), pos)};
    const auto last{std::next(first, today.length())};

#ifdef __cpp_lib_containers_ranges
    s.replace_range(first, last, rg);
#else
    s.replace(first, last, rg.cbegin(), rg.cend());
#endif

    assert("Today is tomorrow's yesterday!" == s);
}
```


## See also


| cpp/string/basic_string/dsc replace | (see dedicated page) |


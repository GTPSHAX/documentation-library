---
title: deduction guides for std::basic_string_view
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/deduction_guides
---


# deduction guides for tt|std::basic_string_view


```cpp
**Header:** `<`string_view`>`
dcl|num=1|since=c++20|
template< class It, class End >
basic_string_view( It, End ) -> basic_string_view<std::iter_value_t<It>>;
dcl|num=2|since=c++23|
template< class R >
basic_string_view( R&& ) -> basic_string_view<ranges::range_value_t<R>>;
```

These deduction guides are provided for `std::basic_string_view`.
1. This deduction guide allow the character type to be deduced from the iterator-sentinel pair. .
2. This deduction guide allow the character type to be deduced from the range. .

## Example


### Example

```cpp
#include <array>
#include <iostream>
#include <string_view>

int main()
{
    std::array a1{'n', 'u', 'c', 'l', 'e', 'o', 'n', 's', ':', '\n'};
    std::basic_string_view s1(a1.cbegin(), a1.cend()); // deduction: CharT -> char
    static_assert(std::is_same_v<decltype(s1)::value_type, char>);
    std::cout << s1;

    std::array a2{L'p', L'r', L'o', L't', L'o', L'n', L's', L'\n'};
    std::basic_string_view s2(a2.cbegin(), a2.cend()); // deduction: CharT -> wchar_t
    static_assert(std::is_same_v<decltype(s2)::value_type, wchar_t>);
    std::wcout << s2;

    std::array<long, 9> a3{'n', 'e', 'u', 't', 'r', 'o', 'n', 's', '\n'};
    std::basic_string_view s3(a3.cbegin(), a3.cend()); // deduction: CharT -> long
    static_assert(std::is_same_v<decltype(s3)::value_type, long>);
    for (const auto e : s3)
        std::cout << static_cast<char>(e);
}
```


**Output:**
```
nucleons:
protons
neutrons
```


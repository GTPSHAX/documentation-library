---
title: std::hash<std::basic_string>
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/hash
---


```cpp
**Header:** `<`string`>`
dcl|num=1|since=c++11|
template< class A >
struct hash<std::basic_string<char, std::char_traits<char>, A>>;
dcl|num=2|since=c++11|
template< class A >
struct hash<std::basic_string<char16_t, std::char_traits<char16_t>, A>>;
dcl|num=3|since=c++11|
template< class A >
struct hash<std::basic_string<char32_t, std::char_traits<char32_t>, A>>;
dcl|num=4|since=c++11|
template< class A >
struct hash<std::basic_string<wchar_t, std::char_traits<wchar_t>, A>>;
dcl|num=5|since=c++20|
template< class A >
struct hash<std::basic_string<char8_t, std::char_traits<char8_t>, A>>;
```

The template specializations of `std::hash` for the various string classes allow users to obtain hashes of strings.
rrev|since=c++17|
These hashes equal the hashes of corresponding `std::basic_string_view` classes: If `S` is one of these string types, `SV` is the corresponding string view type, and `s` is an object of type `S`, then `1=std::hash<S>()(s) == std::hash<SV>()(SV(s))`.

## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <memory_resource>
#include <string>
#include <string_view>
using namespace std::literals;

int main()
{
    auto sv = "Stand back! I've got jimmies!"sv;
    std::string s(sv);
    std::pmr::string pmrs(sv); // use default allocator

    std::cout << std::hash<std::string_view>{}(sv) << '\n';
    std::cout << std::hash<std::string>{}(s) << '\n';
    std::cout << std::hash<std::pmr::string>{}(pmrs) << '\n';
}
```


**Output:**
```
3544599705012401047
3544599705012401047
3544599705012401047
```


## Defect reports


## See also


| cpp/utility/dsc hash | (see dedicated page) |
| cpp/string/basic_string_view/dsc hash | (see dedicated page) |


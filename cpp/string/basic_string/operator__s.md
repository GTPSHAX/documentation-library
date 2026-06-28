---
title: std::literals::string_literals::operator""s
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/operator""s
---


```cpp
**Header:** `<`string`>`
dcla|num=1|since=c++14|constexpr=c++20|
std::string operator""s( const char* str, std::size_t len );
dcl|num=2|since=c++20|
constexpr std::u8string operator""s( const char8_t* str,
std::size_t len );
dcla|num=3|since=c++14|constexpr=c++20|
std::u16string operator""s( const char16_t* str, std::size_t len );
dcla|num=4|since=c++14|constexpr=c++20|
std::u32string operator""s( const char32_t* str, std::size_t len );
dcla|num=5|since=c++14|constexpr=c++20|
std::wstring operator""s( const wchar_t* str, std::size_t len );
```

Forms a string literal of the desired type.
1. Returns }.
2. Returns }.
3. Returns }.
4. Returns }.
5. Returns }.

## Parameters


### Parameters

- `str` - pointer to the beginning of the raw character array literal
- `len` - length of the raw character array literal

## Return value

The string literal.

## Notes

These operators are declared in the namespace `std::literals::string_literals`, where both `literals` and `string_literals` are inline namespaces. Access to these operators can be gained with any of the following `using` directives:
* `using namespace std::literals`
* `using namespace std::string_literals`
* `using namespace std::literals::string_literals`
`std::chrono::duration` also defines `cpp/chrono/operator""s` to represent literal seconds, but it is an arithmetic literal: `10.0s` and `10s` are ten seconds, but `"10"s` is a string.

## Example


### Example

```cpp
#include <iostream>
#include <string>

void print_with_zeros(const auto note, const std::string& s)
{
    std::cout << note;
    for (const char c : s)
        c ? std::cout << c : std::cout << "₀";
    std::cout << " (size = " << s.size() << ")\n";
}

int main()
{
    using namespace std::string_literals;

    std::string s1 = "abc\0\0def";
    std::string s2 = "abc\0\0def"s;
    print_with_zeros("s1: ", s1);
    print_with_zeros("s2: ", s2);

    std::cout << "abcdef"s.substr(1,4) << '\n';
}
```


**Output:**
```
s1: abc (size = 3)
s2: abc₀₀def (size = 8)
bcde
```


## See also


| cpp/string/basic_string/dsc constructor | (see dedicated page) |
| cpp/string/basic_string_view/dsc operator""sv | (see dedicated page) |


---
title: std::basic_string::operator basic_string_view
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/operator_basic_string_view
---

ddcl|since=c++17|notes=<sup>(constexpr C++20)</sup>|
operator std::basic_string_view<CharT, Traits>() const noexcept;
Returns a `std::basic_string_view`, constructed as if by `std::basic_string_view<CharT, Traits>(data(), size())`.

## Parameters

(none)

## Return value

A string view representing the entire contents of the string.

## Notes

It is the programmer's responsibility to ensure that the resulting string view does not outlive the string.

```cpp
std::string get_string();
int f(std::string_view sv);

int x = f(get_string()); // OK
std::string_view sv = get_string(); // Bad: holds a dangling pointer
```


## Example


### Example

```cpp
#include <iostream>
#include <string>
#include <string_view>

void show_wstring_size(std::wstring_view wcstr_v)
{
    std::cout << wcstr_v.size() << " code points\n";
}

int main()
{
    std::string cppstr = "ラーメン";   // narrow string
    std::wstring wcstr = L"ラーメン";  // wide string

    // Implicit conversion from string to string_view
    // via std::string::operator string_view:
    std::string_view cppstr_v = cppstr;

    std::cout << cppstr_v << '\n'
              << cppstr_v.size() << " code units\n";

    // Implicit conversion from wstring to wstring_view
    // via std::wstring::operator wstring_view:
    show_wstring_size(wcstr);
}
```


**Output:**
```
ラーメン
12 code units
4 code points
```


## See also


| cpp/string/basic_string_view/dsc constructor | (see dedicated page) |


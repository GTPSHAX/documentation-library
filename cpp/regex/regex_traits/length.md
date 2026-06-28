---
title: std::regex_traits::length
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_traits/length
---

ddcl|1=
static std::size_t length( const char_type* p );
Calculates the length of a null-terminated character sequence, that is, the smallest `i` such that `1=p[i] == 0`.
Standard library specializations of `std::regex_traits` execute `std::char_traits<CharT>::length(p);`.

## Parameters


### Parameters

- `p` - pointer to the first element of the null-terminated character sequence

## Return value

The length of the null-terminated character string.

## Example


### Example

```cpp
#include <iostream>
#include <regex>

int main()
{
    std::cout << std::regex_traits<char>::length("Кошка") << '\n'
              << std::regex_traits<wchar_t>::length(L"Кошка") << '\n';
}
```


**Output:**
```
10
5
```


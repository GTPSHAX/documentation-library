---
title: std::char_traits::length
type: Strings
source: https://en.cppreference.com/w/cpp/string/char_traits/length
---

ddcl|notes=<sup>(constexpr C++17)</sup>|
static std::size_t length( const char_type* s );
Returns the length of the character sequence pointed to by `s`, that is, the position of the terminating null character (`char_type()`).
See *CharTraits* for the general requirements on character traits for `X::length`.

## Parameters


### Parameters

- `s` - pointer to a character sequence to return length of

## Return value

The length of character sequence pointed to by `s`.

## Complexity

Linear.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <string>

void print(const char* str)
{
    std::cout << std::quoted(str) << " has length = "
              << std::char_traits<char>::length(str) << '\n';
}

int main()
{
    print("foo");

    std::string s{"booo"};
    print(s.c_str());
}
```


**Output:**
```
"foo" has length = 3
"booo" has length = 4
```


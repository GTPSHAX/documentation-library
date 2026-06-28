---
title: std::basic_string::copy
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/copy
---

ddcl|notes=<sup>(constexpr C++20)</sup>|1=
size_type copy( CharT* dest, size_type count, size_type pos = 0 ) const;
Copies a substring [pos, pos + count) to character string pointed to by `dest`. If the requested substring lasts past the end of the string, or if `1=count == npos`, the copied substring is .
The resulting character string is not null-terminated.

## Parameters


### Parameters

- `dest` - pointer to the destination character string
- `count` - length of the substring
- `pos` - position of the first character to include

## Return value

Number of characters copied.

## Exceptions

`std::out_of_range` if `pos > size()`.

## Complexity

Linear in `count`.

## Example


### Example

```cpp
#include <iostream>
#include <string>

int main()
{
    std::string foo("WINE");

    // brace-initialization initializes all characters to 0,
    // providing a null-terminator
    char bar[4]{};

    // do not copy the last char, to guarantee null-termination
    foo.copy(bar, sizeof bar - 1);

    std::cout << bar << '\n'; // requires bar to be null-terminated
}
```


**Output:**
```
WIN
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-847 | C++98 | there was no exception safety guarantee | added strong exception safety guarantee |


## See also


| cpp/string/basic_string/dsc substr | (see dedicated page) |
| cpp/string/basic_string_view/dsc copy | (see dedicated page) |
| cpp/algorithm/dsc copy | (see dedicated page) |
| cpp/string/byte/dsc memcpy | (see dedicated page) |


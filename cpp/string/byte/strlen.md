---
title: std::strlen
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/strlen
---

ddcl|header=cstring|
std::size_t strlen( const char* str );
Returns the length of the given byte string, that is, the number of characters in a character array whose first element is pointed to by `str` up to and not including the first null character. The behavior is undefined if there is no null character in the character array pointed to by `str`.

## Parameters


### Parameters

- `str` - pointer to the null-terminated byte string to be examined

## Return value

The length of the null-terminated string `str`.

## Possible implementation

eq fun
|1=
std::size_t strlen(const char* start)
{
// NB: start is not checked for nullptr!
const char* end = start;
while (*end != '\0')
++end;
return end - start;
}

## Example


### Example

```cpp
#include <cstring>
#include <iostream>

int main()
{
    const char str[] = "dog cat\0mouse";

    std::cout << "without null character: " << std::strlen(str) << '\n'
              << "with null character: " << sizeof str << '\n';
}
```


**Output:**
```
without null character: 7
with null character: 14
```


## See also


| cpp/string/wide/dsc wcslen | (see dedicated page) |
| cpp/string/multibyte/dsc mblen | (see dedicated page) |


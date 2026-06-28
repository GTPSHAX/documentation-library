---
title: std::wcslen
type: Strings
source: https://en.cppreference.com/w/cpp/string/wide/wcslen
---

ddcl|header=cwchar|
std::size_t wcslen( const wchar_t* str );
Returns the length of a wide string, that is the number of non-null wide characters that precede the terminating null wide character.
The behavior is undefined if there is no null character in the wide character array pointed to by `str`.

## Parameters


### Parameters

- `str` - pointer to the null-terminated wide string to be examined

## Return value

The length of the null-terminated wide string `str`.

## Possible implementation

eq fun
|1=
std::size_t wcslen(const wchar_t* start)
{
// NB: start is not checked for nullptr!
const wchar_t* end = start;
while (*end != L'\0')
++end;
return end - start;
}

## Example


### Example

```cpp
#include <iostream>
#include <cwchar>
int main()
{
    const wchar_t* str = L"Hello, world!";
    std::wcout << "The length of L\"" << str << "\" is " << std::wcslen(str) << '\n';
}
```


**Output:**
```
The length of L"Hello, world!" is 13
```


## See also


| cpp/string/byte/dsc strlen | (see dedicated page) |
| cpp/string/multibyte/dsc mblen | (see dedicated page) |


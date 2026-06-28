---
title: std::basic_streambuf::setbuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_streambuf/pubsetbuf
---


```cpp
dcl|num=1|1=
public:
basic_streambuf<CharT, Traits>* pubsetbuf( char_type* s, std::streamsize n )
dcl|num=2|1=
protected:
virtual basic_streambuf<CharT, Traits>* setbuf( char_type* s, std::streamsize n )
```

1. Calls `setbuf(s, n)` of the most derived class.
2. The base class version of this function has no effect. The derived classes may override this function to allow removal or replacement of the controlled character sequence (the buffer) with a user-provided array, or for any other implementation-specific purpose.

## Parameters


### Parameters

- `s` - pointer to the first `CharT` in the user-provided buffer
- `n` - the number of `CharT` elements in the user-provided buffer

## Return value

1. The return value of `setbuf(s, n)`.
2. `this`

## Example


### Example

```cpp
#include <fstream>
#include <iostream>
#include <string>

int main()
{
    int cnt = 0;
    std::ifstream file;
    char buf[1024 * 10 + 1];

    file.rdbuf()->pubsetbuf(buf, sizeof buf);

    file.open("/usr/share/dict/words");

    for (std::string line; getline(file, line);)
        ++cnt;

    std::cout << cnt << '\n';
}
```


**Output:**
```
356010
```


## Defect reports


## See also


| cpp/io/basic_stringbuf/dsc setbuf | (see dedicated page) |
| cpp/io/basic_filebuf/dsc setbuf | (see dedicated page) |
| cpp/io/strstreambuf/dsc setbuf | (see dedicated page) |
| cpp/io/c/dsc setbuf | (see dedicated page) |


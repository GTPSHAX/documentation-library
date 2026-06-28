---
title: std::ferror
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/ferror
---

ddcl|header=cstdio|
int ferror( std::FILE* stream );
Checks the given stream for errors.

## Parameters


### Parameters

- `stream` - the file stream to check

## Return value

Nonzero value if the file stream has errors occurred, `0` otherwise.

## Example


### Example

```cpp
#include <clocale>
#include <cstdio>
#include <cstdlib>
#include <cwchar>

int main()
{
    const char *fname = std::tmpnam(nullptr);
    std::FILE* f = std::fopen(fname, "wb");
    std::fputs("\xff\xff\n", f); // not a valid UTF-8 character sequence
    std::fclose(f);

    std::setlocale(LC_ALL, "en_US.utf8");
    f = std::fopen(fname, "rb");
    std::wint_t ch;
    while ((ch=std::fgetwc(f)) != WEOF) // attempt to read as UTF-8
        std::printf("%#x ", ch);

    if (std::feof(f))
        puts("EOF indicator set");
    if (std::ferror(f))
        puts("Error indicator set");
}
```


**Output:**
```
Error indicator set
```


## See also


| cpp/io/c/dsc clearerr | (see dedicated page) |
| cpp/io/c/dsc feof | (see dedicated page) |
| cpp/io/basic_ios/dsc fail | (see dedicated page) |


---
title: std::putc
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/fputc
---

ddcl|header=cstdio|
int fputc( int ch, std::FILE* stream );
int putc( int ch, std::FILE* stream );
Writes a character `ch` to the given output stream `stream`.
Internally, the character is converted to `unsigned char` just before being written.
In C, `putc()` may be implemented as a macro, which is disallowed in C++. Therefore, calls to `std::fputc()` and `std::putc()` always have the same effect.

## Parameters


### Parameters

- `ch` - character to be written
- `stream` - output stream

## Return value

On success, returns the written character.
On failure, returns `EOF` and sets the ''error'' indicator (see `std::ferror()`) on `stream`.

## Example


### Example

```cpp
#include <cstdio>

int main()
{
    for (char c = 'a'; c != 'z'; c++)
        std::putc(c, stdout);

    // putchar's return value is not equal to the argument
    int r = 0x102A;
    std::printf("\nr = 0x%x\n", r);

    r = std::putchar(r);
    std::printf("\nr = 0x%x\n", r);
}
```


**Output:**
```
abcdefghijklmnopqrstuvwxy
r = 0x102A
*
r = 0x2A
```


## See also


| cpp/io/c/dsc putchar | (see dedicated page) |


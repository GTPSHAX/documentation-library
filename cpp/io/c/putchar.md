---
title: std::putchar
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/putchar
---

ddcl|header=cstdio|
int putchar( int ch );
Writes a character `ch` to `stdout`. Internally, the character is converted to `unsigned char` just before being written.
Equivalent to `std::putc(ch, stdout)`.

## Parameters


### Parameters

- `ch` - character to be written

## Return value

On success, returns the written character.
On failure, returns `EOF` and sets the “error” indicator (see `std::ferror()`) on `stdout`.

## Example


### Example

```cpp
#include <cstdio>

int main()
{
    for (char c = 'a'; c != 'z'; ++c)
        std::putchar(c);

    // putchar return value is not equal to the argument
    int r = 0x1024;
    std::printf("\nr = 0x%x\n", r);
    r = std::putchar(r);
    std::printf("\nr = 0x%x\n", r);
}
```


**Output:**
```
abcdefghijklmnopqrstuvwxy
r = 0x1024
$
r = 0x24
```


## See also


| cpp/io/c/dsc fputc | (see dedicated page) |


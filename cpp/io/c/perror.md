---
title: std::perror
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/perror
---

ddcl|header=cstdio|
void perror( const char *s );
Prints a textual description of the error code currently stored in the system variable `errno` to `stderr`.
The description is formed by concatenating the following components:
* the contents of the null-terminated byte string pointed to by `s`, followed by `": "` (unless `s` is a null pointer or the character pointed to by `s` is the null character).
* implementation-defined error message string describing the error code stored in `errno`, followed by `'\n'`. The error message string is identical to the result of `std::strerror(errno)`.

## Parameters


### Parameters

- `s` - pointer to a null-terminated string with explanatory message

## Return value

(none)

## Example


### Example

```cpp
#include <cerrno>
#include <cmath>
#include <cstdio>

int main()
{
    double not_a_number = std::log(-1.0);
    if (errno == EDOM)
        std::perror("log(-1) failed");
    std::printf("%f\n", not_a_number);
}
```


**Output:**
```
log(-1) failed: Numerical argument out of domain
nan
```


## See also


| cpp/error/dsc errno | (see dedicated page) |
| cpp/string/byte/dsc strerror | (see dedicated page) |


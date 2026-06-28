---
title: std::showpos
type: Input/output
source: https://en.cppreference.com/w/cpp/io/manip/showpos
---


```cpp
**Header:** `<`ios`>`
dcl|num=1|
std::ios_base& showpos( std::ios_base& str );
dcl|num=2|
std::ios_base& noshowpos( std::ios_base& str );
```

Enables or disables the display of the plus sign `'+'` in non-negative integer output. Has no effect on input.
1. Enables the `showpos` flag in the stream `str` as if by calling `str.setf(std::ios_base::showpos)`.
2. Disables the `showpos` flag in the stream `str` as if by calling `str.unsetf(std::ios_base::showpos)`.
This is an I/O manipulator, it may be called with an expression such as `out << std::showpos` for any `out` of type `std::basic_ostream` or with an expression such as `in >> std::showpos` for any `in` of type `std::basic_istream`.

## Parameters


### Parameters

- `str` - reference to I/O stream

## Return value

`str` (reference to the stream after manipulation).

## Example


### Example

```cpp
#include <iostream>

int main()
{
    std::cout
        << "showpos: " << std::showpos << 42 << ' ' << 3.14 << ' ' << 0 << '\n'
        << "noshowpos: " << std::noshowpos << 42 << ' ' << 3.14 << ' ' << 0 << '\n';
}
```


**Output:**
```
showpos: +42 +3.14 +0
noshowpos: 42 3.14 0
```


## See also


| cpp/io/manip/dsc resetiosflags | (see dedicated page) |
| cpp/io/manip/dsc setiosflags | (see dedicated page) |


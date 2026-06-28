---
title: std::setw
type: Input/output
source: https://en.cppreference.com/w/cpp/io/manip/setw
---

ddcl|header=iomanip|
/* unspecified */ setw( int n );
When used in an expression `out << std::setw(n)` or `in >> std::setw(n)`, sets the `width` parameter of the stream `out` or `in` to exactly `n`.
Some operations reset the width to zero (see below), so `std::setw` may need to be repeatedly called to set the width for multiple operations.

## Parameters


### Parameters

- `n` - new value for width

## Return value


## Notes

The width property of the stream will be reset to zero (meaning "unspecified") if any of the following functions are called:
* Input
:*
:*
* Output
:* Overloads of  that take arithmetic types or `void` pointers (at Stage 3 of )
:*  and
:*
:* `std::put_money` (inside )
:* `std::quoted` (when used with an output stream)
The exact effects this modifier has on the input and output vary between the individual I/O functions and are described at each `operator<<` and `operator>>` overload page individually.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <sstream>

int main()
{
    std::cout << "no setw: [" << 42 << "]\n"
              << "setw(6): [" << std::setw(6) << 42 << "]\n"
              << "no setw, several elements: [" << 89 << 12 << 34 << "]\n"
              << "setw(6), several elements: [" << 89 << std::setw(6) << 12 << 34 << "]\n";

    std::istringstream is("hello, world");
    char arr[10];

    is >> std::setw(6) >> arr;
    std::cout << "Input from \"" << is.str() << "\" with setw(6) gave \""
              << arr << "\"\n";
}
```


**Output:**
```
no setw: [42]
setw(6): [    42]
no setw, several elements: [891234]
setw(6), several elements: [89    1234]
Input from "hello, world" with setw(6) gave "hello"
```


## Defect reports


## See also


| cpp/io/ios_base/dsc width|mem=std::ios_base | (see dedicated page) |
| cpp/io/manip/dsc setfill | (see dedicated page) |
| cpp/io/manip/dsc left | (see dedicated page) |
| cpp/io/manip/dsc showbase | (see dedicated page) |


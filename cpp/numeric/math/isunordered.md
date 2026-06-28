---
title: std::isunordered
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/math/isunordered
---

cpp/numeric/math/binary_is|isunordered
|description= Determines if the floating point numbers `x` and `y` are unordered, that is, one or both are NaN and thus cannot be meaningfully compared with each other.
|condition=either `x` or `y` is NaN

## Example


### Example

```cpp
#include <cmath>
#include <iostream>

#define SHOW_UNORDERED(x, y) \
    std::cout << std::boolalpha << "isunordered(" \
              << #x << ", " << #y << "): " \
              << std::isunordered(x, y) << '\n'

int main()
{
    SHOW_UNORDERED(10, 01);
    SHOW_UNORDERED(INFINITY, NAN);
    SHOW_UNORDERED(INFINITY, INFINITY);
    SHOW_UNORDERED(NAN, NAN);
}
```


**Output:**
```
isunordered(10, 01): false
isunordered(INFINITY, NAN): true
isunordered(INFINITY, INFINITY): false
isunordered(NAN, NAN): true
```


## See also


| cpp/numeric/math/dsc fpclassify | (see dedicated page) |
| cpp/numeric/math/dsc isnan | (see dedicated page) |


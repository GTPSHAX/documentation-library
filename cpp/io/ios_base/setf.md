---
title: std::ios_base::setf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ios_base/setf
---


```cpp
dcl|num=1|
fmtflags setf( fmtflags flags );
dcl|num=2|
fmtflags setf( fmtflags flags, fmtflags mask );
```

Sets the formatting flags to specified settings.
1. Sets the formatting flags identified by `flags`. Effectively, the following operation is performed `1=fl = fl  where `fl` defines the state of internal formatting flags.
2. Clears the formatting flags under `mask`, and sets the cleared flags to those specified by `flags`. Effectively the following operation is performed `1=fl = (fl & ~mask)  where `fl` defines the state of internal formatting flags.

## Parameters


### Parameters

- `flags, mask` - new formatting setting. `mask` defines which flags can be altered, `flags` defines which flags of those to be altered should be set (others will be cleared). Both parameters can be a combination of the formatting flags constants

#### Formatting flags


## Return value

The formatting flags before the call to the function.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <numbers>

int main()
{
    const double PI = std::numbers::pi;
    const int WIDTH = 15;

    std::cout.setf(std::ios::right); // equivalent: cout << right;
    std::cout << std::setw(WIDTH / 2) << "radius"
              << std::setw(WIDTH) << "circumference" << '\n';

    std::cout.setf(std::ios::fixed); // equivalent: cout << fixed;
    for (double radius = 1; radius <= 6; radius += 0.5)
        std::cout << std::setprecision(1) << std::setw(WIDTH / 2)
                  << radius
                  << std::setprecision(2) << std::setw(WIDTH)
                  << (2 * PI * radius) << '\n';
}
```


**Output:**
```
<nowiki/>
 radius  circumference
    1.0           6.28
    1.5           9.42
    2.0          12.57
    2.5          15.71
    3.0          18.85
    3.5          21.99
    4.0          25.13
    4.5          28.27
    5.0          31.42
    5.5          34.56
    6.0          37.70
```


## See also


| cpp/io/ios_base/dsc flags | (see dedicated page) |
| cpp/io/ios_base/dsc unsetf | (see dedicated page) |


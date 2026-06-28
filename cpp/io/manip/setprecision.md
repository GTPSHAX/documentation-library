---
title: std::setprecision
type: Input/output
source: https://en.cppreference.com/w/cpp/io/manip/setprecision
---

ddcl|header=iomanip|
/*unspecified*/ setprecision( int n );
When used in an expression `out << setprecision(n)` or `in >> setprecision(n)`, sets the `precision` parameter of the stream `out` or `in` to exactly `n`.

## Parameters


### Parameters

- `n` - new value for precision

## Return value


## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <limits>
#include <numbers>

int main()
{
    constexpr long double pi{std::numbers::pi_v<long double>};

    const auto default_precision{std::cout.precision()};
    constexpr auto max_precision{std::numeric_limits<long double>::digits10 + 1}; 

    std::cout << "default precision: " << default_precision << '\n'
              << "maximum precision: " << max_precision << "\n\n"
                 "precision: pi:\n";

    for (int p{0}; p <= max_precision; ++p)
        std::cout << std::setw(2) << p << "  " << std::setprecision(p) << pi << '\n';

    std::cout << std::setprecision(default_precision); // restore defaults
}
```


**Output:**
```
default precision: 6
maximum precision: 19

precision: pi:
 0  3
 1  3
 2  3.1
 3  3.14
 4  3.142
 5  3.1416
 6  3.14159
 7  3.141593
 8  3.1415927
 9  3.14159265
10  3.141592654
11  3.1415926536
12  3.14159265359
13  3.14159265359
14  3.1415926535898
15  3.14159265358979
16  3.141592653589793
17  3.1415926535897932
18  3.14159265358979324
19  3.141592653589793239
```


## Defect reports


## See also


| cpp/io/manip/dsc fixed | (see dedicated page) |
| cpp/io/ios_base/dsc precision | (see dedicated page) |


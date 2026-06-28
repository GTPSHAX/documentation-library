---
title: std::iostream_category
type: Input/output
source: https://en.cppreference.com/w/cpp/io/iostream_category
---

ddcl|header=ios|since=c++11|
const std::error_category& iostream_category() noexcept;
Obtains a reference to the static error category object for iostream errors. The object is required to override the virtual function `error_category::name()` to return a pointer to the string `"iostream"`. It is used to identify error codes provided in the exceptions of type `std::ios_base::failure`.

## Parameters

(none)

## Return value

A reference to the static object of unspecified runtime type, derived from `std::error_category`.

## Example


### Example

```cpp
#include <fstream>
#include <iostream>

int main()
{
    std::ifstream f("doesn't exist");
    try
    {
        f.exceptions(f.failbit);
    }
    catch (const std::ios_base::failure& e)
    {
        std::cout << "Caught an ios_base::failure.\n"
                  << "Error code: " << e.code().value() 
                  << " (" << e.code().message() << ")\n"
                  << "Error category: " << e.code().category().name() << '\n';

    }
}
```


**Output:**
```
Caught an ios_base::failure.
Error code: 1 (unspecified iostream_category error)
Error category: iostream
```


## Defect reports


## See also


| cpp/io/ios_base/dsc failure | (see dedicated page) |
| cpp/io/dsc io_errc | (see dedicated page) |


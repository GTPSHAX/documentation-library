---
title: std::is_error_code_enum<std::io_errc>
type: Input/output
source: https://en.cppreference.com/w/cpp/io/io_errc/is_error_code_enum
---


```cpp
**Header:** `<`ios`>`
dcl|since=c++11|
template<>
struct is_error_code_enum<std::io_errc> : public std::true_type {};
```

This specialization of `std::is_error_code_enum` informs other library components that values of type `std::io_errc` are enumerations that hold error codes, which makes them implicitly convertible and assignable to objects of type `std::error_code`.

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
        std::cout << "Caught an ios_base::failure.\n";
        if (e.code() == std::io_errc::stream)
            std::cout << "The error code is std::io_errc::stream\n";
    }
}
```


**Output:**
```
Caught an ios_base::failure.
The error code is std::io_errc::stream
```


## See also


| cpp/error/error_code/dsc is_error_code_enum | (see dedicated page) |
| cpp/error/dsc error_code | (see dedicated page) |
| cpp/io/dsc io_errc | (see dedicated page) |


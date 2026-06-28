---
title: std::io_errc
type: Input/output
source: https://en.cppreference.com/w/cpp/io/io_errc
---


```cpp
**Header:** `<`ios`>`
dcl|since=c++11|1=
enum class io_errc {
stream = 1,
};
```

The scoped enumeration `std::io_errc` defines the error codes reported by I/O streams in `std::ios_base::failure` exception objects. Only one error code (`std::io_errc::stream`) is required, although the implementation may define additional error codes. Because the appropriate specialization of `std::is_error_code_enum` is provided, values of type `std::io_errc` are implicitly convertible to `std::error_code`.

## Member constants


| Item | Description |
|------|-------------|
| **Enumeration constant** | Value |


## Non-member functions


| cpp/io/io_errc/dsc make_error_code | (see dedicated page) |
| cpp/io/io_errc/dsc make_error_condition | (see dedicated page) |


## Helper classes


| cpp/io/io_errc/dsc is_error_code_enum | (see dedicated page) |


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


| cpp/error/dsc error_code | (see dedicated page) |
| cpp/error/dsc error_condition | (see dedicated page) |
| cpp/io/ios_base/dsc failure|mem=std::ios_base | (see dedicated page) |


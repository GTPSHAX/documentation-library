---
title: std::make_error_code(std::io_errc)
type: Input/output
source: https://en.cppreference.com/w/cpp/io/io_errc/make_error_code
---


# make_error_codedsc small|(std::io_errc)

ddcl|header=ios|since=c++11|
std::error_code make_error_code( std::io_errc e ) noexcept;
Constructs an `std::error_code` object from a value of type `std::io_errc` as if by `return std::error_code(static_cast<int>(e), std::iostream_category())`.
This function is called by the constructor of `std::error_code` with an `std::io_errc` argument.

## Parameters


### Parameters

- `e` - error code number

## Return value

A value of type `std::error_code` that holds the error code number from `e` associated with the error category `"iostream"`.

## Example


### Example

```cpp
#include <iostream>
#include <system_error>

int main()
{
    std::error_code ec = std::make_error_code(std::io_errc::stream);

    // This works because of the overloaded method
    //    and the is_error_code_enum specialization.
    ec = std::io_errc::stream;

    std::cout << "Error code from io_errc::stream has category "
              << ec.category().name() << '\n';
}
```


**Output:**
```
Error code from io_errc::stream has category iostream
```


## Defect reports


## See also


| cpp/error/dsc error_code | (see dedicated page) |
| cpp/io/dsc io_errc | (see dedicated page) |
| cpp/error/errc/dsc make_error_code | (see dedicated page) |
| cpp/thread/future_errc/dsc make_error_code | (see dedicated page) |


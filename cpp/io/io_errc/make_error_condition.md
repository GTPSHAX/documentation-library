---
title: std::make_error_condition(std::io_errc)
type: Input/output
source: https://en.cppreference.com/w/cpp/io/io_errc/make_error_condition
---


# make_error_conditiondsc small|(std::io_errc)

ddcl|header=ios|since=c++11|
std::error_condition make_error_condition( std::io_errc e ) noexcept;
Constructs an `std::error_condition` object from a value of type `std::io_errc` as if by `return std::error_condition(static_cast<int>(e), std::iostream_category())`.

## Parameters


### Parameters

- `e` - error code number

## Return value

A value of type `std::error_condition` that holds the error code number from `e` associated with the error category `"iostream"`.

## Example


### Example

```cpp
#include <iostream>
#include <system_error>

int main()
{
    std::error_condition ec = std::make_error_condition(std::io_errc::stream);
    std::cout << "error condition for io_errc::stream has value " << ec.value()
              << "\nand message \"" << ec.message() << "\"\n";
}
```


**Output:**
```
error condition for io_errc::stream has value 1
and message "unspecified iostream_category error"
```


## Defect reports


## See also


| cpp/error/dsc error_condition | (see dedicated page) |
| cpp/io/dsc io_errc | (see dedicated page) |


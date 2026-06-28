---
title: std::error_condition
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_condition
---

ddcl|header=system_error|since=c++11|1=
class error_condition;
`std::error_condition` holds a platform-independent value identifying an error condition. Like `std::error_code`, it is uniquely identified by an integer value and a `std::error_category`, but unlike `std::error_code`, the value is not platform-dependent.
A typical implementation holds one integer data member (the value) and a pointer to an `std::error_category`.

## Member functions


| cpp/error/error_condition/dsc constructor | (see dedicated page) |
| cpp/error/error_condition/dsc operator{{= | (see dedicated page) |
| cpp/error/error_condition/dsc assign | (see dedicated page) |
| cpp/error/error_condition/dsc clear | (see dedicated page) |
| cpp/error/error_condition/dsc value | (see dedicated page) |
| cpp/error/error_condition/dsc category | (see dedicated page) |
| cpp/error/error_condition/dsc message | (see dedicated page) |
| cpp/error/error_condition/dsc operator bool | (see dedicated page) |


## Non-member functions


| cpp/error/error_condition/dsc operator_cmp | (see dedicated page) |


## Helper classes


| cpp/error/error_condition/dsc is_error_condition_enum | (see dedicated page) |
| cpp/error/error_condition/dsc hash | (see dedicated page) |


## Notes

The comparison between a `std::error_code` and a `std::error_condition` is defined by their error categories. Notably, an error condition of `std::generic_category` may compare equal to an error code of a specific category (e.g. `std::system_category`), if they represent the same kind of error.
A `std::errc` value can be compared to an error code via implicit conversion to `std::error_condition`.

### Example

```cpp
#include <cerrno>
#include <iostream>
#include <system_error>
#include <Windows.h>

int main()
{
    std::error_code ec{ERROR_FILE_EXISTS, std::system_category()};
    std::error_condition econd{EEXIST, std::generic_category()};

    std::cout.setf(std::ios::boolalpha);
    std::cout << (ec == econd) << '\n'; // typically true<!-- false with libc++, because libc++ treats generic_category() and system_category() as being equivalent, even on windows. See also https://github.com/llvm/llvm-project/pull/93101 -->
    std::cout << (ec == std::errc::file_exists) << '\n'; // ditto
    std::cout << (ec == make_error_code(std::errc::file_exists)) << '\n'; // false:
                                                                     // different category
}
```


**Output:**
```
true
true
false
```


## See also


| cpp/error/dsc error_code | (see dedicated page) |
| cpp/error/dsc error_category | (see dedicated page) |
| cpp/error/errc/dsc make_error_condition | (see dedicated page) |


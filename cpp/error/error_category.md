---
title: std::error_category
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_category
---

ddcl|header=system_error|since=c++11|1=
class error_category;
`std::error_category` serves as the base class for specific error category types, such as `std::system_category`, `std::iostream_category`, etc. Each specific category class defines the `error_code` - `error_condition` mapping and holds the explanatory strings for all error_conditions. The objects of error category classes are treated as singletons, passed by reference.

## Member functions


| cpp/error/error_category/dsc constructor | (see dedicated page) |
| cpp/error/error_category/dsc destructor | (see dedicated page) |
| cpp/error/error_category/dsc operator{{= | (see dedicated page) |
| cpp/error/error_category/dsc name | (see dedicated page) |
| cpp/error/error_category/dsc default_error_condition | (see dedicated page) |
| cpp/error/error_category/dsc equivalent | (see dedicated page) |
| cpp/error/error_category/dsc message | (see dedicated page) |
| cpp/error/error_category/dsc operator cmp | (see dedicated page) |


## Specific error categories


| cpp/error/dsc generic_category | (see dedicated page) |
| cpp/error/dsc system_category | (see dedicated page) |
| cpp/io/dsc iostream_category | (see dedicated page) |
| cpp/thread/dsc future_category | (see dedicated page) |


| ===See also=== | |


| cpp/error/dsc error_condition | (see dedicated page) |
| cpp/error/dsc error_code | (see dedicated page) |


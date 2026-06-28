---
title: std::out_of_range
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/out_of_range
---

ddcl|header=stdexcept|
class out_of_range;
Defines a type of object to be thrown as exception. It reports errors that are consequence of attempt to access elements out of defined range.
It may be thrown by the member functions of `std::bitset` and `std::basic_string`, by  `std::stoi` and `std::stod` families of functions, and by the bounds-checked member access functions (e.g. `std::vector::at` and `std::map::at`).

## Member functions


## Notes

The standard error condition `std::errc::result_out_of_range` typically indicates the condition where the result, rather than the input, is out of range, and is more closely related to `std::range_error` and `ERANGE`.

## Defect reports


## See also


| cpp/string/basic_string/dsc at | (see dedicated page) |
| cpp/string/basic_string_view/dsc at | (see dedicated page) |
| cpp/container/dsc at|deque | (see dedicated page) |
| cpp/container/dsc at|map | (see dedicated page) |
| cpp/container/dsc at|unordered_map | (see dedicated page) |
| cpp/container/dsc at|vector | (see dedicated page) |
| cpp/container/dsc at|array | (see dedicated page) |
| cpp/container/dsc at|span | (see dedicated page) |


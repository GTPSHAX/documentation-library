---
title: std::error_code
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_code
---

ddcl|header=system_error|since=c++11|1=
class error_code;
`std::error_code` represents a platform-dependent error code value. Each `std::error_code` object holds an error code value originating from the operating system or some low-level interface and a pointer to an object of type `std::error_category`, which corresponds to the said interface. The error code values are not required to be unique across different error categories.

## Member functions


| cpp/error/error_code/dsc constructor | (see dedicated page) |
| cpp/error/error_code/dsc operator{{= | (see dedicated page) |
| cpp/error/error_code/dsc assign | (see dedicated page) |

#### Modifiers

| cpp/error/error_code/dsc clear | (see dedicated page) |

#### Observers

| cpp/error/error_code/dsc value | (see dedicated page) |
| cpp/error/error_code/dsc category | (see dedicated page) |
| cpp/error/error_code/dsc default_error_condition | (see dedicated page) |
| cpp/error/error_code/dsc message | (see dedicated page) |
| cpp/error/error_code/dsc operator bool | (see dedicated page) |


## Non-member functions


| cpp/error/error_code/dsc operator_cmp | (see dedicated page) |
| cpp/error/error_code/dsc operator_ltlt | (see dedicated page) |


## Helper classes


| cpp/error/error_code/dsc is_error_code_enum | (see dedicated page) |
| cpp/error/error_code/dsc hash | (see dedicated page) |


## See also


| cpp/error/dsc error_condition | (see dedicated page) |
| cpp/error/dsc error_category | (see dedicated page) |
| cpp/error/errc/dsc make_error_code | (see dedicated page) |


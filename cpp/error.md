---
title: Error handling
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error
---


# Diagnostics library


## Exception handling

The header  provides several classes and functions related to exception handling in C++ programs.


| exception | |
| cpp/error/dsc exception | (see dedicated page) |

#### Capture and storage of exception objects

| cpp/error/dsc uncaught_exception | (see dedicated page) |
| cpp/error/dsc exception_ptr | (see dedicated page) |
| cpp/error/dsc make_exception_ptr | (see dedicated page) |
| cpp/error/dsc current_exception | (see dedicated page) |
| cpp/error/dsc rethrow_exception | (see dedicated page) |
| cpp/error/dsc nested_exception | (see dedicated page) |
| cpp/error/dsc throw_with_nested | (see dedicated page) |
| cpp/error/dsc rethrow_if_nested | (see dedicated page) |

#### Handling of failures in exception handling

| exception | |
| cpp/error/dsc terminate | (see dedicated page) |
| cpp/error/dsc terminate_handler | (see dedicated page) |
| cpp/error/dsc get_terminate | (see dedicated page) |
| cpp/error/dsc set_terminate | (see dedicated page) |
| cpp/error/dsc bad_exception | (see dedicated page) |

#### Handling of exception specification violations {{mark until c++17

| cpp/error/dsc unexpected | (see dedicated page) |
| cpp/error/dsc unexpected_handler | (see dedicated page) |
| cpp/error/dsc get_unexpected | (see dedicated page) |
| cpp/error/dsc set_unexpected | (see dedicated page) |


## Exception categories

Several convenience classes are predefined in the header `<stdexcept>` to report particular error conditions. These classes can be divided into two categories: ''logic'' errors and ''runtime'' errors. Logic errors are a consequence of faulty logic within the program and may be preventable. Runtime errors are due to events beyond the scope of the program and cannot easily be predicted.


| stdexcept | |
| cpp/error/inc logic_error | (see dedicated page) |
| cpp/error/inc invalid_argument | (see dedicated page) |
| cpp/error/inc domain_error | (see dedicated page) |
| cpp/error/inc length_error | (see dedicated page) |
| cpp/error/inc out_of_range | (see dedicated page) |
| cpp/error/inc runtime_error | (see dedicated page) |
| cpp/error/inc range_error | (see dedicated page) |
| cpp/error/inc overflow_error | (see dedicated page) |
| cpp/error/inc underflow_error | (see dedicated page) |
| cpp/error/tx_exception|exception class to cancel atomic transactions|notes= | |


## Error numbers


| cerrno | |
| cpp/error/dsc errno | (see dedicated page) |
| cpp/error/dsc errno_macros | (see dedicated page) |


## System error <sup>(C++11)</sup>

The header `<system_error>` defines types and functions used to report error conditions originating from the operating system, streams I/O, `std::future`, or other low-level APIs.


| system_error | |
| cpp/error/dsc error_category | (see dedicated page) |
| cpp/error/dsc generic_category | (see dedicated page) |
| cpp/error/dsc system_category | (see dedicated page) |
| cpp/error/dsc error_condition | (see dedicated page) |
| cpp/error/dsc errc | (see dedicated page) |
| cpp/error/dsc error_code | (see dedicated page) |
| cpp/error/dsc system_error | (see dedicated page) |


## Assertions

Assertions help to implement checking of preconditions in programs.


| cassert | |
| cpp/error/dsc assert | (see dedicated page) |


## Stacktrace <sup>(C++23)</sup>


| stacktrace | |
| cpp/utility/dsc stacktrace_entry | (see dedicated page) |
| cpp/utility/dsc basic_stacktrace | (see dedicated page) |


## Debugging support <sup>(C++26)</sup>


| debugging | |
| cpp/utility/dsc breakpoint | (see dedicated page) |
| cpp/utility/dsc breakpoint_if_debugging | (see dedicated page) |
| cpp/utility/dsc is_debugger_present | (see dedicated page) |


## See also


| cpp/language/dsc static_assert | (see dedicated page) |


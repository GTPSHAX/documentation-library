---
title: Input/output manipulators
type: Input/output
source: https://en.cppreference.com/w/cpp/io/manip
---


# Input/output manipulators

Manipulators are helper functions that make it possible to control input/output streams using `operator<<` or `operator>>`.
The manipulators that are invoked without arguments (e.g. `std::cout << std::boolalpha;` or `std::cin >> std::hex;`) are implemented as functions that take a reference to a stream as their only argument. The special overloads of `cpp/io/basic_ostream/operator_ltlt|basic_ostream::operator<<` and `cpp/io/basic_istream/operator_gtgt|basic_istream::operator>>` accept pointers to these functions. <sup>(since C++20)</sup> These functions (or instantiations of function templates) are the only addressable functions in the standard library.
The manipulators that are invoked with arguments (e.g. `std::cout << std::setw(10);`) are implemented as functions returning objects of unspecified type. These manipulators define their own `operator<<` or `operator>>` which perform the requested manipulation.


| ios | |
| cpp/io/manip/dsc boolalpha | (see dedicated page) |
| cpp/io/manip/dsc showbase | (see dedicated page) |
| cpp/io/manip/dsc showpoint | (see dedicated page) |
| cpp/io/manip/dsc showpos | (see dedicated page) |
| cpp/io/manip/dsc skipws | (see dedicated page) |
| cpp/io/manip/dsc uppercase | (see dedicated page) |
| cpp/io/manip/dsc unitbuf | (see dedicated page) |
| cpp/io/manip/dsc left | (see dedicated page) |
| cpp/io/manip/dsc hex | (see dedicated page) |
| cpp/io/manip/dsc fixed | (see dedicated page) |
| istream | |
| cpp/io/manip/dsc ws | (see dedicated page) |
| ostream | |
| cpp/io/manip/dsc ends | (see dedicated page) |
| cpp/io/manip/dsc flush | (see dedicated page) |
| cpp/io/manip/dsc endl | (see dedicated page) |
| cpp/io/manip/dsc emit_on_flush | (see dedicated page) |
| cpp/io/manip/dsc flush_emit | (see dedicated page) |
| iomanip | |
| cpp/io/manip/dsc resetiosflags | (see dedicated page) |
| cpp/io/manip/dsc setiosflags | (see dedicated page) |
| cpp/io/manip/dsc setbase | (see dedicated page) |
| cpp/io/manip/dsc setfill | (see dedicated page) |
| cpp/io/manip/dsc setprecision | (see dedicated page) |
| cpp/io/manip/dsc setw | (see dedicated page) |
| cpp/io/manip/dsc get_money | (see dedicated page) |
| cpp/io/manip/dsc put_money | (see dedicated page) |
| cpp/io/manip/dsc get_time | (see dedicated page) |
| cpp/io/manip/dsc put_time | (see dedicated page) |
| cpp/io/manip/dsc quoted | (see dedicated page) |


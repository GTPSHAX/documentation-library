---
title: iostream
type: Standard headers
source: https://en.cppreference.com/w/cpp/header/iostream
---

This header is part of the Input/output library.
Including `<iostream>` behaves as if it defines a static storage duration object of type `std::ios_base::Init`, whose constructor initializes the standard stream objects if it is the first `std::ios_base::Init` object to be constructed, and whose destructor flushes those objects (except for `cin` and `wcin`) if it is the last `std::ios_base::Init` object to be destroyed.


| cpp/header/dsc ios|{{mark c++11 | (see dedicated page) |
| cpp/header/dsc streambuf|{{mark c++11 | (see dedicated page) |
| cpp/header/dsc istream|{{mark c++11 | (see dedicated page) |
| cpp/header/dsc ostream|{{mark c++11 | (see dedicated page) |
| cpp/io/dsc cin | (see dedicated page) |
| cpp/io/dsc cout | (see dedicated page) |
| cpp/io/dsc cerr | (see dedicated page) |
| cpp/io/dsc clog | (see dedicated page) |


## Synopsis


## Defect reports


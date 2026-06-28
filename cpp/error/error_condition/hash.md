---
title: std::hash<std::error_condition>
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_condition/hash
---

ddcl | header=system_error | since=c++17 | 1=
template<> struct hash<std::error_condition>;
The template specialization of `std::hash` for `std::error_condition` allows users to obtain hashes of objects of type `std::error_condition`.

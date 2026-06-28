---
title: std::hash<std::error_code>
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_code/hash
---


# hashsmall|<std::error_code>

ddcl|header=system_error|since=c++11|1=
template<> struct hash<std::error_code>;
The template specialization of `std::hash` for `std::error_code` allows users to obtain hashes of objects of type `std::error_code`.

---
title: std::common_type<std::pair>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/pair/common_type
---

ddcl | header=utility | since=c++23 |
template< class T1, class T2, class U1, class U2 >
requires requires { typename std::pair<std::common_type_t<T1, U1>,
std::common_type_t<T2, U2>>; }
struct common_type<std::pair<T1, T2>, std::pair<U1, U2>>;
The common type of two `pair`s is a `pair` of both common types of corresponding element types of both `pair`s.
The common type is defined only if both pairs of corresponding element types have common types.

## Member types


## Example


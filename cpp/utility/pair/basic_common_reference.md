---
title: std::basic_common_reference<std::pair>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/pair/basic_common_reference
---

ddcl | header=utility | since=c++23 |
template< class T1, class T2, class U1, class U2,
template<class> class TQual, template<class> class UQual >
requires requires { typename std::pair<std::common_reference_t<TQual<T1>, UQual<U1>>,
std::common_reference_t<TQual<T2>, UQual<U2>>>; }
struct basic_common_reference<std::pair<T1, T2>, std::pair<U1, U2>, TQual, UQual>;
The common reference type of two `pair`s is a `pair` of both common reference types of corresponding element types of both `pair`s, where the cv and reference qualifiers on the `pair`s are applied to their element types.
The common reference type is defined only if both pairs of corresponding element types have common reference types.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Example


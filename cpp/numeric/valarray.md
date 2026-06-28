---
title: std::valarray
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray
---

ddcl|header=valarray|
template< class T >
class valarray;
`std::valarray` is the class for representing and manipulating arrays of values. It supports element-wise mathematical operations and various forms of generalized subscript operators, slicing and indirect access.

## Template parameters


### Parameters

- `T` - the type of the elements. The type must meet the *NumericType* requirements

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| dsc|`iterator`|unspecified mutable iterator type, meeting the *RandomAccessIterator* requirements <sup>(until C++20)</sup> and the *ContiguousIterator requirements*<sup>(since C++20)</sup> and modeling , such that | |
| * `std::iterator_traits<iterator>::value_type` is `T`, and | |
| * `std::iterator_traits<iterator>::reference` is `T&` | |
| dsc|`const_iterator`|unspecified constant iterator type, meeting the *RandomAccessIterator* requirements <sup>(until C++20)</sup> and the *ContiguousIterator requirements*<sup>(since C++20)</sup> and modeling , such that | |
| * `std::iterator_traits<const_iterator>::value_type` is `T`, and | |
| * `std::iterator_traits<const_iterator>::reference` is `const T&` | |


## Member functions


| cpp/numeric/valarray/dsc valarray | (see dedicated page) |
| cpp/numeric/valarray/dsc ~valarray | (see dedicated page) |
| cpp/numeric/valarray/dsc operator{{= | (see dedicated page) |
| cpp/numeric/valarray/dsc operator_at | (see dedicated page) |
| cpp/numeric/valarray/dsc operator_arith | (see dedicated page) |
| cpp/numeric/valarray/dsc operator_arith2 | (see dedicated page) |
| cpp/numeric/valarray/dsc swap | (see dedicated page) |
| cpp/numeric/valarray/dsc size | (see dedicated page) |
| cpp/numeric/valarray/dsc resize | (see dedicated page) |
| cpp/numeric/valarray/dsc sum | (see dedicated page) |
| cpp/numeric/valarray/dsc min | (see dedicated page) |
| cpp/numeric/valarray/dsc max | (see dedicated page) |
| cpp/numeric/valarray/dsc shift | (see dedicated page) |
| cpp/numeric/valarray/dsc cshift | (see dedicated page) |
| cpp/numeric/valarray/dsc apply | (see dedicated page) |
| cpp/numeric/valarray/dsc begin | (see dedicated page) |
| cpp/numeric/valarray/dsc end | (see dedicated page) |


## Non-member functions


| cpp/numeric/valarray/dsc swap2 | (see dedicated page) |
| cpp/numeric/valarray/dsc operator_arith3 | (see dedicated page) |
| cpp/numeric/valarray/dsc operator_cmp | (see dedicated page) |
| cpp/numeric/valarray/dsc abs | (see dedicated page) |

#### Exponential functions

| cpp/numeric/valarray/dsc exp | (see dedicated page) |
| cpp/numeric/valarray/dsc log | (see dedicated page) |
| cpp/numeric/valarray/dsc log10 | (see dedicated page) |

#### Power functions

| cpp/numeric/valarray/dsc pow | (see dedicated page) |
| cpp/numeric/valarray/dsc sqrt | (see dedicated page) |

#### Trigonometric functions

| cpp/numeric/valarray/dsc sin | (see dedicated page) |
| cpp/numeric/valarray/dsc cos | (see dedicated page) |
| cpp/numeric/valarray/dsc tan | (see dedicated page) |
| cpp/numeric/valarray/dsc asin | (see dedicated page) |
| cpp/numeric/valarray/dsc acos | (see dedicated page) |
| cpp/numeric/valarray/dsc atan | (see dedicated page) |
| cpp/numeric/valarray/dsc atan2 | (see dedicated page) |

#### Hyperbolic functions

| cpp/numeric/valarray/dsc sinh | (see dedicated page) |
| cpp/numeric/valarray/dsc cosh | (see dedicated page) |
| cpp/numeric/valarray/dsc tanh | (see dedicated page) |


## Helper classes


| cpp/numeric/valarray/dsc slice | (see dedicated page) |
| cpp/numeric/valarray/dsc slice_array | (see dedicated page) |
| cpp/numeric/valarray/dsc gslice | (see dedicated page) |
| cpp/numeric/valarray/dsc gslice_array | (see dedicated page) |
| cpp/numeric/valarray/dsc mask_array | (see dedicated page) |
| cpp/numeric/valarray/dsc indirect_array | (see dedicated page) |


## Deduction guides<sup>(C++17)</sup>


## Notes

`std::valarray` and helper classes are defined to be free of certain forms of aliasing, thus allowing operations on these classes to be optimized similar to the effect of the keyword `c/language/restrict` in the C programming language. In addition, functions and operators that take `valarray` arguments are allowed to return proxy objects to make it possible for the compiler to optimize an expression such as `1=v1 = a * v2 + v3;` as a single loop that executes `1=v1[i] = a * v2[i] + v3[i];` avoiding any temporaries or multiple passes. However, [expression templates](https://en.wikipedia.org/wiki/expression templates) make the same optimization technique available for any C++ container, and the majority of numeric libraries prefer expression templates to valarrays for flexibility. Some C++ standard library implementations use expression templates to implement efficient operations on `std::valarray` (e.g. GNU libstdc++ and LLVM libc++). Only rarely are valarrays optimized any further, as in e.g. [https://software.intel.com/en-us/node/684140 Intel Integrated Performance Primitives].

## Defect reports


## See also


| cpp/numeric/simd/dsc basic_vec | (see dedicated page) |
| cpp/numeric/simd/dsc vec | (see dedicated page) |
| cpp/numeric/simd/dsc basic_mask | (see dedicated page) |
| cpp/numeric/simd/dsc mask | (see dedicated page) |


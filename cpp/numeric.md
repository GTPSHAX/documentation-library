---
title: Numerics library
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric
---


# Numerics library

The C++ numerics library includes common mathematical functions and types, as well as optimized numeric arrays and support for random number generation.

# Mathematical functions and types


## Common mathematical functions

The header  provides standard C library mathematical functions such as `std::fabs`, `std::sqrt`, and `std::sin`.

## Mathematical special functions <sup>(C++17)</sup>

The header  also provides several mathematical special functions such as `std::beta`, `std::hermite`, and `std::cyl_bessel_i`.

## Mathematical constants <sup>(C++20)</sup>

The header  provides several mathematical constants, such as `std::numbers::pi` or `std::numbers::sqrt2`

## Basic linear algebra algorithms <sup>(C++26)</sup>

The header  provides basic linear algebra algorithms which are based on BLAS.

## Data-parallel types <sup>(C++26)</sup>

The header  provides portable types for explicitly stating data-parallelism and structuring data for more efficient SIMD access.

## Complex number arithmetic


| complex | |
| cpp/numeric/complex|a complex number type | |


## Numeric arrays


| valarray | |
| cpp/numeric/valarray|numeric arrays, array masks and array slices | |


# Numeric algorithms

The header  provides numeric algorithms below:

## Factor operations <sup>(C++17)</sup>


| numeric | |
| cpp/numeric/dsc gcd | (see dedicated page) |
| cpp/numeric/dsc lcm | (see dedicated page) |


## Interpolation operations


| numeric | |
| cpp/numeric/dsc midpoint | (see dedicated page) |
| cmath | |
| cpp/numeric/dsc lerp | (see dedicated page) |


## Saturation arithmetic <sup>(C++26)</sup>


| numeric | |
| cpp/numeric/dsc saturating_add | (see dedicated page) |
| cpp/numeric/dsc saturating_sub | (see dedicated page) |
| cpp/numeric/dsc saturating_mul | (see dedicated page) |
| cpp/numeric/dsc saturating_div | (see dedicated page) |
| cpp/numeric/dsc saturating_cast | (see dedicated page) |


## Numeric operations


| numeric | |
| cpp/algorithm/dsc iota | (see dedicated page) |
| cpp/algorithm/ranges/dsc iota | (see dedicated page) |
| cpp/algorithm/dsc accumulate | (see dedicated page) |
| cpp/algorithm/ranges/dsc accumulate | (see dedicated page) |
| cpp/algorithm/dsc reduce | (see dedicated page) |
| cpp/algorithm/ranges/dsc reduce | (see dedicated page) |
| cpp/algorithm/dsc transform_reduce | (see dedicated page) |
| cpp/algorithm/ranges/dsc transform_reduce | (see dedicated page) |
| cpp/algorithm/dsc inner_product | (see dedicated page) |
| cpp/algorithm/ranges/dsc inner_product | (see dedicated page) |
| cpp/algorithm/dsc adjacent_difference | (see dedicated page) |
| cpp/algorithm/ranges/dsc adjacent_difference | (see dedicated page) |
| cpp/algorithm/dsc partial_sum | (see dedicated page) |
| cpp/algorithm/ranges/dsc partial_sum | (see dedicated page) |
| cpp/algorithm/dsc inclusive_scan | (see dedicated page) |
| cpp/algorithm/ranges/dsc inclusive_scan | (see dedicated page) |
| cpp/algorithm/dsc exclusive_scan | (see dedicated page) |
| cpp/algorithm/ranges/dsc exclusive_scan | (see dedicated page) |
| cpp/algorithm/dsc transform_inclusive_scan | (see dedicated page) |
| cpp/algorithm/ranges/dsc transform_inclusive_scan | (see dedicated page) |
| cpp/algorithm/dsc transform_exclusive_scan | (see dedicated page) |
| cpp/algorithm/ranges/dsc transform_exclusive_scan | (see dedicated page) |


# Miscellaneous


## Pseudo-random number generation

The header  defines pseudo-random number generators and numerical distributions. The header  also includes C-style random number generation via `std::srand` and `std::rand`.

## Floating-point environment <sup>(C++11)</sup>

The header  defines flags and functions related to exceptional floating-point state, such as overflow and division by zero.

## Bit manipulation <sup>(C++20)</sup>

The header  provides several function templates to access, manipulate, and process individual bits and bit sequences. The byte ordering (endianness) of scalar types can be inspected via `std::endian` facility.

## Checked integer arithmetic <sup>(C++26)</sup>

The C compatibility header  provides several function templates for checked integer arithmetic.


| stdckdint.h | |
| cpp/numeric/dsc ckd_add | (see dedicated page) |
| cpp/numeric/dsc ckd_sub | (see dedicated page) |
| cpp/numeric/dsc ckd_mul | (see dedicated page) |


## See also


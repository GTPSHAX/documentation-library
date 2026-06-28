---
title: Compile-time rational arithmetic
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/numeric/ratio
---


# Compile-time rational arithmetic mark since c++11

The class template `std::ratio` and associated templates provide compile-time rational arithmetic support. Each instantiation of this template exactly represents any finite rational number.

## Compile-time fractions


| ratio | |
| cpp/numeric/ratio/dsc ratio | (see dedicated page) |


## Compile-time rational arithmetic

Several alias templates, that perform arithmetic operations on `ratio` objects at compile-time are provided.


| ratio | |
| cpp/numeric/ratio/dsc ratio_add | (see dedicated page) |
| cpp/numeric/ratio/dsc ratio_subtract | (see dedicated page) |
| cpp/numeric/ratio/dsc ratio_multiply | (see dedicated page) |
| cpp/numeric/ratio/dsc ratio_divide | (see dedicated page) |


## Compile-time rational comparison

Several class templates, that perform comparison operations on `ratio` objects at compile-time are provided.


| ratio | |
| cpp/numeric/ratio/dsc ratio_equal | (see dedicated page) |
| cpp/numeric/ratio/dsc ratio_not_equal | (see dedicated page) |
| cpp/numeric/ratio/dsc ratio_less | (see dedicated page) |
| cpp/numeric/ratio/dsc ratio_less_equal | (see dedicated page) |
| cpp/numeric/ratio/dsc ratio_greater | (see dedicated page) |
| cpp/numeric/ratio/dsc ratio_greater_equal | (see dedicated page) |


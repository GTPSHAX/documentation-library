---
title: deduction guides for std::extents
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/extents/deduction_guides
---


# deduction guides for tt|std::extents

ddcl|header=mdspan|since=c++23|1=
template< class... Integrals >
explicit extents( Integrals... ) -> /* see below */;
A deduction guide is provided for `std::extents` to allow deduction from integral arguments.
The deduced type is equivalent to rrev multi|until1=c++26
|rev1=`std::dextents<std::size_t, sizeof...(Integrals)>`
|rev2=
.

## Example


## See also


| cpp/container/mdspan/extents/dsc constructor | (see dedicated page) |


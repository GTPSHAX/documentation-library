---
title: std::domain_error
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/domain_error
---

ddcl|header=stdexcept|
class domain_error;
Defines a type of object to be thrown as exception. It may be used by the implementation to report domain errors, that is, situations where the inputs are outside of the domain on which an operation is defined.
The standard library components do not throw this exception (mathematical functions report domain errors as specified in `math_errhandling`). Third-party libraries, however, use this. For example, [https://www.boost.org/doc/libs/1_55_0/libs/math/doc/html/math_toolkit/error_handling.html boost.math] throws `std::domain_error` if `boost::math::policies::throw_on_error` is enabled (the default setting).

## Member functions


## Defect reports


---
title: std::underflow_error
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/underflow_error
---

ddcl|header=stdexcept|
class underflow_error;
Defines a type of object to be thrown as exception. It may be used to report arithmetic underflow errors (that is, situations where the result of a computation is a subnormal floating-point value).
The standard library components do not throw this exception (mathematical functions report underflow errors as specified in `math_errhandling`). Third-party libraries, however, use this. For example, [https://www.boost.org/doc/libs/1_66_0/libs/math/doc/html/math_toolkit/error_handling.html boost.math] throws `std::underflow_error` if `boost::math::policies::throw_on_error` is enabled (the default setting).

## Member functions


## Defect reports


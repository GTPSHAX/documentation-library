---
title: std::range_error
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/range_error
---

ddcl|header=stdexcept|
class range_error;
Defines a type of object to be thrown as exception. It can be used to report range errors (that is, situations where a result of a computation cannot be represented by the destination type).
The only standard library components that throw this exception are `std::wstring_convert::from_bytes` and `std::wstring_convert::to_bytes`.
The mathematical functions in the standard library components do not throw this exception (mathematical functions report range errors as specified in `math_errhandling`).

## Member functions


## Defect reports


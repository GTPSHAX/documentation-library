---
title: std::logic_error
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/logic_error
---

ddcl|header=stdexcept|
class logic_error;
Defines a type of object to be thrown as exception. It reports errors that are a consequence of faulty logic within the program such as violating logical preconditions or class invariants and may be preventable.
No standard library components throw this exception directly, but the exception types
`std::invalid_argument`, `std::domain_error`, `std::length_error`, `std::out_of_range`, `std::future_error`, and `cpp/experimental/optional/bad_optional_access|std::experimental::bad_optional_access` are derived from `std::logic_error`.

## Member functions


## Defect reports


---
title: std::move_only_function::operator()
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/move_only_function/operator()
---

ddcl | since=c++23 |
R operator()( Args... args ) /*cv*/ /*ref*/ noexcept(/*noex*/);
Invokes the stored callable target with the parameters `args`. The `/*cv*/`, `/*ref*/`, and `/*noex*/` parts of `operator()` are identical to those of the template parameter of `std::move_only_function`.
Equivalent to `return std::invoke_r<R>(/*cv-ref-cast*/(f), std::forward<Args>(args)...);`, where `f` is a cv-unqualified lvalue that denotes the target object of `*this`, and `/*cv-ref-cast*/(f)` is equivalent to:
* `f` if *cv* *ref* is either empty or `&`, or
* `std::as_const(f)` if *cv* *ref* is either `const` or `const &`, or
* `std::move(f)` if *cv* *ref* is `&&`, or
* `std::move(std::as_const(f))` if *cv* *ref* is `const &&`.
The behavior is undefined if `*this` is empty.

## Parameters


### Parameters


## Return value

`std::invoke_r<R>(/*cv-ref-cast*/(f), std::forward<Args>(args)...)`.

## Exceptions

Propagates the exception thrown by the underlying function call.

## Example


## See also


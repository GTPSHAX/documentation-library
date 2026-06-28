---
title: std::predicate
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/predicate
---

ddcl|header=concepts|since=c++20|1=
template< class F, class... Args >
concept predicate =
std::regular_invocable<F, Args...> &&
boolean-testable<std::invoke_result_t<F, Args...>>;
The concept  specifies that `F` is a predicate that accepts arguments whose types and value categories are encoded by `Args...`, i.e., it can be invoked with these arguments to produce a  result.
Note that  requires the invocation to not modify either the callable object or the arguments and be equality-preserving.

## References


---
title: boolean-testable
type: Concepts
source: https://en.cppreference.com/w/cpp/concepts/boolean-testable
---


# ''boolean-testable''


```cpp
dcla|anchor=no|num=1|since=c++20|expos=yes|1=
template< class B >
concept __boolean_testable_impl = std::convertible_to<B, bool>;
dcla|anchor=no|num=2|since=c++20|expos=yes|1=
template< class B >
concept boolean-testable =
__boolean_testable_impl<B> &&
requires (B&& b) {
{ !std::forward<B>(b) } -> __boolean_testable_impl;
};
```

The exposition-only concept  specifies the requirements for expressions that are convertible to `bool` and for which the logical operators have the usual behavior (including [Short-circuit evaluation|short-circuiting](https://en.wikipedia.org/wiki/Short-circuit evaluation|short-circuiting)), even for two different  types.
Formally, to model the exposition-only concept , the type must not define any member `operator&&` and `operator, and no viable non-member `operator&&` and `operator may be visible by argument-dependent lookup. Additionally, given an expression `e` such that `decltype((e))` is `B`,  is modeled only if `1=bool(e) == !bool(!e)`.

## Notes

Examples of  types include `bool`, `std::true_type`, `std::bitset<N>::``cpp/utility/bitset/reference`, and `int*`.

## References


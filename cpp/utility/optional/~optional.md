---
title: std::optional::~optional
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/optional/~optional
---

ddcl|since=c++17|notes=<sup>(constexpr C++20)</sup>|
~optional();
If the object contains a value and the type `T` is not trivially destructible (see `std::is_trivially_destructible`), destroys the contained value by calling its destructor, as if by `value().T::~T()`.
Otherwise, does nothing.

## Notes

If `T` is trivially-destructible, then this destructor is also trivial, so `std::optional<T>` is also trivially-destructible.

## Defect reports


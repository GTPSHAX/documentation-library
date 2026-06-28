---
title: std::nullopt_t
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/optional/nullopt_t
---


```cpp
dcl | since=c++17 |1=
struct nullopt_t;
```

`std::nullopt_t` is an empty class type used to indicate that an `std::optional` does not contain a value.
`std::nullopt_t` is a non-aggregate *LiteralType* that has no default constructor, no initializer-list constructor, but does have a `constexpr` constructor that takes an implementation-defined literal type.

## Notes

The constraints on `nullopt_t`'s constructors exist to support both } and `1=op = nullopt;` as the syntax for disengaging an optional object.
A possible implementation of this class is

```cpp
struct nullopt_t {
    constexpr explicit nullopt_t(int) {}
};
```


## See also


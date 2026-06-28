---
title: std::ranges::adjacent_view::sentinel<Const>::sentinel
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_view/sentinel/sentinel
---


```cpp
dcl|num=1|since=c++23|1=
/*sentinel*/() = default;
dcl|num=2|since=c++23|1=
constexpr /*sentinel*/( /*sentinel*/<!Const> i )
requires Const &&
std::convertible_to<ranges::sentinel_t<V>, ranges::sentinel_t<Base>>;
```

Constructs a sentinel.
1. Default constructor. Value-initializes the underlying sentinel (denoted as ) with `ranges::sentinel_t<Base>()`.
2. Conversion from `/*sentinel*/<false>` to `/*sentinel*/<true>`. Move constructs the underlying sentinel  with the corresponding member of `i`.
This type also has a private constructor which is used by `ranges::adjacent_view::end|adjacent_view::end`. This constructor is not accessible to users.

## Parameters


### Parameters

- `i` - a `/*sentinel*/<false>`

## Example


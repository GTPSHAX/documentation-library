---
title: std::ranges::enumerate_view::sentinel<Const>::sentinel
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/enumerate_view/sentinel/sentinel
---


```cpp
dcl|num=1|since=c++23|1=
/*sentinel*/() = default;
dcl|num=2|since=c++23|1=
constexpr /*sentinel*/( /*sentinel*/<!Const> i )
requires Const &&
std::convertible_to<ranges::sentinel_t<V>, ranges::sentinel_t<Base>>;
|1=
private:
constexpr explicit /*sentinel*/( ranges::sentinel_t<Base> end );
```

Constructs a `sentinel`.
1. Default constructor. Value-initializes the underlying sentinel with `ranges::sentinel_t<Base>()`.
2. Conversion from `/*sentinel*/<false>` to `/*sentinel*/<true>`. Move constructs the underlying sentinel  with `std::move(other.end_)`.
3. A private constructor which is used by `enumerate_view::end`. Move constructs the  with `std::move(end)` This constructor is not accessible to users.

## Parameters


### Parameters

- `i` - a `/*sentinel*/<false>`

## Example


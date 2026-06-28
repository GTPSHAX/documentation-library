---
title: std::ranges::elements_view::sentinel<Const>::sentinel
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/elements_view/sentinel/sentinel
---


```cpp
dcl | num=1 | since=c++20 |1=
/*sentinel*/() = default;
dcl | num=2 | since=c++20 |
constexpr explicit /*sentinel*/( ranges::sentinel_t<Base> end );
dcl | num=3 | since=c++20 |
constexpr /*sentinel*/( /*sentinel*/<!Const> i )
requires Const && std::convertible_to<ranges::sentinel_t<V>,
ranges::sentinel_t<Base>>;
```

Constructs a sentinel.
1. Default constructor. Value-initializes the underlying sentinel.
2. Initializes the underlying sentinel with `end`.
3. Conversion from `/*sentinel*/<false>` to `/*sentinel*/<true>`. Move constructs the underlying sentinel.

## Parameters


### Parameters


## Example


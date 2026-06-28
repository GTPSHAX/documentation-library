---
title: std::ranges::zip_view::sentinel<Const>::sentinel
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_view/sentinel/sentinel
---


```cpp
dcl|num=1|since=c++23|1=
/*sentinel*/() = default;
dcl|num=2|since=c++23|1=
constexpr /*sentinel*/( /*sentinel*/<!Const> i )
requires Const &&
(std::convertible_to<
ranges::sentinel_t<Views>,
ranges::sentinel_t</*maybe-const*/<Const, Views>>> && ...);
```

Constructs a sentinel.
1. Default constructor. Value-initializes the underlying tuple of sentinels .
2. Conversion from `/*sentinel*/<false>` to `/*sentinel*/<true>`. Move constructs the underlying tuple of sentinels  with `std::move(i.end_)`.

## Parameters


### Parameters

- `i` - a `/*sentinel*/<false>`

## Example


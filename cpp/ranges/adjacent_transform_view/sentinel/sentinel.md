---
title: std::ranges::adjacent_transform_view::sentinel<Const>::sentinel
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_transform_view/sentinel/sentinel
---


```cpp
dcl|num=1|since=c++23|1=
/*sentinel*/() = default;
dcl|num=2|since=c++23|1=
constexpr /*sentinel*/( /*sentinel*/<!Const> i )
requires Const &&
std::convertible_to</*inner-sentinel*/<false>, /*inner-sentinel*/<Const>>;
|1=
private:
constexpr explicit /*sentinel*/( /*inner-sentinel*/<Const> inner );
```

Construct a sentinel.
1. Default constructor. Default-initializes the underlying sentinel .
2. Conversion from `/*sentinel*/<false>` to `/*sentinel*/<true>`. Move constructs the underlying sentinel  with .
3. This sentinel also has a private constructor which is used by `ranges::adjacent_transform_view::end`. This constructor is not accessible to users. Initializes the underlying sentinel  with `inner`.

## Parameters


### Parameters

- `i` - an `/*sentinel*/<false>`
- `inner` - a sentinel of type `ranges::adjacent_transform_view|adjacent_transform_view::`

## Example


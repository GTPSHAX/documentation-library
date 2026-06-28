---
title: std::ranges::zip_transform_view::sentinel<Const>::sentinel
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_transform_view/sentinel/sentinel
---


```cpp
dcl|num=1|since=c++23|1=
/*sentinel*/() = default;
dcl|num=2|since=c++23|1=
constexpr /*sentinel*/( /*sentinel*/<!Const> i )
requires Const &&
std::convertible_to</*zentinel*/<false>, /*zentinel*/<Const>>;
|1=
constexpr explicit /*sentinel*/( /*zentinel*/<Const> inner );
```

Constructs a sentinel.
1. Default constructor. Default-initializes the underlying sentinel object .
2. Conversion from `/*sentinel*/<false>` to `/*sentinel*/<true>`. Move constructs the underlying object  with `1=std::move(i.inner_)`.
3. Value-initializes the underlying object  with `inner`. This constructor is not accessible to users.

## Parameters


### Parameters

- `i` - a `/*sentinel*/<false>`
- `inner` - an underlying object of type `<Const>`

## Example


---
title: std::ranges::join_view::sentinel<Const>::sentinel
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_view/sentinel/sentinel
---


```cpp
dcl|num=1|since=c++20|1=
/*sentinel*/() = default;
dcl|num=2|since=c++20|1=
constexpr explicit /*sentinel*/( Parent& parent );
dcl|num=3|since=c++20|1=
constexpr /*sentinel*/( /*sentinel*/<!Const> i )
requires Const &&
std::convertible_to<ranges::sentinel_t<V>, ranges::sentinel_t<Base>>;
```

Constructs a sentinel.
1. Default constructor. Value-initializes the underlying sentinel.
2. Initializes the underlying sentinel  with `1=ranges::end(parent.base_)`.
3. Conversion from `/*sentinel*/<false>` to `/*sentinel*/<true>`. Move constructs the underlying sentinel  with `1=std::move(i.end_)`.

## Parameters


### Parameters

- `parent` - a (possibly const-qualified) `ranges::join_view`
- `i` - a `/*sentinel*/<false>`

## Example


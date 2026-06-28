---
title: std::ranges::take_while_view::sentinel<Const>::sentinel
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/take_while_view/sentinel/sentinel
---


```cpp
dcl|num=1|since=c++20|1=
/*sentinel*/() = default;
dcl|num=2|since=c++20|1=
constexpr explicit /*sentinel*/( ranges::sentinel_t<Base> end, const Pred* pred );
dcl|num=3|since=c++20|1=
constexpr /*sentinel*/( /*sentinel*/<!Const> s )
requires Const &&
std::convertible_to<ranges::sentinel_t<V>, ranges::sentinel_t<Base>>;
```

Constructs a sentinel.
1. Default constructor. Value-initializes the underlying sentinel and the pointer to predicate.
2. Initializes the underlying sentinel with `end` and the pointer to predicate with `pred`.
3. Conversion from `/*sentinel*/<false>` to `/*sentinel*/<true>`. Copy constructs corresponding members.

## Parameters


### Parameters

- `end` - a sentinel representing the end of (possibly const-qualified) `V`
- `pred` - a pointer to predicate
- `i` - a `/*sentinel*/<false>`

## Example


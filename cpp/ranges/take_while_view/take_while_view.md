---
title: std::ranges::take_while_view::take_while_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/take_while_view/take_while_view
---


```cpp
dcl|num=1|since=c++20|1=
take_while_view() requires std::default_initializable<V> &&
std::default_initializable<Pred> = default;
dcl|num=2|since=c++20|1=
constexpr explicit take_while_view( V base, Pred pred );
```

Constructs a `take_while_view`.
1. Default constructor. Value-initializes the underlying view and the predicate.
2. Move constructs the underlying view  from `base` and the predicate  from `pred`.

## Parameters


### Parameters

- `base` - underlying view
- `fun` - predicate

## Example


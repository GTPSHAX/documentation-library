---
title: std::ranges::lazy_split_view::lazy_split_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/lazy_split_view/lazy_split_view
---


```cpp
dcl|num=1|since=c++20|1=
lazy_split_view()
requires std::default_initializable<V> &&
std::default_initializable<Pattern> = default;
dcla|num=2|since=c++20|1=
constexpr explicit lazy_split_view( V base, Pattern pattern );
dcl|num=3|since=c++20|1=
template< ranges::input_range R >
requires std::constructible_from<V, views::all_t<R>> &&
std::constructible_from<Pattern, ranges::single_view<
ranges::range_value_t<R>>>
constexpr explicit lazy_split_view( R&& r, ranges::range_value_t<R> e );
```

Constructs a `lazy_split_view`.
1. Default constructor. Value-initializes the underlying view  and the delimiter .
2. Initializes the underlying view  with `std::move(base)` and the delimiter  with `std::move(pattern)`.
3. Initializes the underlying view  with `views::all(std::forward<R>(r))` and the delimiter  with }.

## Parameters


### Parameters

- `base` - the underlying view to be split
- `pattern` - a view to be used as the delimiter
- `e` - an element to be used as the delimiter

## Example


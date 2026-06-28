---
title: Vs...>::iterator::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/cartesian_product_view/iterator/iterator
---


```cpp
dcl|num=1|since=c++23|1=
/*iterator*/() = default;
dcl|num=2|since=c++23|1=
constexpr /*iterator*/( /*iterator*/<!Const> i )
requires Const && (
std::convertible_to<ranges::iterator_t<First>, ranges::iterator_t<const First>>
&& ... &&
std::convertible_to<ranges::iterator_t<Vs>, ranges::iterator_t<const Vs>>
);
|1=
private:
constexpr /*iterator*/(
/*Parent*/& parent,
std::tuple<ranges::iterator_t</*maybe-const*/<Const, First>>,
ranges::iterator_t</*maybe-const*/<Const, Vs>>...> current );
```

Construct an iterator.
1. Default constructor. Value-initializes the  with `nullptr` and default-initializes the .
2. Conversion from `/*iterator*/<false>` to `/*iterator*/<true>`. Initializes  with  and  with `std::move(i.current_)`.
3. A private constructor which is used by `cartesian_product_view::begin` and `cartesian_product_view::end`. This constructor is not accessible to users.
Initializes  with `std::addressof(parent)` and  with `std::move(current)`.

## Parameters


### Parameters

- `i` - an `/*iterator*/<false>`

## Example


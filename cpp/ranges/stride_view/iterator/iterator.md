---
title: std::ranges::stride_view::iterator<Const>::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/stride_view/iterator/iterator
---


```cpp
dcl|num=1|since=c++23|1=
/*iterator*/()
requires std::default_initializable<ranges::iterator_t<Base>> = default;
dcl|num=2|since=c++23|1=
constexpr /*iterator*/( /*iterator*/<!Const> i )
requires Const and
std::convertible_to<ranges::iterator_t<V>, ranges::iterator_t<Base>> and
std::convertible_to<ranges::sentinel_t<V>, ranges::sentinel_t<Base>>;
|1=
private:
constexpr /*iterator*/( /*Parent*/& parent,
ranges::iterator_t<Base> current,
ranges::range_difference_t<Base> missing = 0 );
```

Constructs an `iterator`.
1. Default constructor. Value-initializes:
*  with `ranges::iterator_t<Base>()`,
*  with `ranges::sentinel_t<Base>()`,
*  with `0`,
*  with `0`.
2. Conversion from `/*iterator*/<false>` to `/*iterator*/<true>`. Initializes:
*  with `std::move(i.current_)`,
*  with `std::move(i.end_)`,
*  with `i.stride_`,
*  with `i.missing_`.
3. A private constructor which is used by `stride_view::begin` and `stride_view::end`. This constructor is not accessible to users. Initializes
*  with `std::move(current)`,
*  with `ranges::end(parent->base_)`,
*  with `parent->stride_`,
*  with `missing`.

## Parameters


### Parameters

- `i` - an `/*iterator*/<false>`

## Example


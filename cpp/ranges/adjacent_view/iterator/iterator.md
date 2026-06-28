---
title: std::ranges::adjacent_view::iterator<Const>::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_view/iterator/iterator
---


```cpp
dcl|num=1|since=c++23|1=
/*iterator*/() = default;
dcl|num=2|since=c++23|1=
constexpr /*iterator*/( /*iterator*/<!Const> i )
requires Const &&
ranges::convertible_to<ranges::iterator_t<V>, ranges::iterator_t<Base>>;
```

Construct an iterator.
1. Default constructor. Value-initializes the underlying array of iterators `''current_''` to `''Base''`, as if by `std::array<ranges::iterator_t<Base>, N>()`.
2. Conversion from `/*iterator*/<false>` to `/*iterator*/<true>`. Move constructs the underlying `''current_''` member.
This iterator also has two private constructors which is used by `ranges::adjacent_view::begin` and `ranges::adjacent_view::end`. These constructors are not accessible to users.

## Parameters


### Parameters

- `i` - an `/*iterator*/<false>`

## Example


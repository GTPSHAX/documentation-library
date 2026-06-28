---
title: std::ranges::adjacent_transform_view::iterator<Const>::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_transform_view/iterator/iterator
---


```cpp
dcl|num=1|since=c++23|1=
/*iterator*/() = default;
dcl|num=2|since=c++23|1=
constexpr /*iterator*/( /*iterator*/<!Const> i )
requires Const &&
std::convertible_to</*inner-iterator*/<false>, /*inner-iterator*/<Const>>;
|1=
private:
constexpr /*iterator*/( Parent& parent, /*inner-iterator*/<Const> inner );
```

Construct an iterator.
1. Default constructor. Value-initializes the underlying pointer  with `nullptr`, and default-initializes the underlying iterator .
2. Conversion from `/*iterator*/<false>` to `/*iterator*/<true>`. Initializes the underlying pointer  with `i.parent_`, and move constructs the underlying iterator  with .
3. This iterator also has a private constructor which is used by `ranges::adjacent_transform_view::begin` and `ranges::adjacent_transform_view::end`. This constructor is not accessible to users. Initializes  with `std::addressof(parent)`, and move constructs  with `std::move(inner)`.

## Parameters


### Parameters

- `i` - an `/*iterator*/<false>`
- `parent` - an owning object of type `ranges::adjacent_transform_view|adjacent_transform_view`
- `inner` - an iterator of type `ranges::adjacent_transform_view|adjacent_transform_view::``cpp/ranges/adjacent_transform_view#Member types|''inner_iterator''`

## Example


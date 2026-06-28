---
title: std::ranges::zip_transform_view::iterator<Const>::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_transform_view/iterator/iterator
---


```cpp
dcl|num=1|since=c++23|1=
/*iterator*/iterator() = default;
dcl|num=2|since=c++23|1=
constexpr /*iterator*/( /*iterator*/<!Const> i )
requires Const &&
std::convertible_to</*ziperator*/<false>, /*ziperator*/<Const>>;
|1=
constexpr /*iterator*/( Parent& parent, /*ziperator*/<Const> inner );
```

Construct an iterator.
1. Default constructor. Default-initializes the underlying iterators, and value-initializes the pointer to parent `ranges::zip_transform_view` with `nullptr`.
2. Conversion from `/*iterator*/<false>` to `/*iterator*/<true>`. Move constructs the underlying pointer to parent  with `i.parent_` and  with `std::move(i.inner_)`.
3. Initializes the pointer to parent  with `std::addressof(parent)`, and the underlying  iterator with `std::move(inner)`. This constructor is not accessible to users.

## Parameters


### Parameters

- `i` - an `/*iterator*/<false>`
- `parent` - a (possibly const-qualified) `ranges::zip_transform_view`
- `inner` - an iterator of type `<Const>`

## Example


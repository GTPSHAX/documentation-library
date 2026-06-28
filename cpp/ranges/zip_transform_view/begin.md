---
title: std::ranges::zip_transform_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_transform_view/begin
---


```cpp
dcl | num=1 | since=c++23 |1=
constexpr auto begin();
dcl | num=2 | since=c++23 |1=
constexpr auto begin() const
requires ranges::range<const ranges::zip_view<Views...>>;
```

Obtains the beginning iterator of `zip_transform_view`.
1. Equivalent to `return /*iterator*/<false>(*this, zip_.begin());`.
2. Equivalent to `return /*iterator*/<true>(*this, zip_.begin());`.

## Parameters

(none)

## Return value

`Iterator` to the first element.

## Notes

`ranges::range<const ranges::zip_view<Views...>>` is modeled if and only if for every type `Vi` in `Views...`, `const Vi` models .

## Example


---
title: std::ranges::zip_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_view/begin
---


```cpp
dcl|num=1|since=c++23|1=
constexpr auto begin()
requires (!(/*simple-view*/<Views> && ...));
dcl|num=2|since=c++23|1=
constexpr auto begin() const
requires (ranges::range<const Views> && ...);
```

Obtains the beginning `iterator` of `zip_view`.

## Return value

1. .
2. .

## Notes

`ranges::range<const ranges::zip_view<Views...>>` is modeled if and only if for every type `Vi` in `Views...`, `const Vi` models .

## Example


---
title: std::ranges::join_with_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/join_with_view/begin
---


```cpp
dcl|num=1|since=c++23|
constexpr auto begin();
dcl|num=2|since=c++23|
constexpr auto begin() const
requires ranges::forward_range<const V> &&
ranges::forward_range<const Pattern> &&
std::is_reference_v<ranges::range_reference_t<const V>> &&
ranges::input_range<ranges::range_reference_t<const V>> &&
/*concatable*/<ranges::range_reference_t<const V>,
const Pattern>;
```

Returns an `iterator` to the beginning of the `join_with_view`.
1. Returns a mutable iterator or const iterator.
* If `V` models , equivalent to box|`1=constexpr bool use_const =`<br>`<V> && std::is_reference_v<``> &&``<Pattern>;`<br>`return``<use_const>{*this, ranges::begin(`c/core|)};.
* Otherwise, equivalent to box|`1== ranges::begin(``);`<br>`return`}.
2. Returns a const iterator.
@@ For the definition of , see .

## Return value

1. As described above.
2. }.

## Example


---
title: std::ranges::chunk_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/begin
---


```cpp
dcl|num=1|since=c++23|
constexpr /*outer_iterator*/ begin();
dcl|num=2|since=c++23|
constexpr auto begin() requires (!/*simple_view*/<V>);
dcl|num=3|since=c++23|
constexpr auto begin() const requires ranges::forward_range<const V>;
```

Returns an `iterator` to the first element of the `chunk_view`.
1. Available only if `V` models . Equivalent to
box|
`1== ranges::begin(``);`<br>
`1==``;`<br>
`return``(*this);`
2. Available if `V` models . Equivalent to
.
3. Available if `V` models . Equivalent to
.

## Return value

An iterator to the first element of the `chunk_view`, as described above.

## Example


## See also


| cpp/ranges/adaptor/dsc end|chunk_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |


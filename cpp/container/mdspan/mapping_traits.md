---
title: std::mdspan::is_always_exhaustive
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/mapping_traits
---


```cpp
dcl|num=1|since=c++23|
constexpr bool is_unique() const;
dcl|num=2|since=c++23|
constexpr bool is_exhaustive() const;
dcl|num=3|since=c++23|
constexpr bool is_strided() const;
dcl|num=4|since=c++23|
static constexpr bool is_always_unique();
dcl|num=5|since=c++23|
static constexpr bool is_always_exhaustive();
dcl|num=6|since=c++23|
static constexpr bool is_always_strided();
```

Checks if  the underlying layout mapping `''map_''` or  its type `mapping_type` models the semantics of *LayoutMapping*'s predicate mapping traits.
@1-3@ Let `''func''` be  `is_unique`,  `is_exhaustive`, or  `is_strided`, then it's equivalent to `return map_.func();`.
@4-6@ Let `''func''` be  `is_always_unique`,  `is_always_exhaustive`, or  `is_always_strided`, then it's equivalent to `return mapping_type::func();`.

## Parameters

(none)

## Return value

See above.

## Example


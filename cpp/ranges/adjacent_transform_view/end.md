---
title: std::ranges::adjacent_transform_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_transform_view/end
---


```cpp
dcl|num=1|since=c++23|1=
constexpr auto end();
dcl|num=2|since=c++23|1=
constexpr auto end() const
requires ranges::range<const InnerView> &&
std::regular_invocable<const F&,
/*REPEAT*/(ranges::range_reference_t<const V>, N)...>;
```

Returns an `iterator` or a `sentinel` representing the end of the `adjacent_transform_view`.
Let  be the underlying `ranges::adjacent_view`.
1. Equivalent to:

```cpp
if constexpr (ranges::common_range<InnerView>)
    return /*iterator*/<false>(*this, inner_.end());
else
    return /*sentinel*/<false>(inner_.end());
```

2. Equivalent to:

```cpp
if constexpr (ranges::common_range<const InnerView>)
    return /*iterator*/<true>(*this, inner_.end());
else
    return /*sentinel*/<true>(inner_.end());
```


## Parameters

(none)

## Return value

An `iterator` to the element following the last element, if the underlying view `V` models . Otherwise, a `sentinel` which compares equal to the end iterator.

## Notes

`adjacent_transform_view<V,F,N>` models  whenever the underlying view `V` does.

## Example


## See also


| cpp/ranges/adaptor/dsc begin|adjacent_transform_view | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |


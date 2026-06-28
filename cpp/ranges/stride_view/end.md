---
title: std::ranges::stride_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/stride_view/end
---


```cpp
dcl|num=1|since=c++23|1=
constexpr auto end() requires (!/*simple-view*/<V>);
dcl|num=2|since=c++23|1=
constexpr auto end() const requires ranges::range<const V>
```

Returns an `iterator` or a `sentinel` representing the end of the `stride_view`.
Let  and  be the underlying data members.
1. Let `Const` be defined as `1=using Const = false;` and `Base` as `1=using Base = V;`.
2. Let `Const` be defined as `1=using Const = true;` and `Base` as `1=using Base = const V;`.
Equivalent to:

```cpp
if constexpr (ranges::common_range<Base> &&
              ranges::sized_range<Base> &&
              ranges::forward_range<Base>)
{
    auto missing = (stride_ - ranges::distance(base_) % stride_) % stride_;
    return iterator<Const>(this, ranges::end(base_), missing);
}
else if constexpr (ranges::common_range<Base> &&
                   !ranges::bidirectional_range<Base>)
{
    return iterator<Const>(this, ranges::end(base_));
}
else
{
    return std::default_sentinel;
}
```


## Parameters

(none)

## Return value

An `iterator` to the element following the last element, if the underlying view `V` models . Otherwise, the `std::default_sentinel` which compares equal to the end iterator.

## Notes

`stride_view<V>` models  whenever the underlying view `V` does.

## Example


## See also


| cpp/ranges/adaptor/dsc begin|stride_view | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |


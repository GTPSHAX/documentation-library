---
title: std::ranges::chunk_by_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_by_view/end
---

ddcl|since=c++23|
constexpr auto end();
Returns an `iterator` or a  representing the end of the `chunk_by_view`.
Equivalent to:

```cpp
if constexpr (ranges::common_range<V>)
    return /*iterator*/(*this, ranges::end(base_), ranges::end(base_));
else
    return std::default_sentinel;
```


## Parameters

(none)

## Return value

An `iterator` to the element following the last element, or a sentinel which compares equal to the end iterator.

## Notes

`end()` returns an iterator if and only if the underlying view is a : `chunk_by_view<V,Pred>` models  whenever `V` does.

## Example


## See also


| cpp/ranges/adaptor/dsc begin|chunk_by_view | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |


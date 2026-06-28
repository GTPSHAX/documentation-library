---
title: std::ranges::elements_view::size
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/elements_view/size
---


```cpp
dcl|since=c++20|
constexpr auto size() requires ranges::sized_range<V>;
dcl|since=c++20|
constexpr auto size() const requires ranges::sized_range<const V>;
```

Returns the number of elements, i.e. `ranges::size(base_)`, where  is the underlying view.

## Parameters

(none)

## Return value

The number of elements.

## Example


## See also


| cpp/ranges/dsc size | (see dedicated page) |
| cpp/ranges/dsc ssize | (see dedicated page) |


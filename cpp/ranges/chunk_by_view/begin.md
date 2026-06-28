---
title: std::ranges::chunk_by_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_by_view/begin
---

ddcl|since=c++23|1=
constexpr /*iterator*/ begin();
Returns an `iterator` to the first element of the `chunk_by_view`.
Equivalent to:

```cpp
ranges::iterator_t<V> iter;

if (begin_.has_value())
    iter = begin_.value();
else
{
    iter = /*find_next*/(ranges::begin(base()));
    begin_ = iter; // caching
}

return /*iterator*/(*this, ranges::begin(base()), iter);
```

The behavior is undefined if the underlying predicate  does not contain a value.

## Parameters

(none)

## Return value

`Iterator` to the first element.

## Notes

In order to provide the amortized constant-time complexity required by the  concept, this function caches the result within the data member  for use on subsequent calls.

## Example


## See also


| cpp/ranges/adaptor/dsc end|chunk_by_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |


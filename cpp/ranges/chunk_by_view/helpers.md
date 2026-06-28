---
title: std::ranges::chunk_by_view::find_prev
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_by_view/helpers
---

member|''next''|2=
ddcl|since=c++23|notes=|1=
constexpr ranges::iterator_t<V>
/*find-next*/( ranges::iterator_t<V> current );
Finds the next chunk.
Let
and
be appropriate underlying data-members of `chunk_by_view`.
Equivalent to

```cpp
return ranges::next
(
    ranges::adjacent_find
    (
        current, ranges::end(base_), std::not_fn(std::ref(*pred_))
    ),
    1, ranges::end(base_)
);
```

The behavior is undefined if `pred_.has_value()` is `false` before the call to this function.
Used in the following non-static member functions:
* `ranges::chunk_by_view|ranges::chunk_by_view::''iterator''::``operator++`

## Parameters


### Parameters

- `current` - the iterator to current element in adapted view

## Return value

An iterator to the next chunk, as described above.
member|''prev''|2=
ddcl|since=c++23|notes=|1=
constexpr ranges::iterator_t<V>
/*find-prev*/( ranges::iterator_t<V> current )
requires ranges::bidirectional_range<V>;
Finds the previous chunk.
Let
and
be appropriate underlying data-members of `chunk_by_view`.
Returns an iterator `i` in the range [ranges::begin(base_), current) such that:
* `ranges::adjacent_find(i, current, std::not_fn(std::ref(*pred_)))` is equal to `current`, and
* if `i` is not equal to `ranges::begin(base_)`, then `bool(std::invoke(*pred_, *ranges::prev(i), *i))` is `false`.
The behavior is undefined if before the call to this function `1=current == ranges::begin(base_)` or `1=pred_.has_value() != true`.
Used in the following non-static member functions:
* `ranges::chunk_by_view|ranges::chunk_by_view::''iterator''::``operator--`

## Parameters


### Parameters

- `current` - the iterator to current element in adapted view

## Return value

An iterator to the previous chunk, as described above.

---
title: std::ranges::split_view::find_next
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/split_view/find_next
---


```cpp
dcla|expos=yes|
constexpr ranges::subrange<ranges::iterator_t<V>>
/*find_next*/( ranges::iterator_t<V> it );
```

Searches for the next occurrence of pattern in the underlying view. Equivalent to:
box|c/core|1=
auto [b, e] = ranges::search(ranges::subrange(it, ranges::end(`)),`c/core|1=);
if (b != ranges::end(`) and ranges::empty(`c/core|))
{
++b;
++e;
}
return {b, e};

## Parameters


### Parameters

- `it` - an iterator to the position at which to start the search

## Return value

A subrange that represents the next position of the pattern, if it was found. An empty subrange otherwise.

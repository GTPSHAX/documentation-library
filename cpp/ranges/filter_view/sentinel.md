---
title: std::ranges::filter_view::sentinel
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/filter_view/sentinel
---

ddcl|since=c++20|notes=|
class /*sentinel*/;
The return type of `cpp/ranges/filter_view|filter_view::end` when the underlying  `V` does not model .

## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions

member|''sentinel''|2=

```cpp
dcl|since=c++20|num=1|1=
/*sentinel*/() = default;
dcl|since=c++20|num=2|1=
constexpr explicit /*sentinel*/( filter_view& parent );
```

1. Value-initializes  via its default member initializer (`1== ranges::sentinel_t<V>()`).
2. Initializes  with `ranges::end(parent.base_)`.
member|base|2=
ddcl|since=c++20|1=
constexpr ranges::sentinel_t<V> base() const;
Equivalent to `return end_;`.

## Non-member functions

member|1=operator==<small>(std::ranges::filter_view::''iterator'', std::ranges::filter_view::''sentinel'')</small>|2=
ddcl|since=c++20|1=
friend constexpr bool operator==( const /*iterator*/& x,
const /*sentinel*/& y );
Equivalent to `1=return x.current_ == y.end_;`, where  is the underlying iterator wrapped in `filter_view::''iterator''`.

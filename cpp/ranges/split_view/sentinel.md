---
title: std::ranges::split_view::sentinel
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/split_view/sentinel
---

ddcla|since=c++20|expos=yes|
class /*sentinel*/;
The return type of `cpp/ranges/split_view|split_view::end` when the underlying  type `V` does not models .

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
constexpr explicit /*sentinel*/( ranges::split_view& parent );
```

1. Value-initializes  via its default member initializer (`1== ranges::sentinel_t<V>()`).
2. Initializes  with `1=ranges::end(parent.base_)`.

## Non-member functions


| nolink=true|operator | |

member|1=operator==|2=
ddcl|since=c++20|1=
friend constexpr bool operator==( const /*iterator*/& x,
const /*sentinel*/& y );
Equivalent to `1=return x.cur_ == y.end_ and !x.trailing_empty_;`.

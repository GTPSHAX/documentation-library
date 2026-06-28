---
title: std::ranges::iota_view::sentinel
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/iota_view/sentinel
---


```cpp
dcla|anchor=no|expos=yes|
struct /*sentinel*/;
```

`ranges::iota_view<W, Bound>::` is the type of the reachable sentinels returned by  of `ranges::iota_view<W, Bound>`.

## Data members


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Member functions

member|''sentinel''|2=

```cpp
dcl|num=1|since=c++20|1=
/*sentinel*/() = default;
dcl|num=2|since=c++20|
constexpr explicit /*sentinel*/( Bound bound );
```

1. Value-initializes .
2. Initializes  with `bound`.

## Non-member functions

member|operator|2=
ddcl|since=c++20|1=
friend constexpr bool operator==( const /*iterator*/& x,
const /*sentinel*/& y );
Returns .
member|operator-|2=

```cpp
dcl|num=1|since=c++20|
friend constexpr std::iter_difference_t<W>
operator-(const /*iterator*/& x, const /*sentinel*/& y)
requires std::sized_sentinel_for<Bound, W>;
dcl|num=2|since=c++20|
friend constexpr std::iter_difference_t<W>
operator-(const /*sentinel*/& x, const /*iterator*/& y)
requires std::sized_sentinel_for<Bound, W>;
```

1. Returns .
2. Returns .

## Example


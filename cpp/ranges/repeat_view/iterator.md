---
title: std::ranges::repeat_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/repeat_view/iterator
---


```cpp
dcla|expos=yes|
struct /*iterator*/;
```

`ranges::repeat_view<W, Bound>::` is the type of the iterators returned by `begin()` and `end()` of `ranges::repeat_view<W, Bound>`.

## Nested types


| Item | Description |
|------|-------------|

#### Exposition-only types

| **Type** | Definition |

#### Iterator property types

| **Type** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Member functions

member|''iterator''|2=

```cpp
dcl|num=1|since=c++23|1=
/*iterator*/() = default;
dcla|num=2|since=c++23|expos=yes|1=
constexpr explicit /*iterator*/
( const W* value, /*index-type*/ b = /*index-type*/() );
```

Constructs an iterator. Overload  is called by `begin()` and `end()` of `ranges::repeat_view`.
1. Initializes  with `nullptr` and value-initializes .
2. Initializes  with `value` and  with `b`.
@@ If `Bound` is not `std::unreachable_sentinel_t` and `b` is negative, the behavior is undefined.
member|operator*|2=
ddcl|since=c++23|
constexpr const W& operator*() const noexcept;
Returns .
member|operator[]|2=
ddcl|since=c++23|
constexpr const W& operator[]( difference_type n ) const noexcept;
Returns `*(*this + n)`.
member|operator++|2=

```cpp
dcl|num=1|since=c++23|
constexpr /*iterator*/& operator++();
dcl|num=2|since=c++23|
constexpr void operator++(int);
```

1. Equivalent to .
2. Equivalent to `1=auto tmp = *this; ++*this; return tmp;`.
member|operator--|2=

```cpp
dcl|num=1|since=c++23|
constexpr /*iterator*/& operator--();
dcl|num=2|since=c++23|
constexpr /*iterator*/ operator--(int);
```

1. Equivalent to .
@@ If `Bound` is not `std::unreachable_sentinel_t` and  is non-positive, the behavior is undefined.
2. Equivalent to `1=auto tmp = *this; --*this; return tmp;`.
member|1=operator+=|2=
ddcl|since=c++23|1=
constexpr /*iterator*/& operator+=( difference_type n );
Equivalent to .
If `Bound` is not `std::unreachable_sentinel_t` and  is negative, the behavior is undefined.
member|1=operator-=|2=
ddcl|since=c++23|1=
constexpr /*iterator*/& operator-=( difference_type n );
Equivalent to .
If `Bound` is not `std::unreachable_sentinel_t` and  is negative, the behavior is undefined.

## Non-member functions

member|1=operator==, <=>|2=

```cpp
dcl|num=1|since=c++23|1=
friend constexpr bool operator==
( const /*iterator*/& x, const /*iterator*/& y );
dcl|num=2|since=c++23|1=
friend constexpr auto operator<=>
( const /*iterator*/& x, const /*iterator*/& y );
```

1. Returns .
2. Returns .
member|1=operator+|2=

```cpp
dcl|num=1|since=c++23|
friend constexpr /*iterator*/ operator+
( /*iterator*/ i, difference_type n );
dcl|num=2|since=c++23|
friend constexpr /*iterator*/ operator+
( difference_type n, /*iterator*/ i );
```

Equivalent to `1=i += n; return i;`.
member|1=operator-|2=

```cpp
dcl|num=1|since=c++23|
friend constexpr /*iterator*/ operator-
( /*iterator*/ i, difference_type n );
dcl|num=2|since=c++23|
friend constexpr difference_type operator-
( const /*iterator*/& x, const /*iterator*/& y );
```

1. Equivalent to `1=i -= n; return i;`.
2. Returns .

## Notes

is always .

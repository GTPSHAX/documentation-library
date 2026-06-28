---
title: std::ranges::basic_istream_view::iterator
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/basic_istream_view/iterator
---


```cpp
dcla|expos=yes|
struct /*iterator*/;
```

`ranges::basic_istream_view<Val, CharT, Traits>::` is the type of the iterators returned by `begin()` of `ranges::basic_istream_view<Val, CharT, Traits>`.
is an , but does not satisfy *InputIterator*, and thus does not work with pre-C++20 s.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |


## Member functions

member|''iterator''|

```cpp
dcl|num=1|since=c++20|1=
/*iterator*/( const /*iterator*/& ) = delete;
dcl|num=2|since=c++20|1=
/*iterator*/( /*iterator*/&& ) = default;
dcl|num=3|since=c++20|
constexpr explicit /*iterator*/( basic_istream_view& parent );
```

1. The copy constructor is deleted. The iterator is not copyable.
2. The move constructor is defaulted.
3. Initializes  with `std::addressof(parent)`.
member|operator|

```cpp
dcl|num=1|since=c++20|1=
/*iterator*/& operator=( const /*iterator*/& ) = delete;
dcl|num=2|since=c++20|1=
/*iterator*/& operator=( /*iterator*/&& ) = default;
```

1. The copy assignment operator is deleted. The iterator is not copyable.
2. The move assignment operator is defaulted.
member|operator++|

```cpp
dcl|num=1|since=c++20|
/*iterator*/& operator++();
dcl|num=2|since=c++20|
void operator++(int);
```

1. Equivalent to .
2. Equivalent to `++*this`.
member|operator*|
ddcl|since=c++20|
Val& operator*() const;
Returns .

## Non-member functions

member|operator|
ddcl|since=c++20|1=
friend bool operator==( const /*iterator*/& x, std::default_sentinel_t );
Returns .

## Defect reports


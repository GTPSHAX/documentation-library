---
title: std::ranges::enumerate_view::iterator<Const>::operators
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/enumerate_view/iterator/operator_arith
---


```cpp
dcl|num=1|since=c++23|
constexpr /*iterator*/& operator++();
dcl|num=2|since=c++23|
constexpr void operator++( int );
dcl|num=3|since=c++23|
constexpr /*iterator*/ operator++( int )
requires ranges::forward_range<Base>;
dcl|num=4|since=c++23|
constexpr /*iterator*/& operator--()
requires ranges::bidirectional_range<Base>;
dcl|num=5|since=c++23|
constexpr /*iterator*/ operator--( int )
requires ranges::bidirectional_range<Base>;
dcl|num=6|since=c++23|1=
constexpr /*iterator*/& operator+=( difference_type n )
requires ranges::random_access_range<Base>;
dcl|num=7|since=c++23|1=
constexpr /*iterator*/& operator-=( difference_type n )
requires ranges::random_access_range<Base>;
```

Increments or decrements the `iterator`.
Let  be the underlying iterator and  be the underlying index.
1. Equivalent to `1=++current_; ++pos_; return *this;`
2. Equivalent to `1=++current_;`
3. Equivalent to `1=auto tmp = *this; ++*this; return tmp;`
4. Equivalent to `1=--current_; --pos_; return *this;`
5. Equivalent to `1=auto tmp = *this; --*this; return tmp;`
6. Equivalent to `1=current_ += n; pos_ += n; return *this;`
7. Equivalent to `1=current_ -= n; pos_ -= n; return *this;`

## Parameters


### Parameters

- `n` - position relative to current location

## Return value

@1,4,6,7@ `*this`
2. (none)
@3,5@ a copy of `*this` that was made before the change

## See also


| cpp/ranges/enumerate_view/iterator/operator_arith2|title=operator+<br>operator-|performs iterator arithmetic|notes= | |


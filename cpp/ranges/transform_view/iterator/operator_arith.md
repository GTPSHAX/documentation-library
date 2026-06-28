---
title: std::ranges::transform_view::iterator<Const>::operators
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/transform_view/iterator/operator_arith
---


```cpp
dcl | num=1 | since=c++20 |
constexpr /*iterator*/& operator++();
dcl | num=2 | since=c++20 |
constexpr void operator++( int );
dcl | num=3 | since=c++20 |
constexpr /*iterator*/ operator++( int )
requires ranges::forward_range<Base>;
dcl | num=4 | since=c++20 |
constexpr /*iterator*/& operator--()
requires ranges::bidirectional_range<Base>;
dcl | num=5 | since=c++20 |
constexpr /*iterator*/ operator--( int )
requires ranges::bidirectional_range<Base>;
dcl | num=6 | since=c++20 |1=
constexpr /*iterator*/& operator+=( difference_type n )
requires ranges::random_access_range<Base>;
dcl | num=7 | since=c++20 |1=
constexpr /*iterator*/& operator-=( difference_type n )
requires ranges::random_access_range<Base>;
```

Increments or decrements the iterator.
Let `current_` be the underlying iterator.
1. Equivalent to `1=++current_; return *this;`
2. Equivalent to `1=++current_;`
3. Equivalent to `1=auto tmp = *this; ++*this; return tmp;`
4. Equivalent to `1=--current_; return *this;`
5. Equivalent to `1=auto tmp = *this; --*this; return tmp;`
6. Equivalent to `1=current_ += n; return *this;`
7. Equivalent to `1=current_ -= n; return *this;`

## Parameters


### Parameters


## Return value

@1,4,6,7@ `*this`
@3,5@ a copy of `*this` that was made before the change

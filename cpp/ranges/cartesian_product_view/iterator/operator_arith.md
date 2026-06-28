---
title: Vs...>::iterator::operators
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/cartesian_product_view/iterator/operator_arith
---


```cpp
dcl|num=1|since=c++23|
constexpr /*iterator*/& operator++();
dcl|num=2|since=c++23|
constexpr void operator++( int );
dcl|num=3|since=c++23|
constexpr /*iterator*/ operator++( int )
requires ranges::forward_range</*maybe-const*/<Const, First>>;
dcl|num=4|since=c++23|
constexpr /*iterator*/& operator--()
requires /*cartesian-product-is-bidirectional*/<Const, First, Vs...>;
dcl|num=5|since=c++23|
constexpr /*iterator*/ operator--( int )
requires /*cartesian-product-is-bidirectional*/<Const, First, Vs...>;
dcl|num=6|since=c++23|1=
constexpr /*iterator*/& operator+=( difference_type n )
requires /*cartesian-product-is-random-access*/<Const, First, Vs...>;
dcl|num=7|since=c++23|1=
constexpr /*iterator*/& operator-=( difference_type n )
requires /*cartesian-product-is-random-access*/<Const, First, Vs...>;
```

Increments or decrements the `iterator`.
Let  denote the underlying tuple of iterators and  denote the underlying pointer to `cartesian_product_view`.
1. Equivalent to
2. Equivalent to `++*this;`
3. Equivalent to `1=auto tmp = *this; ++*this; return tmp;`
4. Equivalent to
5. Equivalent to `1=auto tmp = *this; --*this; return tmp;`
6. Sets the value of `*this` to , where  is:
* if `n > 0`, the value of `*this` provided that  been called `n` times. Otherwise,
* if `n < 0`, the value of `*this` provided that  been called `-n` times. Otherwise,
* the value of `*this` before the call.
The behavior is undefined if `n` is not in the range [ranges::distance(*this, ranges::begin(*parent_)), ranges::distance(*this, ranges::end(*parent_))|]).
7. Equivalent to `1=*this += -n; return *this;`.

## Parameters


### Parameters

- `n` - position relative to current location

## Return value

@1,4,6,7@ `*this`
2. (none)
@3,5@ a copy of `*this` that was made before the change.

## Complexity

6. Constant.

## Example


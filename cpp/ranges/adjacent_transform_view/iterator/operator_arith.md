---
title: std::ranges::adjacent_transform_view::iterator<Const>::operators
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_transform_view/iterator/operator_arith
---


```cpp
dcl|num=1|since=c++23|
constexpr /*iterator*/& operator++();
dcl|num=2|since=c++23|
constexpr /*iterator*/ operator++(int);
dcl|num=3|since=c++23|
constexpr /*iterator*/& operator--()
requires ranges::bidirectional_range<Base>;
dcl|num=4|since=c++23|
constexpr /*iterator*/ operator--( int )
requires ranges::bidirectional_range<Base>;
dcl|num=5|since=c++23|1=
constexpr /*iterator*/& operator+=( difference_type n )
requires ranges::random_access_range<Base>;
dcl|num=6|since=c++23|1=
constexpr /*iterator*/& operator-=( difference_type n )
requires ranges::random_access_range<Base>;
```

Increments or decrements the `iterator`.
Let  be the underlying iterator and  be the exposition-only member type.
Equivalent to:
1. `++inner_; return *this;`
2. `1=auto tmp = *this; ++*this; return tmp;`
3. `--inner_; return *this;`
4. `1=auto tmp = *this; --*this; return tmp;`
5. `1=inner_ += n; return *this;`
6. `1=inner_ -= n; return *this;`

## Parameters


### Parameters

- `n` - position relative to current location

## Return value

@1,3,5,6@ `*this`
@2,4@ a copy of `*this` that was made before the change

## Example


## See also


| cpp/ranges/adaptor/iterator/dsc_operator_arith2|adjacent_transform_view | (see dedicated page) |


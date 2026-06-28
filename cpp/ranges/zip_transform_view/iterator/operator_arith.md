---
title: std::ranges::zip_transform_view::iterator<Const>::operators
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_transform_view/iterator/operator_arith
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
Let  be the underlying iterator and  be the exposition-only member type.
Equivalent to:
1. `++inner_; return *this;`
2. `++*this;`
3. `1=auto tmp = *this; ++*this; return tmp;`
4. `--inner_; return *this;`
5. `1=auto tmp = *this; --*this; return tmp;`
6. `1=inner_ += n; return *this;`
7. `1=inner_ -= n; return *this;`

## Parameters


### Parameters

- `n` - position relative to current location

## Return value

@1,4,6,7@ `*this`
2. (none)
@3,5@ a copy of `*this` that was made before the change

## Example


## See also


| cpp/ranges/adaptor/iterator/dsc_operator_arith2|zip_transform_view | (see dedicated page) |


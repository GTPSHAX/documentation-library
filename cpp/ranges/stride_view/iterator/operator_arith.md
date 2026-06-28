---
title: std::ranges::stride_view::iterator<Const>::operators
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/stride_view/iterator/operator_arith
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
Let , , , and  be the data members of the `iterator`.
1. Equivalent to

```cpp
missing_ = ranges::advance(current_, stride_, end_);
return *this
```

Before the call  should not be equal to .
2. Equivalent to `++*this;`.
3. Equivalent to `1=auto tmp = *this; ++*this; return tmp;`.
4. Equivalent to

```cpp
ranges::advance(current_, missing_ - stride_);
missing_ = 0;
return *this;
```

5. Equivalent to `1=auto tmp = *this; --*this; return tmp;`.
6. Equivalent to

```cpp
if (n > 0)
{
    ranges::advance(current_, stride_ * (n - 1));
    missing_ = ranges::advance(current_, stride_, end_);
}
else if (n < 0)
{
    ranges::advance(current_, stride_ * n + missing_);
    missing_ = 0;
}

return *this;
```

If `n > 0`, then before the call to this function the `ranges::distance(current_, end_)` must be greater than `stride_ * (n - 1)`.
Note that if `n < 0`, the `ranges::distance(current_, end_)` is always greater than (non-positive) `stride_ * (n - 1)`.
7. Equivalent to `1=return *this += -n;`

## Parameters


### Parameters

- `n` - position relative to current location

## Return value

@1,4,6,7@ `*this`
2. (none)
@3,5@ a copy of `*this` that was made before the change

## Example


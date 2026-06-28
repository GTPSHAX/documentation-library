---
title: std::ranges::chunk_view::iterator<Const>::operators
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/iterator/operator_arith
---


```cpp
dcl|num=1|since=c++23|
constexpr /*iterator*/& operator++();
dcl|num=2|since=c++23|
constexpr /*iterator*/ operator++( int );
dcl|num=3|since=c++23|
constexpr /*iterator*/& operator--()
requires ranges::bidirectional_range<Base>;
dcl|num=4|since=c++23|
constexpr /*iterator*/ operator--( int )
requires ranges::bidirectional_range<Base>;
dcl|num=5|since=c++23|1=
constexpr /*iterator*/& operator+=( difference_type x )
requires ranges::random_access_range<Base>;
dcl|num=6|since=c++23|1=
constexpr /*iterator*/& operator-=( difference_type x )
requires ranges::random_access_range<Base>;
```

Advances or decrements the `iterator`.
Let , , and  be the underlying `data members` of `chunk_view::iterator`.
1. Equivalent to:

```cpp
missing_ = ranges::advance(current_, n_, end_);
return *this;
```

Before the invocation the expression `1=current_ != end_` must be `true`, otherwise the behavior is undefined.
2. Equivalent to: `1=auto tmp = *this; ++*this; return tmp;`.
3. Equivalent to:

```cpp
ranges::advance(current_, missing_ - n_);
missing_ = 0;
return *this;
```

4. Equivalent to: `1=auto tmp = *this; --*this; return tmp;`.
5. Equivalent to:

```cpp
if (x > 0)
{
    ranges::advance(current_, n_ * (x - 1));
    missing_ = ranges::advance(current_, n_, end_);
}
else if (x < 0)
{
    ranges::advance(current_, n_ * x + missing_);
    missing_ = 0;
}
return *this;
```

If `x` is positive, then before the invocation the expression `ranges::distance(current_, end_) > n_ * (x - 1)` must be `true` (i.e., informally, the requested chunk should be "inside" the underlying sequence). If `x` is negative, this precondition is always met.
6. Equivalent to: `1=return *this += -x;`.

## Parameters


### Parameters

- `x` - a position relative to current location

## Return value

@1,3,5,6@ `*this`
@2,4@ a copy of `*this` that was made before the change

## Example


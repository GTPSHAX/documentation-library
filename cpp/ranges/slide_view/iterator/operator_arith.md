---
title: std::ranges::slide_view::iterator<Const>::operators
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/slide_view/iterator/operator_arith
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
constexpr /*iterator*/& operator+=( difference_type n )
requires ranges::random_access_range<Base>;
dcl|num=6|since=c++23|1=
constexpr /*iterator*/& operator-=( difference_type n )
requires ranges::random_access_range<Base>;
```

Advances or decrements the `iterator`.
Let  and  be the underlying iterators to the begin and end of the sliding window.
1. Equivalent to:

```cpp
current_ = ranges::next(current_);
last_ele_ = ranges::next(last_ele_); // if last_ele_ is present
return *this;
```

Before the invocation, the  and  (if present) must be incrementable.
2. Equivalent to: `1=auto tmp = *this; ++*this; return tmp;`
3. Equivalent to:

```cpp
current_ = ranges::prev(current_);
last_ele_ = ranges::prev(last_ele_); // if last_ele_ is present
return *this;
```

Before the invocation, the  and  (if present) must be decrementable.
4. Equivalent to: `1=auto tmp = *this; --*this; return tmp;`
5. Equivalent to:

```cpp
current_ = current_ + n;
last_ele_ = last_ele_ + n; // if last_ele_ is present
return *this;
```

Before the invocation, the expressions `current_ + n` and `last_ele_ + n` (if  is present) must have well-defined behavior.
6. Equivalent to:

```cpp
current_ = current_ - n;
last_ele_ = last_ele_ - n; // if last_ele_ is present
return *this;
```

Before the invocation, the expressions `current_ - n` and `last_ele_ - n` (if  is present) must have well-defined behavior.

## Parameters


### Parameters

- `n` - position relative to current location

## Return value

@1,3,5,6@ `*this`
@2,4@ a copy of `*this` that was made before the change

## Example


---
title: std::ranges::chunk_by_view::iterator::operators
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_by_view/iterator/operator_arith
---


```cpp
dcl|num=1|since=c++23|
constexpr /*iterator*/& operator++();
dcl|num=2|since=c++23|
constexpr /*iterator*/ operator++(int);
dcl|num=3|since=c++23|
constexpr /*iterator*/& operator--() requires ranges::bidirectional_range<V>;
dcl|num=4|since=c++23|
constexpr /*iterator*/ operator--(int) requires ranges::bidirectional_range<V>;
```

Increments or decrements the `iterator`.
Let
,
, and
be the appropriate underlying (exposition-only) data-members of `iterator`.
Let
and
be
appropriate (exposition-only) member functions of `ranges::chunk_by_view`.
1. Equivalent to:

```cpp
current_ = next_;
next_ = parent_->/*find-next*/(current_);
return *this;
```

@@ The behavior is undefined if before the call to this operator  is equal to .
2. Equivalent to: `1=auto tmp = *this; ++*this; return tmp;`
3. Equivalent to:

```cpp
next_ = current_;
current_ = parent_->/*find-prev*/(next_);
return *this;
```

4. Equivalent to: `1=auto tmp = *this; --*this; return tmp;`

## Parameters

(none)

## Return value

@1,3@ `*this`
@2,4@ a copy of `*this` that was made before the change.

---
title: std::ranges::chunk_view::inner-iterator::operator++
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/inner_iterator/operator_inc
---


```cpp
dcl|num=1|since=c++23|
constexpr /*inner-iterator*/& operator++();
dcl|num=2|since=c++23|
constexpr void operator++( int );
```

Increments the `iterator`.
Let  be the underlying pointer to enclosing `chunk_view`.
1. Equivalent to:

```cpp
++*parent_->current_;
if (*parent_->current_ == ranges::end(parent_->base_))
    parent_->remainder_ = 0;
else
    --parent_->remainder_;
return *this;
```

Before invocation of this operator the expression `1=*this == std::default_sentinel` must be `false`.
2. Equivalent to `++*this`.

## Parameters

(none)

## Return value

1. `*this`
2. (none)

## Example


## See also


| cpp/ranges/chunk_view/inner_iterator/operator-|calculates the number of chunks remained|notes= | |


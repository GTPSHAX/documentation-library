---
title: iter_move(ranges::adjacent_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_view/iterator/iter_move
---


# iter_movesmall|(ranges::adjacent_view::''iterator'')


```cpp
dcl|since=c++23|
friend constexpr auto iter_move( const /*iterator*/& i )
noexcept(/* see description */);
```

Returns the result of applying `ranges::iter_move` to the underlying iterators.
Equivalent to: `return /*tuple-transform*/(ranges::iter_move, i.current_);`, where  is an underlying array of iterators.

## Parameters


### Parameters

- `i` - iterator

## Return value

The result of applying `ranges::iter_move` to the underlying iterators.

## Exceptions

noexcept|
noexcept(ranges::iter_move(declval<const ranges::iterator_t<Base>&>()))
&&
std::is_nothrow_move_constructible_v<ranges::range_rvalue_reference_t<Base>>

## See also


| cpp/iterator/ranges/dsc iter move | (see dedicated page) |


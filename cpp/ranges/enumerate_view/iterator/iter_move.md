---
title: iter_move(ranges::enumerate_view::iterator)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/enumerate_view/iterator/iter_move
---


# iter_movesmall|(ranges::enumerate_view::''iterator'')

ddcl|since=c++23|
friend constexpr auto iter_move( const /*iterator*/& i ) noexcept(/* see below */)
Let  be the underlying iterator,  be the underlying index, and  be the (possibly cv-qualified) type of the underlying sequence.
Equivalent to:

```cpp
template<class D, class B>
using tuple = std::tuple<D, ranges::range_rvalue_reference_t<B>>;

return tuple<difference_type, Base>(i.pos_, ranges::iter_move(i.current_));
```


## Parameters


### Parameters

- `i` - iterator

## Return value

A tuple that contains an index and the result of applying `ranges::iter_move` to the stored iterator.

## Exceptions

noexcept|
noexcept(ranges::iter_move(i.current_)) and
std::is_nothrow_move_constructible_v<
ranges::range_rvalue_reference_t<Base>>

## See also


| cpp/iterator/ranges/dsc iter_move | (see dedicated page) |


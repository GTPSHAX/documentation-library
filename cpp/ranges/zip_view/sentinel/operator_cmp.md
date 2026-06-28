---
title: operators (ranges::zip_view::sentinel)
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_view/sentinel/operator_cmp
---


# 1= operator==small|(ranges::zip_view::''iterator'', ranges::zip_view::''sentinel'')


```cpp
dcl|since=c++23|1=
template< bool OtherConst >
requires (std::sentinel_for<
ranges::sentinel_t</*maybe-const*/<Const, Views>>,
ranges::iterator_t</*maybe-const*/<OtherConst, Views>>> && ...)
friend constexpr bool operator==( const /*iterator*/<OtherConst>& x,
const /*sentinel*/& y  );
```

Compares the underlying tuple of iterators of `x` with the underlying tuple of sentinels of `y`.

## Parameters


### Parameters

- `x` -  to compare
- `y` -  to compare

## Return value

Let `x.current_` denote the underlying tuple of iterators, and `y.end_` denote the underlying tuple of sentinels.
Returns
* `true` if at least one underlying iterator, obtained by expression equivalent to `std::get<i>(x.current_)`, evaluates equal (using an appropriate `1= operator==`) to some underlying sentinel, obtained by expression equivalent to `std::get<i>(y.end_)`, for some index `i` in ranges `1= 0 <= i < sizeof...(Views)`,
* `false` otherwise.

## Example


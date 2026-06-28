---
title: std::swap(std::mdspan)
type: Containers
source: https://en.cppreference.com/w/cpp/container/mdspan/swap2
---


# swapsmall|(std::mdspan)

ddcl|since=c++23|
friend constexpr void swap( mdspan& x, mdspan& y ) noexcept;
Overloads the `cpp/utility/swap|std::swap` algorithm for `std::mdspan`. Exchanges the state of `x` with that of `y`. Equivalent to:
box|
`std::``cpp/utility/swap``(x.``, y.``);`<br>
`std::``cpp/utility/swap``(x.``, y.``);`<br>
`std::``cpp/utility/swap``(x.``, y.``);`

## Parameters


### Parameters

- `x, y` - `mdspan` objects whose states to swap

## Return value

(none)

## Example


## See also


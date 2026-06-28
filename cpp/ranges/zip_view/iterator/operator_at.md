---
title: std::ranges::zip_view::iterator<Const>::operator[]
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/zip_view/iterator/operator_at
---

ddcl | since=c++23 | 1=
constexpr auto operator[]( difference_type n ) const
requires /*all-random-access*/<Const, Views...>;
Obtains a `std::tuple` that consists of underlying pointed-to elements at given offset relative to current location.
Equivalent to:

```cpp
return /*tuple-transform*/([&]<class I>(I& i) -> decltype(auto) {
           return i[iter_difference_t<I>(n)];
       }, current_);
```


## Parameters


### Parameters


## Return value

The obtained tuple-like element.

## Example


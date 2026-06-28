---
title: std::ranges::adjacent_view::iterator<Const>::operator[]
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_view/iterator/operator_at
---

ddcl|since=c++23|1=
constexpr auto operator[]( difference_type n ) const
requires ranges::random_access_range<Base>;
Returns an element at specified relative location.
Let  be an underlying array of iterators.
Equivalent to:

```cpp
return /*tuple-transform*/([&](auto& i) -> decltype(auto) { return i[n]; }, current_);
```


## Parameters


### Parameters

- `n` - position relative to current location

## Return value

The element at displacement `n` relative to the current location.

## Example


### Example

```cpp
#include <ranges>
#include <tuple>

int main()
{
    constexpr static auto v = {0, 1, 2, 3, 4, 5};
    //                               └──┬──┘  
    //                                  └─────────────────┐
    constexpr auto view = v {{!
```

//                 ┌───────────────────┬──────────────┘
//                 │                ┌──┴──┐
static_assert(view[2] == std::tuple{2, 3, 4});
}

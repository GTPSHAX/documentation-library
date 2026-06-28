---
title: std::ranges::stride_view::iterator<Const>::operator[]
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/stride_view/iterator/operator_at
---

ddcl|since=c++23|1=
constexpr decltype(auto) operator[]( difference_type n ) const
requires ranges::random_access_range<Base>
Returns an element at specified relative location.
Equivalent to: `return *(*this + n);`.

## Parameters


### Parameters

- `n` - position relative to current location

## Return value

The element at displacement `n` relative to the current location.

## Example


### Example

```cpp
#include <ranges>

int main()
{
    constexpr static auto v = {'a', 'b', 'c', 'd', 'e'};
    constexpr auto view{v {{!
```

constexpr auto iter{view.begin() + 1};
static_assert(*iter == 'c');
static_assert(iter[0] == 'c');
static_assert(iter[1] == 'e');
}

## See also


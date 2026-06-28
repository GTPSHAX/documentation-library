---
title: std::ranges::elements_view::iterator<Const>::operator[]
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/elements_view/iterator/operator_at
---

ddcl|since=c++20|1=
constexpr decltype(auto) operator[]( difference_type n ) const
requires ranges::random_access_range<Base>;
Returns an element at specified relative location, as if by `/*get-element*/(this->base() + n)`,

## Parameters


### Parameters

- `n` - position relative to current location

## Return value

The element at displacement `n` relative to the current location.

## Example


### Example

```cpp
#include <iostream>
#include <ranges>
#include <string_view>
#include <tuple>

int main()
{
    using T = std::tuple<int, char, std::string_view>;

    const auto il =
    {
        T{1, 'A', "α"},
        T{2, 'B', "β"},
        T{3, 'C', "γ"},
    };

    std::cout << std::views::elements<0>(il)[1] << ' '   // 2
              << std::views::elements<1>(il)[1] << ' '   // B
              << std::views::elements<2>(il)[1] << '\n'; // β
}
```


**Output:**
```
2 B β
```


## See also


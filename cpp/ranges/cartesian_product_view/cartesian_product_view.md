---
title: Vs...>::cartesian_product_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/cartesian_product_view/cartesian_product_view
---


```cpp
dcl|num=1|since=c++23|1=
constexpr cartesian_product_view() = default;
dcl|num=2|since=c++23|1=
constexpr explicit cartesian_product_view( First first_base, Vs... bases );
```

Constructs an `cartesian_product_view`.
1. Default constructor. Default-initializes the underlying data member .
2. Move constructs the underlying  by initializing it with `std::move(first_base), std::move(bases)...`.

## Parameters


### Parameters

- `first_base` - the first view object to adapt
- `bases` - the pack of views objects to adapt

## Example


### Example

```cpp
#include <array>
#include <format>
#include <iostream>
#include <ranges>
#include <vector>

int main()
{
    auto x = std::array{'A', 'B'};
    auto y = std::vector{1, 2, 3};
    auto z = std::vector{-1, -2, -3};

    auto v = std::ranges::cartesian_product_view(x, y, z); // overload (2)

    for (int i{1}; auto const& [rx, ry, rz] : v)
        std::cout << std::format("({} {} {}){}", rx, ry, rz, (i++ % 3) ? ' ' : '\n');
}
```


**Output:**
```
(A 1 -1) (A 1 -2) (A 1 -3)
(A 2 -1) (A 2 -2) (A 2 -3)
(A 3 -1) (A 3 -2) (A 3 -3)
(B 1 -1) (B 1 -2) (B 1 -3)
(B 2 -1) (B 2 -2) (B 2 -3)
(B 3 -1) (B 3 -2) (B 3 -3)
```


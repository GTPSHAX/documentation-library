---
title: std::ranges::transform_view::transform_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/transform_view/transform_view
---


```cpp
dcl|num=1|since=c++20|1=
transform_view() requires std::default_initializable<V> &&
std::default_initializable<F> = default;
dcl|num=2|since=c++20|1=
constexpr explicit transform_view( V base, F fun );
```

Constructs a `transform_view`.
1. Default constructor. Value-initializes the underlying view  and the transformation function .
2. Move constructs the underlying view  from `base` and the transformation function  from `fun`.

## Parameters


### Parameters

- `base` - view
- `fun` - transformation function

## Example


### Example

```cpp
#include <algorithm>
#include <functional>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <ranges>

int main()
{
    std::cout << std::setprecision(15) << std::fixed;
    auto atan1term{std::ranges::views::transform
    (
        [](int n) { return ((n % 2) ? -1 : 1) * 1.0 / (2 * n + 1); }
    )};
    for (const int iterations : {1, 2, 3, 4, 5, 10, 100, 1000, 1'000'000})
    {
        auto seq{std::ranges::views::iota(0, iterations) bitor atan1term};
        const double accum{*std::ranges::fold_left_first(seq, std::plus{})};
        std::cout << "π ≈ " << 4 * accum << " (iterations: " << iterations << ")\n";
    }
    std::cout << "π ≈ " << std::numbers::pi << " (std::numbers::pi)\n";
}
```


**Output:**
```
π ≈ 4.000000000000000 (iterations: 1)
π ≈ 2.666666666666667 (iterations: 2)
π ≈ 3.466666666666667 (iterations: 3)
π ≈ 2.895238095238096 (iterations: 4)
π ≈ 3.339682539682540 (iterations: 5)
π ≈ 3.041839618929403 (iterations: 10)
π ≈ 3.131592903558554 (iterations: 100)
π ≈ 3.140592653839794 (iterations: 1000)
π ≈ 3.141591653589774 (iterations: 1000000)
π ≈ 3.141592653589793 (std::numbers::pi)
```


## Defect reports


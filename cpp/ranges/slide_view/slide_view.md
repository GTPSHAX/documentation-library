---
title: std::ranges::slide_view::slide_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/slide_view/slide_view
---

ddcl|since=c++23|1=
constexpr explicit slide_view( V base, ranges::range_difference_t<V> n );
Constructs a `slide_view` initializing the underlying data members:
* move construct the underlying view  with `std::move(base)`,
* the "window size"  with `n`.

## Parameters


### Parameters

- `base` - the source view
- `n` - the “sliding window” size

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <ranges>

int main()
{
    const auto source = {1, 2, 3, 4};

    auto slide = std::views::slide(source, 3);

    std::ranges::for_each(slide, [](std::ranges::viewable_range auto&& w)
    {
        std::cout << '[' << w[0] << ' ' << w[1] << ' ' << w[2] << "]\n";
    });
}
```


**Output:**
```
[1 2 3]
[2 3 4]
```


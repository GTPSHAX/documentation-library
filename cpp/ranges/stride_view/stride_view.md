---
title: std::ranges::stride_view::stride_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/stride_view/stride_view
---

ddcl|since=c++23|
constexpr explicit stride_view( V base, ranges::range_difference_t<V> stride );
Constructs a `stride_view` initializing the underlying data members:
* move construct the underlying view  with `std::move(base)`,
* construct the  with `stride`.
If `stride < 1` the behavior is undefined.

## Parameters


### Parameters

- `base` - the source view
- `stride` - the stride value

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <ranges>
#include <string_view>

void print(std::string_view rem, auto v, std::string_view term = "\n")
{
    std::cout << rem << ": ";
    std::ranges::copy(v, std::ostream_iterator<int>(std::cout, " "));
    std::cout << term;
};

int main()
{
    auto source = std::views::iota(1, 10);
    print("source", source);

    for (int stride_value : std::views::iota(1, 6))
    {
        auto strided_view = std::views::stride(source, stride_value);

        print("stride", std::views::single(stride_value), "-> ");
        print("result", strided_view);
    }
}
```


**Output:**
```
source: 1 2 3 4 5 6 7 8 9
stride: 1 -> result: 1 2 3 4 5 6 7 8 9
stride: 2 -> result: 1 3 5 7 9
stride: 3 -> result: 1 4 7
stride: 4 -> result: 1 5 9
stride: 5 -> result: 1 6
```


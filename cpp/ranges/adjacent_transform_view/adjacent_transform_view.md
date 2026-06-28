---
title: std::ranges::adjacent_transform_view::adjacent_transform_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_transform_view/adjacent_transform_view
---


```cpp
dcl|num=1|since=c++23|1=
adjacent_transform_view() = default;
dcl|num=2|since=c++23|1=
constexpr explicit adjacent_transform_view( V base, F fun );
```

Constructs an `adjacent_transform_view`.
1. Default constructor. Default-initializes the underlying data members  and .
2. Move constructs the underlying data members:  with `std::move(fun)` and  with `std::move(base)`.

## Parameters


### Parameters

- `base` - the underlying view
- `fun` - the N-ary transformation function

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <ranges>

int main()
{
    constexpr static auto v = {1, 2, 3, 4, 5};
    constexpr auto mul = [](auto... x) { return (... * x); };
    constexpr auto view = std::views::adjacent_transform<3>(v, mul);
    std::ranges::copy(view, std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';
}
```


**Output:**
```
6 24 60
```


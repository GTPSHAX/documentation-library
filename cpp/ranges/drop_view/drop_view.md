---
title: std::ranges::drop_view::drop_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/drop_view/drop_view
---


```cpp
dcl|num=1|since=c++20|1=
drop_view() requires std::default_initializable<V> = default;
dcl|num=2|since=c++20|
constexpr explicit drop_view( V base, ranges::range_difference_t<V> count );
```

Constructs a `drop_view`.
1. Default constructor. Value-initializes the underlying view  and initializes the count  to `0`. After construction,  returns a copy of `V()` and  equals to the size of the underlying view.
2. Initializes the underlying view  with `std::move(base)` and the count  with `count`. After construction,  returns a copy of `base` and  returns `ranges::size(base) - count` if the size of `base` is not less than `count`, or `0` otherwise.

## Parameters


### Parameters

- `base` - the underlying view
- `count` - number of elements to skip

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <iterator>
#include <ranges>

int main()
{
    constexpr std::array hi{'H', 'e', 'l', 'l', 'o', ',',
                            ' ', 'C', '+', '+', '2', '0'};

    std::ranges::for_each(hi, [](const char c){ std::cout << c; });
    std::cout << '\n';

    constexpr auto n = std::distance(hi.cbegin(), std::ranges::find(hi, 'C'));

    auto cxx = std::ranges::drop_view{hi, n};

    std::ranges::for_each(cxx, [](const char c){ std::cout << c; });
    std::cout << '\n';
}
```


**Output:**
```
Hello, C++20
C++20
```


## Defect reports


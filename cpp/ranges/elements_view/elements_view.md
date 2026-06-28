---
title: std::ranges::elements_view::elements_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/elements_view/elements_view
---


```cpp
dcl|num=1|since=c++20|1=
elements_view() requires std::default_initializable<V> = default;
dcl|num=2|since=c++20|1=
constexpr explicit elements_view( V base );
```

Constructs an `elements_view`.
1. Default constructor. Value-initializes the underlying view . After construction, `base()` returns a copy of `V()`.
2. Initializes the underlying view  with `std::move(base)`.

## Parameters


### Parameters

- `base` - the underlying view

## Example


### Example

```cpp
#include <array>
#include <iostream>
#include <ranges>
#include <tuple>

void println(auto const& v)
{
    for (auto const& e : v)
        std::cout << e << ' ';
    std::cout << '\n';
}

int main()
{
    using namespace std::literals;

    const std::array<std::tuple<int, char, std::string>, 2> vt
    {
        std::tuple{1, 'A', "α"s},
        std::tuple{2, 'B', "β"s},
    };

    [[maybe_unused]]
    auto empty = std::views::elements<0>;

    println(std::views::elements<0>(vt));
    println(std::views::elements<1>(vt));
    println(std::views::elements<2>(vt));
}
```


**Output:**
```
1 2
A B
α β
```


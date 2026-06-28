---
title: std::ranges::drop_while_view::drop_while_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/drop_while_view/drop_while_view
---


```cpp
dcl|num=1|since=c++20|1=
drop_while_view() requires std::default_initializable<V> &&
std::default_initializable<Pred> = default;
dcl|num=2|since=c++20|1=
constexpr explicit drop_while_view( V base, Pred pred );
```

Constructs a `drop_while_view`.
1. Default constructor. Value-initializes the underlying view  and the predicate .
2. Move constructs the underlying view  from `base` and the predicate  from `pred`.

## Parameters


### Parameters

- `base` - underlying view
- `pred` - predicate

## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <ranges>

int main()
{
    static constexpr auto a = {-2, -7, -1, -8, -2, +-+8, 3, 1, 4, 1, 5};
    auto positive = [](int x) { return 0 < x; };
    for (auto v = std::ranges::drop_while_view{a, std::not_fn(positive)}; int x : v)
        std::cout << x << ' ';
    std::cout << '\n';
}
```


**Output:**
```
3 1 4 1 5
```


## Defect reports


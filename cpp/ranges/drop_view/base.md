---
title: std::ranges::drop_view::base
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/drop_view/base
---


```cpp
dcl|num=1|since=c++20|
constexpr V base() const& requires std::copy_constructible<V>;
dcl|num=2|since=c++20|
constexpr V base() &&;
```

Returns a copy of the underlying view.
1. Copy constructs the result from the underlying view .
2. Move constructs the result from the underlying view .

## Return value

A copy of the underlying (adapted) view .

## Example


### Example

```cpp
#include <iostream>
#include <ranges>

namespace stq {
void println(auto, const auto& v)
{
    for (const auto& e : v)
        std::cout << e << ' ';
    std::cout << '\n';
}
}

int main()
{
    static constexpr int a[]{1, 2, 3, 4, 5};
    constexpr auto view = a {{!
```

stq::println("{}", view);
const auto base = view.base();
stq::println("{}", base);
}
|output=
3 4 5
1 2 3 4 5

---
title: std::ranges::stride_view::base
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/stride_view/base
---


```cpp
dcl|num=1|since=c++23|
constexpr V base() const& requires std::copy_constructible<V>;
dcl|num=2|since=c++23|
constexpr V base() &&;
```

1. Copy constructs the result from the underlying view. Equivalent to .
2. Move constructs the result from the underlying view. Equivalent to .

## Return value

A copy of the underlying view.

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <ranges>

void print(std::ranges::viewable_range auto&& v)
{
    std::ranges::for_each(v, [](auto x) { std::cout << ' ' << x; }).fun('\n');
};

int main()
{
    const auto source = {1, 2, 3, 4, 5};

    auto view1 = std::views::stride(source, 1337);
    print(view1.base());

    auto view2 = source {{!
```

print(view2.base());
}
|output=<nowiki/>
1 2 3 4 5
5 4 3 2 1

---
title: std::ranges::chunk_view::base
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/base
---


```cpp
dcl|num=1|since=c++23|
constexpr V base() const& requires std::copy_constructible<V>;
dcl|num=2|since=c++23|
constexpr V base() &&;
```

Returns a copy of the underlying view.
1. Copy constructs the result from the underlying view. Equivalent to
.
2. Move constructs the result from the underlying view. Equivalent to
.

## Return value

A copy of the underlying view.

## Example


### Example

```cpp
#include <print>
#include <ranges>

int main()
{
    static constexpr auto v = {1, 2, 3, 4};
    constexpr auto w{std::ranges::chunk_view(v, 2)};
    std::println("{}", w.base());
}
```


**Output:**
```
[1, 2, 3, 4]
```


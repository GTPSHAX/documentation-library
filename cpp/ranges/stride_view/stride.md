---
title: std::ranges::stride_view::stride
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/stride_view/stride
---

ddcl|since=c++23|
constexpr ranges::range_difference_t<_Vp> stride() const noexcept;
Returns a copy of the underlying stride object . Equivalent to .

## Return value

The stride value.

## Example


### Example

```cpp
#include <ranges>

int main()
{
    constexpr auto view = std::views::iota(1337)
                        {{!
```

static_assert(view.stride() == 42);
}

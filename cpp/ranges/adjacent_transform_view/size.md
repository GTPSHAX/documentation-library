---
title: std::ranges::adjacent_transform_view::size
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/adjacent_transform_view/size
---


```cpp
dcl|since=c++23|
constexpr auto size() requires ranges::sized_range<InnerView>;
dcl|since=c++23|
constexpr auto size() const requires ranges::sized_range<const InnerView>;
```

Returns the number of elements.
Let  be the underlying object of type  (that is the `ranges::adjacent_view<V,N>`).
@1,2@ Equivalent to `return inner_.size();`.

## Parameters

(none)

## Return value

The number of elements, may be `0` if the size of the underlying view `V` is less than `N`.

## Example


### Example

```cpp
#include <ranges>

int main()
{
    constexpr static auto v = {1, 2, 3, 4, 5, 6};

    auto f = [](auto...) { return 0; }; // dummy

    constexpr int width1 {4};
    constexpr auto view1 = v {{!
```

static_assert(view1.size() == 3);
static_assert(view1.size() == (v.size() - width1 + 1));
constexpr int width2 {8};
constexpr auto view2 = v | std::views::adjacent_transform<width2>(f);
// window is too wide, so view2 has no elements:
static_assert(view2.size() == 0);
}

## See also


| cpp/ranges/dsc size | (see dedicated page) |
| cpp/ranges/dsc ssize | (see dedicated page) |


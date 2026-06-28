---
title: std::ranges::stride_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/stride_view/begin
---


```cpp
dcl|num=1|since=c++23|
constexpr auto begin() requires (!__simple_view<V>);
dcl|num=2|since=c++23|
constexpr auto begin() const requires ranges::range<const V>;
```

Returns an `iterator` to the first element of the `stride_view`.
1. Equivalent to `return iterator<false>(this, ranges::begin(base_));`.
2. Equivalent to `return iterator<true>(this, ranges::begin(base_));`.
Overload  does not participate in overload resolution if `V` is a simple view (that is, if `V` and `const V` are views with the same iterator and sentinel types).

## Parameters

(none)

## Return value

`Iterator` to the first element of the view.

## Example


### Example

```cpp
#include <print>
#include <ranges>

int main()
{
    constexpr auto v = {'A', 'B', 'C'};
    const auto x = v {{!
```

const auto y = v | std::views::reverse | std::views::stride(2);
const auto z = v | std::views::stride(2) | std::views::reverse;
std::println("{} {} {}", *x.begin(), *y.begin(), *z.begin());
}
|output=A C C

## See also


| cpp/ranges/adaptor/dsc end|stride_view | (see dedicated page) |


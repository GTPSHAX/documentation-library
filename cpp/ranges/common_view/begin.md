---
title: std::ranges::common_view::begin
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/common_view/begin
---


```cpp
dcl|num=1|since=c++20|
constexpr auto begin() requires (!/*simple_view*/<V>);
dcl|num=2|since=c++20|
constexpr auto begin() const requires range<const V>;
```

1. Returns an iterator to the first element of the `common_view`, that is:
* , if both `ranges::random_access_range<V>` and `ranges::sized_range<V>` are satisfied,
*  otherwise.
2. Same as , but `V` is const-qualified.

## Return value

An iterator to the beginning of the underlying view.

## Example


### Example

```cpp
#include <iostream>
#include <numeric>
#include <ranges>
#include <string_view>

int main()
{
    constexpr auto common = std::views::iota(1)
                          {{!
```

| std::views::common
;
for (int i{}; int e : common)
std::cout << (i++ ? " + " : "") << e;
std::cout << " = " << std::accumulate(common.begin(), common.end(), 0) << '\n';
}
|output = 1 + 2 + 3 = 6

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-4012 | C++20 | non-const overload missed simple-view check | added |


## See also


| cpp/ranges/adaptor/dsc end|common_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |


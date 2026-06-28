---
title: std::ranges::common_view::end
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/common_view/end
---


```cpp
dcl|num=1|since=c++20|
constexpr auto end() requires (!/*simple-view*/<V>);
dcl|num=2|since=c++20|
constexpr auto end() const requires ranges::range<const V>;
```

1. Returns an iterator representing the end of the `common_view`, that is:
* , if both `ranges::random_access_range<V>` and `ranges::sized_range<V>` are satisfied,
*  otherwise.
2. Same as , but `V` is const-qualified.

## Return value

An iterator representing the end of the underlying view.

## Example


### Example

```cpp
#include <iostream>
#include <numeric>
#include <ranges>

int main()
{
    constexpr int n{4};

    constexpr auto v1 = std::views::iota(1)
                      {{!
```

| std::views::common
;
constexpr auto v2 = std::views::iota(2)
| std::views::take(n)
;
const int product = std::inner_product(v1.begin(), v1.end(),
v2.begin(),
0);
std::cout << product << '\n';
}
|output=40

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-4012 | C++20 | non-const overload missed simple-view check | added |


## See also


| cpp/ranges/adaptor/dsc begin|common_view | (see dedicated page) |
| cpp/ranges/dsc begin | (see dedicated page) |
| cpp/ranges/dsc end | (see dedicated page) |


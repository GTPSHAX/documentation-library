---
title: std::ranges::take_view::size
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/take_view/size
---


```cpp
dcl|num=1|since=c++20|
constexpr auto size() requires ranges::sized_range<V>;
dcl|num=2|since=c++20|
constexpr auto size() const requires ranges::sized_range<const V>;
```

Returns the number of elements, which is the smaller of the count passed to the constructor and the size of the underlying view.
Let  be the underlying view,  be the underlying counter (equals to `0` if default constructed). Equivalent to

```cpp
auto n = ranges::size(base_);
return ranges::min(n, static_cast<decltype(n)>(count_));
```


## Parameters

(none)

## Return value

The number of elements.

## Example


### Example

```cpp
#include <iostream>
#include <ranges>

int main()
{
    constexpr int arr[]{1, 2, 3};

    for (int i = 0; i != 6; ++i)
    {
        const auto tv = std::ranges::take_view{arr, i};
        std::cout << tv.size() << ' ';
    }
    std::cout << '\n';
}
```


**Output:**
```
0 1 2 3 3 3
```


## See also


| cpp/ranges/dsc size | (see dedicated page) |
| cpp/ranges/dsc ssize | (see dedicated page) |


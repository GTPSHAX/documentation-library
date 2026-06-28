---
title: std::ranges::chunk_view::chunk_view
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/chunk_view/chunk_view
---

ddcl|since=c++23|
constexpr explicit chunk_view( V base, ranges::range_difference_t<V> n );
Constructs a `chunk_view`, initializing the underlying data members:
* move constructs the  with `std::move(base)`,
* initializes the "chunk size"  with `n`.
In addition, if `V` models exactly the , the constructor initializes the following exposition-only data members:
* initializes the  with `0`,
* default-initializes the .
The behavior is undefined if `n` is less than or equal to `0`.

## Parameters


### Parameters

- `base` - the adapted view
- `n` - the chunk size

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <ranges>

int main()
{
    auto i = std::views::iota(0, 10);
    auto w = std::ranges::chunk_view(i, 4);

    std::ranges::for_each(w, [](auto const v)
    {
        for (auto e : v)
            std::cout << e << ' ';
        std::cout << '\n';
    });
}
```


**Output:**
```
0 1 2 3
4 5 6 7
8 9
```


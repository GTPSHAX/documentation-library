---
title: std::span::front
type: Containers
source: https://en.cppreference.com/w/cpp/container/span/front
---

ddcl|since=c++20|
constexpr reference front() const;
Returns a reference to the first element in the span.

## Return value

A reference to the first element.

## Complexity

Constant.

## Notes

For a span `c`, the expression `c.front()` is equivalent to `*c.begin()`.

## Example


### Example

```cpp
#include <iostream>
#include <span>

void print(std::span<const int> const data)
{
    for (auto offset{0U}; offset != data.size(); ++offset)
        std::cout << data.subspan(offset).front() << ' ';
    std::cout << '\n';
}

int main()
{
    constexpr int data[]{0, 1, 2, 3, 4, 5, 6};
    print({data, 4});
}
```


**Output:**
```
0 1 2 3
```


## See also


| cpp/container/dsc back|span | (see dedicated page) |


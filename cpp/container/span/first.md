---
title: std::span::first
type: Containers
source: https://en.cppreference.com/w/cpp/container/span/first
---


```cpp
dcl|num=1|since=c++20|
template< std::size_t Count >
constexpr std::span<element_type, Count> first() const;
dcl|num=2|since=c++20|
constexpr std::span<element_type, std::dynamic_extent>
first( size_type count ) const;
```

Obtains a subview over the first `Count` or `count` elements of this span.
1. The element count is provided as a template argument, and the subview has a static extent.
@@ If `Count > Extent` is `true`, the program is ill-formed.
2. The element count is provided as a function argument, and the subview has a dynamic extent.

## Parameters


### Parameters

- `count` - the number of the elements of the subview

## Return value

1. }
2. }

## Example


### Example

```cpp
#include <iostream>
#include <ranges>
#include <span>
#include <string_view>

void print(const std::string_view title,
           const std::ranges::forward_range auto& container)
{
    auto size{std::size(container)};
    std::cout << title << '[' << size << "]{";
    for (const auto& elem : container)
        std::cout << elem << (--size ? ", " : "");
    std::cout << "};\n";
}

void run_game(std::span<const int> span)
{
    print("span: ", span);

    std::span<const int, 5> span_first = span.first<5>();
    print("span.first<5>(): ", span_first);

    std::span<const int, std::dynamic_extent> span_first_dynamic = span.first(4);
    print("span.first(4): ", span_first_dynamic);
}

int main()
{
    int a[8]{1, 2, 3, 4, 5, 6, 7, 8};
    print("int a", a);
    run_game(a);
}
```


**Output:**
```
int a[8]{1, 2, 3, 4, 5, 6, 7, 8};
span: [8]{1, 2, 3, 4, 5, 6, 7, 8};
span.first<5>(): [5]{1, 2, 3, 4, 5};
span.first(4): [4]{1, 2, 3, 4};
```


## See also


| cpp/container/span/dsc last | (see dedicated page) |
| cpp/container/span/dsc subspan | (see dedicated page) |


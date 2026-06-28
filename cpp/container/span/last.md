---
title: std::span::last
type: Containers
source: https://en.cppreference.com/w/cpp/container/span/last
---


```cpp
dcl|num=1|since=c++20|
template< std::size_t Count >
constexpr std::span<element_type, Count> last() const;
dcl|num=2|since=c++20|
constexpr std::span<element_type, std::dynamic_extent>
last( size_type count ) const;
```

Obtains a subview over the last `Count` or `count` elements of this span.
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
#include <span>
#include <string_view>

void println(const std::string_view title, const auto& container)
{
    std::cout << title << '[' << std::size(container) << "]{ ";
    for (const auto& elem : container)
        std::cout << elem << ", ";
    std::cout << "};\n";
};

void run(std::span<const int> span)
{
    println("span: ", span);

    std::span<const int, 3> span_last = span.last<3>();
    println("span.last<3>(): ", span_last);

    std::span<const int, std::dynamic_extent> span_last_dynamic = span.last(2);
    println("span.last(2): ", span_last_dynamic);
}

int main()
{
    int a[8]{1, 2, 3, 4, 5, 6, 7, 8};
    println("int a", a);
    run(a);
}
```


**Output:**
```
int a[8]{ 1, 2, 3, 4, 5, 6, 7, 8, };
span: [8]{ 1, 2, 3, 4, 5, 6, 7, 8, };
span.last<3>(): [3]{ 6, 7, 8, };
span.last(2): [2]{ 7, 8, };
```


## See also


| cpp/container/span/dsc first | (see dedicated page) |
| cpp/container/span/dsc subspan | (see dedicated page) |


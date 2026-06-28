---
title: std::swap(std::pair)
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/pair/swap2
---


# swappetty|(std::pair)


```cpp
**Header:** `<`utility`>`
dcl rev multi|num=1
|since1=c++11|dcl1=
template< class T1, class T2 >
void swap( std::pair<T1,T2>& x, std::pair<T1,T2>& y )
noexcept(/* see below */);
|since2=c++20|dcl2=
template< class T1, class T2 >
constexpr void swap( std::pair<T1,T2>& x, std::pair<T1,T2>& y )
noexcept(/* see below */);
dcl|num=2
|since=c++23|
template< class T1, class T2 >
constexpr void swap( const std::pair<T1,T2>& x, const std::pair<T1,T2>& y )
noexcept(/* see below */);
```

Swaps the contents of `x` and `y`. Equivalent to `x.swap(y)`.
rrev|since=c++17|
1. .
2. .

## Parameters


### Parameters

- `x, y` - pairs whose contents to swap

## Exceptions


## Example


### Example

```cpp
#include <iostream>
#include <utility>

int main()
{
    auto p1 = std::make_pair(10, 3.14);
    auto p2 = std::pair(12, 1.23); // CTAD, since C++17

    auto print_p1_p2 = [&](auto msg) {
        std::cout << msg
                  << "p1 = {" << std::get<0>(p1)
                  << ", "     << std::get<1>(p1) << "}, "
                  << "p2 = {" << std::get<0>(p2)
                  << ", "     << std::get<1>(p2) << "}\n";
    };

    print_p1_p2("Before p1.swap(p2): ");
    p1.swap(p2);
    print_p1_p2("After  p1.swap(p2): ");
    std::swap(p1, p2);
    print_p1_p2("After swap(p1, p2): ");
}
```


**Output:**
```
Before p1.swap(p2): p1 = {10, 3.14}, p2 = {12, 1.23}
After  p1.swap(p2): p1 = {12, 1.23}, p2 = {10, 3.14}
After swap(p1, p2): p1 = {10, 3.14}, p2 = {12, 1.23}
```


## See also


| cpp/algorithm/dsc swap | (see dedicated page) |
| cpp/utility/tuple/dsc swap2 | (see dedicated page) |


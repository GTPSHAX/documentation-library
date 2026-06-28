---
title: std::tuple_size<std::pair>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/pair/tuple_size
---


# tuple_sizesmall|<std::pair>

ddcl|header=utility|since=c++11|
template< class T1, class T2 >
struct tuple_size<std::pair<T1, T2>>
: std::integral_constant<std::size_t, 2> { };
The partial specialization of `std::tuple_size` for pairs provides a compile-time way to obtain the number of elements in a pair, which is always 2, using tuple-like syntax.

## Example


### Example

```cpp
#include <iostream>
#include <tuple>
#include <utility>

template<class T>
void test([[maybe_unused]]T t)
{
    [[maybe_unused]]
    int a[std::tuple_size<T>::value]; // can be used at compile time
    std::cout << std::tuple_size<T>::value << '\n'; // or at run time
}

int main()
{
    test(std::make_tuple(1, 2, 3.14));
    test(std::make_pair(1, 3.14));
}
```


**Output:**
```
3
2
```


## Defect reports


## See also


| cpp/language/dsc structured binding | (see dedicated page) |
| cpp/utility/dsc tuple_size | (see dedicated page) |
| cpp/container/array/dsc tuple_size | (see dedicated page) |
| cpp/utility/tuple/dsc tuple_size | (see dedicated page) |
| cpp/ranges/subrange/dsc tuple_size | (see dedicated page) |
| cpp/utility/pair/dsc tuple_element | (see dedicated page) |


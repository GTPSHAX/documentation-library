---
title: std::is_placeholder
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/is_placeholder
---

ddcl|header=functional|since=c++11|
template< class T >
struct is_placeholder;
If `T` is the type of a standard placeholder `(_1, _2, _3, ...)`, then this template is derived from `std::integral_constant<int, 1>`, `std::integral_constant<int, 2>`, `std::integral_constant<int, 3>`, respectively.
If `T` is not a standard placeholder type, this template is derived from `std::integral_constant<int, 0>`.
A program may specialize this template for a  `T` to implement *UnaryTypeTrait* with base characteristic of `std::integral_constant<int, N>` with positive `N` to indicate that `T` should be treated as `N` placeholder type.
`std::bind` uses `std::is_placeholder` to detect placeholders for unbound arguments.

## Helper variable template

ddcl|since=c++17|1=
template< class T >
constexpr int is_placeholder_v = is_placeholder<T>::value;

## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <type_traits>

struct My_2 {} my_2;

namespace std
{
    template<>
    struct is_placeholder<My_2> : public integral_constant<int, 2> {};
}

int f(int n1, int n2)
{
    return n1 + n2;
}

int main()
{
    std::cout << "Standard placeholder _5 is for the argument number "
              << std::is_placeholder_v<decltype(std::placeholders::_5)>
              << '\n';

    auto b = std::bind(f, my_2, 2);
    std::cout << "Adding 2 to 11 selected with a custom placeholder gives " 
              << b(10, 11) // the first argument, namely 10, is ignored
              << '\n';
}
```


**Output:**
```
Standard placeholder _5 is for the argument number 5
Adding 2 to 11 selected with a custom placeholder gives 13
```


## See also


| cpp/utility/functional/dsc bind | (see dedicated page) |
| cpp/utility/functional/dsc placeholders | (see dedicated page) |


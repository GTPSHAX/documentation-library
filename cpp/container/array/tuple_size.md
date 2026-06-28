---
title: std::tuple_size(std::array)
type: Containers
source: https://en.cppreference.com/w/cpp/container/array/tuple_size
---


# tuple_sizepetty|<std::array>

ddcl|header=array|since=c++11|
template< class T, std::size_t N >
struct tuple_size< std::array<T, N> > :
std::integral_constant<std::size_t, N>
{ };
Provides access to the number of elements in an `std::array` as a compile-time constant expression.

## Helper variable template

ddcl|since=c++17|1=
template< class T >
constexpr std::size_t tuple_size_v = tuple_size<T>::value;

## Example


### Example

```cpp
#include <array>

int main()
{
    auto arr = std::to_array("ABBA");
    static_assert(std::tuple_size<decltype(arr)>{} == 5);
}
```


## See also


| cpp/language/dsc structured binding | (see dedicated page) |
| cpp/utility/dsc tuple_size | (see dedicated page) |
| cpp/utility/tuple/dsc tuple_size | (see dedicated page) |
| cpp/utility/pair/dsc tuple_size | (see dedicated page) |
| cpp/ranges/subrange/dsc tuple_size | (see dedicated page) |


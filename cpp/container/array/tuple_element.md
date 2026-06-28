---
title: std::tuple_element<std::array>
type: Containers
source: https://en.cppreference.com/w/cpp/container/array/tuple_element
---


# tuple_elementsmall|<std::array>


```cpp
**Header:** `<`array`>`
dcl|since=c++11|1=
template< std::size_t I, class T, std::size_t N >
struct tuple_element< I, std::array<T, N> >;
```

Provides compile-time indexed access to the type of the elements of the array using tuple-like interface.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Possible implementation

eq fun
|1=
template<std::size_t I, class T>
struct tuple_element;
template<std::size_t I, class T, std::size_t N>
struct tuple_element<I, std::array<T,N>>
{
using type = T;
};

## Example


### Example

```cpp
#include <array>
#include <tuple>
#include <type_traits>

int main()
{
    // define array and get the type of the element at position 0
    std::array<int, 10> data{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    using T = std::tuple_element<0, decltype(data)>::type; // int
    static_assert(std::is_same_v<T, int>);

    const auto const_data = data;
    using CT = std::tuple_element<0, decltype(const_data)>::type; // const int

    // the result of tuple_element depends on the cv-qualification of the tuple-like type
    static_assert(!std::is_same_v<T, CT>);
    static_assert(std::is_same_v<CT, const int>);
}
```


## See also


| cpp/language/dsc structured binding | (see dedicated page) |
| cpp/utility/tuple/dsc tuple_element | (see dedicated page) |
| cpp/utility/pair/dsc tuple_element | (see dedicated page) |


---
title: std::tuple_size<std::tuple>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/tuple/tuple_size
---


# tuple_sizesmall|<std::tuple>

ddcl|header=tuple|since=c++11|
template< class... Types >
struct tuple_size< std::tuple<Types...> >
: std::integral_constant<std::size_t, sizeof...(Types)> { };
Provides access to the number of elements in a tuple as a compile-time constant expression.

## Helper variable template

ddcl|since=c++17|1=
template< class T >
constexpr std::size_t tuple_size_v = tuple_size<T>::value;

## Example


### Example

```cpp
#include <iostream>
#include <tuple>

template <class T>
void test(T value)
{
    int a[std::tuple_size_v<T>]; // can be used at compile time

    std::cout << std::tuple_size<T>{} << ' ' // or at run time
              << sizeof a << ' '
              << sizeof value << '\n';
}

int main()
{
    test(std::make_tuple(1, 2, 3.14));
}
```


**Output:**
```
3 12 16
```


## See also


| cpp/language/dsc structured binding | (see dedicated page) |
| cpp/utility/dsc tuple_size | (see dedicated page) |
| cpp/utility/pair/dsc tuple_size | (see dedicated page) |
| cpp/container/array/dsc tuple_size | (see dedicated page) |
| cpp/ranges/subrange/dsc tuple_size | (see dedicated page) |
| cpp/utility/tuple/dsc get | (see dedicated page) |


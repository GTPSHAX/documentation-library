---
title: std::tuple_element<std::tuple>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/tuple/tuple_element
---


# tuple_elementsmall|<std::tuple>

ddcl|header=tuple|since=c++11|
template< std::size_t I, class... Types >
struct tuple_element< I, std::tuple<Types...> >;
Provides compile-time indexed access to the types of the elements of the tuple.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Possible implementation

eq fun
|1=
template<std::size_t I, class T>
struct tuple_element;
#ifndef __cpp_pack_indexing
// recursive case
template<std::size_t I, class Head, class... Tail>
struct tuple_element<I, std::tuple<Head, Tail...>>
: std::tuple_element<I - 1, std::tuple<Tail...>>
{ };
// base case
template<class Head, class... Tail>
struct tuple_element<0, std::tuple<Head, Tail...>>
{
using type = Head;
};
#else
// C++26 implementation using pack indexing
template<std::size_t I, class... Ts>
struct tuple_element<I, std::tuple<Ts...>>
{
using type = Ts...[I];
};
#endif

## Example


### Example

```cpp
#include <boost/type_index.hpp>
#include <cstddef>
#include <iostream>
#include <string>
#include <tuple>
#include <utility>

template<typename TupleLike, std::size_t I = 0>
void printTypes()
{
    if constexpr (I == 0)
        std::cout << boost::typeindex::type_id_with_cvr<TupleLike>() << '\n';

    if constexpr (I < std::tuple_size_v<TupleLike>)
    {
        using SelectedType = std::tuple_element_t<I, TupleLike>;

        std::cout << "  The type at index " << I << " is: "
                  << boost::typeindex::type_id_with_cvr<SelectedType>() << '\n';
        printTypes<TupleLike, I + 1>();
    }
}

struct MyStruct {};

using MyTuple = std::tuple<int, long&, const char&, bool&&,
                           std::string, volatile MyStruct>;

using MyPair = std::pair<char, bool&&>;

static_assert(std::is_same_v<std::tuple_element_t<0, MyPair>, char>);
static_assert(std::is_same_v<std::tuple_element_t<1, MyPair>, bool&&>);

int main()
{
    printTypes<MyTuple>();
    printTypes<MyPair>();
}
```


**Output:**
```
std::tuple<int, long&, char const&, bool&&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, MyStruct volatile>
  The type at index 0 is: int
  The type at index 1 is: long&
  The type at index 2 is: char const&
  The type at index 3 is: bool&&
  The type at index 4 is: std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >
  The type at index 5 is: MyStruct volatile
std::pair<char, bool&&>
  The type at index 0 is: char
  The type at index 1 is: bool&&
```


## See also


| cpp/language/dsc structured binding | (see dedicated page) |
| cpp/utility/dsc tuple_element | (see dedicated page) |


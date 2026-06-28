---
title: std::tuple_size<std:ranges::subrange>
type: Ranges
source: https://en.cppreference.com/w/cpp/ranges/subrange/tuple_size
---

ddcl|header=ranges|since=c++20|
template< class I, class S, ranges::subrange_kind K >
struct tuple_size<ranges::subrange<I, S, K>>
: std::integral_constant<std::size_t, 2> {};
The partial specialization of `cpp/utility/tuple_size|std::tuple_size` for `std::ranges::subrange` provides a compile-time way to obtain the number of components of a `subrange`, which is always 2, using tuple-like syntax. It is provided for structured binding support.

## Example


### Example

```cpp
#include <array>
#include <iostream>
#include <iterator>
#include <ranges>

int main()
{
    static_assert(2 == std::tuple_size_v<std::ranges::subrange<int*, int*>>);

    using array5 = std::array<int, 5>;

    static_assert(2 == std::tuple_size<std::ranges::subrange<
        array5::const_iterator, array5::const_iterator>>{});

    constexpr array5 a{1, 2, 3, 4, 5};

    std::ranges::subrange sub_a1{a};

    for (std::cout << "sub_a1: { "; int e : sub_a1)
        std::cout << e << ' ';
    std::cout << "}\n";

    std::ranges::subrange sub_a2{std::next(cbegin(a)), std::prev(cend(a))};

    const auto [first, last] = sub_a2;
    std::cout << "sub_a2 size = " << std::distance(first, last) << '\n';

    for (std::cout << "sub_a2: { "; int e : sub_a2)
        std::cout << e << ' ';
    std::cout << "}\n";
}
```


**Output:**
```
sub_a1: { 1 2 3 4 5 }
sub_a2 size = 3
sub_a2: { 2 3 4 }
```


## See also


| cpp/language/dsc structured binding | (see dedicated page) |
| cpp/utility/dsc tuple_size | (see dedicated page) |
| cpp/utility/tuple/dsc tuple_size | (see dedicated page) |
| cpp/utility/pair/dsc tuple_size | (see dedicated page) |
| cpp/container/array/dsc tuple_size | (see dedicated page) |
| cpp/ranges/subrange/dsc tuple_element | (see dedicated page) |


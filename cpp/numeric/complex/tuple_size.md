---
title: std::tuple_size<std::complex>
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/tuple_size
---


# tuple_sizesmall|<std::complex>

ddcl|header=complex|since=c++26|
template< class T >
struct tuple_size<std::complex<T>>
: std::integral_constant<std::size_t, 2> {};
The partial specialization of `cpp/utility/tuple_size|std::tuple_size` for `std::complex` provides a compile-time way to obtain the number of components of a `complex`, which is always `2`, using tuple-like syntax. It is provided for structured binding support.

## Notes


## Example


### Example

```cpp
#include <complex>

static_assert(std::tuple_size_v<std::complex<float>> == 2);

static_assert([]
{
    using namespace std::literals;
    auto [re, im] = -1.5 + 2.5i;
    return re == -1.5 && im == 2.5;
}());

static_assert([]
{
    using namespace std::literals;
    auto z = std::complex<double>{};
    auto& [re, im] = z;
    re = 1.0;
    im = 2.0;
    return z == 1.0 + 2.0i;
}());

int main() {}
```


## See also


| cpp/language/dsc structured binding | (see dedicated page) |
| cpp/utility/dsc tuple_size | (see dedicated page) |
| cpp/numeric/complex/dsc tuple_element | (see dedicated page) |
| cpp/numeric/complex/dsc get | (see dedicated page) |


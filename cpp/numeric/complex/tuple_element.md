---
title: std::tuple_element<std::complex>
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/tuple_element
---


# tuple_elementsmall|<std::complex>


```cpp
**Header:** `<`complex`>`
dcl|since=c++26|
template< std::size_t I, class T >
struct tuple_element<I, std::complex<T>>;
```

The partial specializations of `cpp/utility/tuple_element|std::tuple_element` for `std::complex` provide compile-time access to the underlying real and imaginary number type of a `complex`, using tuple-like syntax. They are provided for structured binding support. The program is ill-formed if `1=I >= 2`.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Notes


## Example


### Example

```cpp
#include <complex>
#include <type_traits>

static_assert([z = std::complex<float>()]
{
    using T = decltype(z);
    return
#if __cpp_lib_tuple_like >= 202311L
        std::is_same_v<std::tuple_element_t<0, T>, float> &&
        std::is_same_v<std::tuple_element_t<1, T>, float> &&
#endif
        std::is_same_v<T::value_type, float>;
}());

int main() {}
```


## See also


| cpp/language/dsc structured binding | (see dedicated page) |
| cpp/utility/dsc tuple_element | (see dedicated page) |
| cpp/numeric/complex/dsc tuple_size | (see dedicated page) |
| cpp/numeric/complex/dsc get | (see dedicated page) |


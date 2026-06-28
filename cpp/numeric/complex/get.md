---
title: std::get(std::complex)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/complex/get
---


# getpetty|(std::complex)


```cpp
**Header:** `<`complex`>`
dcl|num=1|since=c++26|
template< std::size_t I >
friend constexpr T& get( std::complex<T>& x );
dcl|num=2|since=c++26|
template< std::size_t I >
friend constexpr const T& get( const std::complex<T>& x );
dcl|num=3|since=c++26|
template< std::size_t I >
friend constexpr T&& get( std::complex<T>&& x );
dcl|num=4|since=c++26|
template< std::size_t I >
friend constexpr const T&& get( const std::complex<T>&& x );
```

Returns the reference to real or imaginary part from a `complex` when `1=I == 0` or `1=I == 1`, respectively. It is mainly provided for structured binding support.

## Parameters


### Parameters

- `x` - a `complex`

## Return value

@1-4@ A reference to the real or imaginary part from the stored one when `1=I == 0` or `1=I == 1`, respectively.

## Notes


## Example


### Example

```cpp
#include <complex>

static_assert([z = std::complex(1.0, 2.0)]
{
#if __cpp_lib_tuple_like >= 202311L
    return std::get<0>(z) == 1.0 and std::get<1>(z) == 2.0;
#else
    return z.real() == 1.0 and z.imag() == 2.0;
#endif
}());

int main() {}
```


## See also


| cpp/language/dsc structured binding | (see dedicated page) |
| cpp/utility/tuple/dsc get | (see dedicated page) |
| cpp/utility/pair/dsc get | (see dedicated page) |
| cpp/container/array/dsc get | (see dedicated page) |


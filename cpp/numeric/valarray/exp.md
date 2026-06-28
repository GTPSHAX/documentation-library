---
title: std::exp(std::valarray)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/exp
---


# expsmall|(std::valarray)

ddcl|header=valarray|1=
template< class T >
valarray<T> exp( const valarray<T>& va );
For each element in `va` computes ''e'' raised to the power equal to the value of the element.

## Parameters


### Parameters

- `va` - value array to apply the operation to

## Return value

Value array containing ''e'' raised by the values in `va`.

## Notes


## Possible implementation


## Example


### Example

```cpp
#include <complex>
#include <iostream>
#include <numbers>
#include <valarray>

int main()
{
    const double pi = std::numbers::pi;
    std::valarray<std::complex<double>> v =
    {
        {0, 0}, {0, pi / 2}, {0, pi}, {0, 3 * pi / 2}, {0, 2 * pi}
    };
    std::valarray<std::complex<double>> v2 = std::exp(v);
    for (std::cout << std::showpos << std::fixed; auto n : v2)
        std::cout << n << '\n';
}
```


**Output:**
```
(+1.000000,+0.000000)
(+0.000000,+1.000000)
(-1.000000,+0.000000)
(-0.000000,-1.000000)
(+1.000000,-0.000000)
```


## See also


| cpp/numeric/valarray/dsc log | (see dedicated page) |
| cpp/numeric/math/dsc exp | (see dedicated page) |
| cpp/numeric/complex/dsc exp | (see dedicated page) |


---
title: std::log10(std::valarray)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/log10
---


# log10small|(std::valarray)

ddcl|header=valarray|1=
template< class T >
valarray<T> log10( const valarray<T>& va );
For each element in `va` computes common (base 10) logarithm of the value of the element.

## Parameters


### Parameters

- `va` - value array to apply the operation to

## Return value

Value array containing common logarithms of the values in `va`.

## Notes


## Possible implementation


## Example


### Example

```cpp
#include <cmath>
#include <iomanip>
#include <iostream>
#include <valarray>

void show(char const* title, const std::valarray<float>& va)
{
    std::cout << title << " : " << std::right;
    for (float x : va)
        std::cout << std::setw(6) << x;
    std::cout << '\n';
}

int main()
{
    const std::valarray<float> n{-2.f, -1.f, 0.f, 1.f, 2.f, 3.f, INFINITY};
    const std::valarray<float> pow10{std::pow(10.f, n)};
    const std::valarray<float> log10_pow10{std::log10(pow10)};

    show("n      ", n);
    show("10ⁿ    ", pow10);
    show("lg(10ⁿ)", log10_pow10);
}
```


**Output:**
```
n       :     -2    -1     0     1     2     3   inf
10ⁿ     :   0.01   0.1     1    10   100  1000   inf
lg(10ⁿ) :     -2    -1     0     1     2     3   inf
```


## See also


| cpp/numeric/valarray/dsc log | (see dedicated page) |
| cpp/numeric/math/dsc log10 | (see dedicated page) |
| cpp/numeric/complex/dsc log10 | (see dedicated page) |


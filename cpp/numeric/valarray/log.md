---
title: std::log(std::valarray)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/log
---


# logsmall|(std::valarray)

ddcl|header=valarray|1=
template< class T >
valarray<T> log( const valarray<T>& va );
For each element in `va` computes natural logarithm of the value of the element.

## Parameters


### Parameters

- `va` - value array to apply the operation to

## Return value

Value array containing natural logarithms of the values in `va`.

## Notes


## Possible implementation


## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <valarray>

void show(char const* title, const std::valarray<double>& va)
{
    std::cout << title << " :" << std::right << std::fixed;
    for (double x : va)
        std::cout << std::setw(10) << x;
    std::cout << '\n';
}

int main()
{
    const std::valarray<double> n{0.0, 1.0, 2.0, 3.0};
    const std::valarray<double> exp_n{std::exp(n)};
    const std::valarray<double> log_exp_n{std::log(exp_n)};

    show("n      ", n);
    show("eⁿ     ", exp_n);
    show("log(eⁿ)", log_exp_n);
}
```


**Output:**
```
n       :  0.000000  1.000000  2.000000  3.000000
eⁿ      :  1.000000  2.718282  7.389056 20.085537
log(eⁿ) :  0.000000  1.000000  2.000000  3.000000
```


## See also


| cpp/numeric/valarray/dsc log10 | (see dedicated page) |
| cpp/numeric/valarray/dsc exp | (see dedicated page) |
| cpp/numeric/math/dsc log | (see dedicated page) |
| cpp/numeric/complex/dsc log | (see dedicated page) |


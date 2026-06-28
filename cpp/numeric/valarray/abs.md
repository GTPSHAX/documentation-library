---
title: std::abs(std::valarray)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/abs
---


# abssmall|(std::valarray)

ddcl|header=valarray|1=
template< class T >
valarray<T> abs( const valarray<T>& va );
Computes absolute value of each element in the value array.

## Parameters


### Parameters

- `va` - value array to apply the operation to

## Return value

Value array containing absolute values of the values in `va`.

## Notes


## Possible implementation


## Example


### Example

```cpp
#include <iostream>
#include <valarray>

int main()
{
    std::valarray<int> v{1, -2, 3, -4, 5, -6, 7, -8};
    std::valarray<int> v2 = std::abs(v);
    for (auto n : v2)
        std::cout << n << ' ';
    std::cout << '\n';
}
```


**Output:**
```
1 2 3 4 5 6 7 8
```


## See also


| cpp/numeric/math/dsc abs | (see dedicated page) |
| cpp/numeric/math/dsc fabs | (see dedicated page) |
| cpp/numeric/complex/dsc abs | (see dedicated page) |


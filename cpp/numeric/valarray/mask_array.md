---
title: std::mask_array
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/mask_array
---

ddcl|header=valarray|
template< class T > class mask_array;
`std::mask_array` is a helper template used by the `valarray subscript operator` with `std::valarray<bool>` argument. It has reference semantics and provides access to the subset of the valarray consisting of the elements whose indices correspond to `true` values in the `std::valarray<bool>` mask.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/numeric/valarray/array/dsc constructor|mask_array | (see dedicated page) |
| cpp/numeric/valarray/array/dsc destructor|mask_array | (see dedicated page) |
| cpp/numeric/valarray/array/dsc operator{{= | (see dedicated page) |
| cpp/numeric/valarray/array/dsc operator_arith|mask_array | (see dedicated page) |


## Example


### Example

```cpp
#include <iostream>
#include <valarray>

void println(auto rem, const auto& data)
{
    for (std::cout << rem; int n : data)
        std::cout << n << ' ';
    std::cout << '\n';
}

int main()
{
    std::valarray<int> data{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    println("Initial valarray: ", data);

    data[data > 5] = -1;
    // the type of data>5 is std::valarray<bool>
    // the type of data[data>5] is std::mask_array<int>

    println("After v[v>5]=-1:  ", data);
}
```


**Output:**
```
Initial valarray: 0 1 2 3 4 5 6 7 8 9
After v[v>5]=-1:  0 1 2 3 4 5 -1 -1 -1 -1
```


## See also


| cpp/numeric/simd/dsc simd_mask | (see dedicated page) |
| cpp/experimental/simd/dsc simd_mask | (see dedicated page) |


---
title: std::indirect_array
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/indirect_array
---


```cpp
**Header:** `<`valarray`>`
dcl|
template< class T > class indirect_array;
```

`std::indirect_array` is a helper template used by the valarray subscript operator with `std::valarray<std::size_t>` argument. It has reference semantics to a subset of the array whose indices specified by the `std::valarray<std::size_t>` object.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/numeric/valarray/array/dsc constructor|indirect_array | (see dedicated page) |
| cpp/numeric/valarray/array/dsc destructor|indirect_array | (see dedicated page) |
| cpp/numeric/valarray/array/dsc operator{{= | (see dedicated page) |
| cpp/numeric/valarray/array/dsc operator_arith|indirect_array | (see dedicated page) |


## Example


### Example

```cpp
#include <iostream>
#include <valarray>

int main()
{
    std::valarray<int> data{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    std::valarray<std::size_t> idx{0, 2, 4, 6, 8};

    std::cout << "Original valarray: ";
    for (int n : data)
        std::cout << n << ' ';
    std::cout << '\n';

    data[idx] += data[idx]; // double the values at indices 'idx'

    // the type of data[idx] is std::indirect_array<int>

    std::cout << "After indirect modification: ";
    for (int n : data)
        std::cout << n << ' ';
    std::cout << '\n';
}
```


**Output:**
```
Original valarray: 0 1 2 3 4 5 6 7 8 9 
After indirect modification: 0 1 4 3 8 5 12 7 16 9
```


---
title: deduction guides for std::valarray
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/deduction_guides
---


# deduction guides for tt|std::valarray


```cpp
**Header:** `<`valarray`>`
dcl|since=c++17|
template< typename T, std::size_t cnt >
valarray( const T(&)[cnt], std::size_t ) -> valarray<T>;
```

This deduction guide is provided for `std::valarray` to allow deduction from array and size (note that deduction from pointer and size is covered by the implicit guides).

## Example


### Example

```cpp
#include <iostream>
#include <valarray>

int main()
{
    int a[] = {1, 2, 3, 4};
    std::valarray va(a, 3); // uses explicit deduction guide
    for (int x : va)
        std::cout << x << ' ';
    std::cout << '\n';
}
```


**Output:**
```
1 2 3
```


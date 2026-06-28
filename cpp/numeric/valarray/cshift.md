---
title: std::valarray::cshift
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/cshift
---

ddcl|
valarray<T> cshift( int count ) const;
Returns a new valarray of the same size with elements whose positions are shifted circularly by `count` elements.
A non-negative value of `count` shifts the elements circularly left `count` places and a negative value of `count` shifts the elements circularly right `-count` places.

## Parameters


### Parameters

- `count` - number of positions to shift the elements by

## Return value

The resulting valarray with circularly shifted elements.

## Notes


## Example


### Example

```cpp
#include <print>
#include <valarray>

int main()
{
    const std::valarray<int> v{1, 2, 3, 4, 5, 6, 7, 8};
    std::println("{}", v);
    std::println("{} <- 3", v.cshift(3));
    std::println("{} <- 11", v.cshift(11));
    std::println("{} -> 2", v.cshift(-2));
    std::println("{} -> 10", v.cshift(-10));
}
```


**Output:**
```
[1, 2, 3, 4, 5, 6, 7, 8]
[4, 5, 6, 7, 8, 1, 2, 3] <- 3
[4, 5, 6, 7, 8, 1, 2, 3] <- 11
[7, 8, 1, 2, 3, 4, 5, 6] -> 2
[7, 8, 1, 2, 3, 4, 5, 6] -> 10
```


## Defect reports


## See also


| cpp/numeric/valarray/dsc shift | (see dedicated page) |


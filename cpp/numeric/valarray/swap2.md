---
title: std::swap(std::valarray)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/swap2
---


# swapsmall|(std::valarray)

ddcl|header=valarray|since=c++11|
template< class T >
void swap( std::valarray<T>& lhs, std::valarray<T>& rhs ) noexcept;
Specializes the `std::swap` algorithm for `std::valarray`. Swaps the contents of `lhs` and `rhs`. Calls `lhs.swap(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - valarrays whose contents to swap

## Return value

(none)

## Complexity

Constant.

## Example


### Example


**Output:**
```
Before swap:
x: {3, 1, 4, 1, 5}
y: {2, 7, 1, 8}
After swap:
x: {2, 7, 1, 8}
y: {3, 1, 4, 1, 5}
```


## See also


| cpp/numeric/valarray/dsc swap | (see dedicated page) |


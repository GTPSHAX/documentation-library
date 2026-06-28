---
title: std::slice
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/slice
---

ddcl|header=valarray|
class slice;
`std::slice` is the selector class that identifies a subset of `std::valarray` similar to [BLAS](https://en.wikipedia.org/wiki/BLAS) slice. An object of type `std::slice` holds three values: the starting index, the stride, and the total number of values in the subset. Objects of type `std::slice` can be used as indices with valarray's `operator[]`.

## Member functions

member|slice|

```cpp
dcl|num=1|
slice()
dcl|num=2|
slice( std::size_t start, std::size_t size, std::size_t stride );
dcl|num=3|
slice( const slice& other );
```

Constructs a new slice.
1. Default constructor. Equivalent to `slice(0, 0, 0)`. This constructor exists only to allow construction of arrays of slices.
2. Constructs a new slice with parameters `start`, `size`, `stride`. This slice will refer to `size` number of elements, each with the position:
:@@ $start + 0 * stride$
:@@ $start + 1 * stride$
:@@ $...$
:@@ $start + (size - 1) * stride$
3. Constructs a copy of `other`.

## Parameters


### Parameters

- `start` - the position of the first element
- `size` - the number of elements in the slice
- `stride` - the number of positions between successive elements in the slice
- `other` - another slice to copy
member|start, size, stride|

```cpp
dcl|num=1|
std::size_t start() const;
dcl|num=2|
std::size_t size() const;
dcl|num=3|
std::size_t stride() const;
```

Returns the parameters passed to the slice on construction - start, size and stride respectively.

## Parameters

(none)

## Return value

The parameters of the slice -- start, size and stride respectively.

## Complexity

Constant.

## Non-member functions


| cpp/numeric/valarray/slice|title=operator== | |

member|1=operator==|2=

```cpp
dcl|since=c++20|1=
friend bool operator==( const slice& lhs, const slice& rhs );
```

Checks if the parameters of `lhs` and `rhs` - start, size and stride are equal respectively.

## Parameters


### Parameters

- `lhs, rhs` - slices to compare

## Return value

`1=lhs.start() == rhs.start() && lhs.size() == rhs.size() && lhs.stride() == rhs.stride()`

## Example


### Example

```cpp
#include <iostream>
#include <valarray>

class Matrix
{
    std::valarray<int> data;
    int dim;
public:
    Matrix(int r, int c) : data(r*c), dim(c) {}
    int& operator()(int r, int c) { return data[r * dim + c]; }
    int trace() const { return data[std::slice(0, dim, dim + 1)].sum(); }
};

int main()
{
    Matrix m(3, 3);
    int n = 0;
    for (int r = 0; r < 3; ++r)
       for (int c = 0; c < 3; ++c)
           m(r, c) = ++n;
    std::cout << "Trace of the matrix (1,2,3) (4,5,6) (7,8,9) is " << m.trace() << '\n';
}
```


**Output:**
```
Trace of the matrix (1,2,3) (4,5,6) (7,8,9) is 15
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-543 | C++98 | it was unclear whether a default constructed slice is usable | it is usable (as an empty subset) |


## See also


| cpp/numeric/valarray/dsc operator_at | (see dedicated page) |
| cpp/numeric/valarray/dsc gslice | (see dedicated page) |
| cpp/numeric/valarray/dsc slice_array | (see dedicated page) |
| cpp/container/dsc mdspan | (see dedicated page) |


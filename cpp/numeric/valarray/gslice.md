---
title: std::gslice
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/gslice
---

ddcl|header=valarray|
class gslice;
`std::gslice` is the selector class that identifies a subset of `std::valarray` indices defined by a multi-level set of strides and sizes. Objects of type `std::gslice` can be used as indices with valarray's `operator[]` to select, for example, columns of a multidimensional array represented as a `valarray`.
Given the starting value $s$, a list of strides $i and a list of sizes $d, a `std::gslice` constructed from these values selects the set of indices $k.
For example, a gslice with starting index `3`, strides `{19,4,1`} and lengths `{2,4,3`} generates the following set of `24 indices:
cc|1=
3 + 0*19 + 0*4 + 0*1 = 3,
3 + 0*19 + 0*4 + 1*1 = 4,
3 + 0*19 + 0*4 + 2*1 = 5,
3 + 0*19 + 1*4 + 0*1 = 7,
3 + 0*19 + 1*4 + 1*1 = 8,
3 + 0*19 + 1*4 + 2*1 = 9,
3 + 0*19 + 2*4 + 0*1 = 11,
...
3 + 1*19 + 3*4 + 1*1 = 35,
3 + 1*19 + 3*4 + 2*1 = 36
It is possible to construct `std::gslice` objects that select some indices more than once: if the above example used the strides }, the indices would have been }. Such gslices may only be used as arguments to the const version of `std::valarray::operator[]`, otherwise the behavior is undefined.

## Member functions

member|gslice|

```cpp
dcl|num=1|
gslice()
dcl|num=2|
gslice( std::size_t start, const std::valarray<std::size_t>& sizes,
const std::valarray<std::size_t>& strides );
dcl|num=3|
gslice( const gslice& other );
```

Constructs a new generic slice.
1. Default constructor. Equivalent to `gslice(0, std::valarray<std::size_t>(), std::valarray<std::size_t>())`. This constructor exists only to allow construction of arrays of slices.
2. Constructs a new slice with parameters `start`, `sizes`, `strides`.
3. Constructs a copy of `other`.

## Parameters


### Parameters

- `start` - the position of the first element
- `sizes` - an array that defines the number of elements in each dimension
- `strides` - an array that defines the number of positions between successive elements in each dimension
- `other` - another slice to copy
member|start, size, stride|

```cpp
dcl|num=1|
std::size_t start() const;
dcl|num=2|
std::valarray<std::size_t> size() const;
dcl|num=3|
std::valarray<std::size_t> stride() const;
```

Returns the parameters passed to the slice on construction - start, sizes and strides respectively.

## Parameters

(none)

## Return value

The parameters of the slice -- start, sizes and strides respectively.

## Complexity

Constant.

## Example


### Example

```cpp
#include <iostream>
#include <valarray>

void test_print(std::valarray<int>& v, int planes, int rows, int cols)
{
    for (int r = 0; r < rows; ++r)
    {
        for (int z = 0; z < planes; ++z)
        {
            for (int c = 0; c < cols; ++c)
                std::cout << v[z * rows * cols + r * cols + c] << ' ';
            std::cout << "  ";
        }
        std::cout << '\n';
    }
}

int main()
{
    std::valarray<int> v = // 3d array: 2 x 4 x 3 elements
        {111,112,113 , 121,122,123 , 131,132,133 , 141,142,143,
         211,212,213 , 221,222,223 , 231,232,233 , 241,242,243};
    // int ar3d[2][4][3]
    std::cout << "Initial 2x4x3 array:\n";
    test_print(v, 2, 4, 3);

    // update every value in the first columns of both planes
    v[std::gslice(0, {2, 4}, {4 * 3, 3})] = 1; // two level one strides of 12 elements
                                               // then four level two strides of 3 elements

    // subtract the third column from the second column in the 1st plane
    v[std::gslice(1, {1, 4}, {4 * 3, 3})] -= v[std::gslice(2, {1, 4}, {4 * 3, 3})];

    std::cout << "\n" "After column operations:\n";
    test_print(v, 2, 4, 3);
}
```


**Output:**
```
Initial 2x4x3 array:
111 112 113   211 212 213
121 122 123   221 222 223
131 132 133   231 232 233
141 142 143   241 242 243

After column operations:
1 -1 113   1 212 213
1 -1 123   1 222 223
1 -1 133   1 232 233
1 -1 143   1 242 243
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-543 | C++98 | it was unclear whether a default constructed generic slice is usable | it is usable (as an empty subset) |


## See also


| cpp/numeric/valarray/dsc operator_at | (see dedicated page) |
| cpp/numeric/valarray/dsc slice | (see dedicated page) |
| cpp/numeric/valarray/dsc gslice_array | (see dedicated page) |


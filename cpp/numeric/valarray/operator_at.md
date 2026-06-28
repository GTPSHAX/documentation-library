---
title: std::valarray::operator[]
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/operator_at
---


```cpp
dcl|num=1|
const T&               operator[]( std::size_t pos ) const;
dcl|num=2|
T&                     operator[]( std::size_t pos );
dcl|num=3|
std::valarray<T>       operator[]( std::slice slicearr ) const;
dcl|num=4|
std::slice_array<T>    operator[]( std::slice slicearr );
dcl|num=5|
std::valarray<T>       operator[]( const std::gslice& gslicearr ) const;
dcl|num=6|
std::gslice_array<T>   operator[]( const std::gslice& gslicearr );
dcl|num=7|
std::valarray<T>       operator[]( const std::valarray<bool>& boolarr ) const;
dcl|num=8|
std::mask_array<T>     operator[]( const std::valarray<bool>& boolarr );
dcl|num=9|
std::valarray<T>       operator[]( const std::valarray<std::size_t>& indarr ) const;
dcl|num=10|
std::indirect_array<T> operator[]( const std::valarray<std::size_t>& indarr );
```

Retrieve single elements or portions of the array.
The `const` overloads that return element sequences create a new `std::valarray` object.
The non-`const` overloads return classes holding references to the array elements.
@1,2@
@3-10@ .

## Parameters


### Parameters

- `pos` - position of the element to return
- `slicearr` - `slice` of the elements to return
- `gslicearr` - `gslice` of the elements to return
- `boolarr` - mask of the elements to return
- `indarr` - indices of the elements to return

## Return value

@1,2@ A reference to the corresponding element.
@3,5,7,9@ A `std::valarray` object containing copies of the selected items.
@4,6,8,10@ The corresponding data structure containing references to the selected items.

## Notes

For proper `std::valarray` values `a`, `b` and proper `std::size_t` values `i`, `j`, all of the following expressions always evaluate to `true`:
1. `1=(a[i] = q, a[i]) == q` for non-const `a`
2. `1=&a[i + j] == &a[i] + j`
*This means that `std::valarray` elements are adjacent in memory.
3. `1=&a[i] != &b[j]` for every objects `a` and `b` that are not aliases of one another
*This means that there are no aliases in the elements and this property can be used to perform some kinds of optimization.
References become invalid on `resize()` or when the array is destructed.
For overloads ,
Slice/mask/indirect index accesses do not chain: `1=v[v == n][std::slice(0, 5, 2)] = x;` is an error because `std::mask_array` (the type of `1=v[v == n]`) does not have `operator[]`.

## Example


### Example

```cpp
#include <cstddef>
#include <iomanip>
#include <iostream>
#include <valarray>

int main() 
{
    std::valarray<int> data = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    std::cout << "Initial valarray:   ";
    for (int n : data)
        std::cout << std::setw(3) << n;
    std::cout << '\n';

    data[data > 5] = -1; // valarray<bool> overload of operator[]
    // the type of data > 5 is std::valarray<bool>
    // the type of data[data > 5] is std::mask_array<int>

    std::cout << "After v[v > 5] = -1:";
    for (std::size_t n = 0; n < data.size(); ++n) 
        std::cout << std::setw(3) << data[n]; // regular operator[]
    std::cout << '\n';
}
```


**Output:**
```
Initial valarray:     0  1  2  3  4  5  6  7  8  9
After v[v > 5] = -1:  0  1  2  3  4  5 -1 -1 -1 -1
```


## Defect reports


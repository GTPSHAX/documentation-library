---
title: std::valarray::operator=
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/operator=
---


```cpp
dcl|num=1|1=
valarray<T>& operator=( const valarray<T>& other );
dcl|num=2|since=c++11|1=
valarray<T>& operator=( valarray<T>&& other ) noexcept;
dcl|num=3|1=
valarray<T>& operator=( const T& val );
dcl|num=4|1=
valarray<T>& operator=( const std::slice_array<T>& other );
dcl|num=5|1=
valarray<T>& operator=( const std::gslice_array<T>& other );
dcl|num=6|1=
valarray<T>& operator=( const std::mask_array<T>& other );
dcl|num=7|1=
valarray<T>& operator=( const std::indirect_array<T>& other );
dcl|num=8|since=c++11|1=
valarray<T>& operator=( std::initializer_list<T> il );
```

Replaces the contents of the numeric array.
1. Copy assignment operator. If `1=size() != other.size()`, first resizes `*this` as if by `resize(other.size())`. Each element of `*this` is assigned the value of the corresponding element of `other`.
2. Move assignment operator. Replaces the contents of `*this` with those of `other`. The value of `other` is unspecified after this operation. The complexity of this operation may be linear if T has non-trivial destructors, but is usually constant otherwise.
3. Replaces each value in `*this` with a copy of `val`.
@4-7@ Replaces the contents of `*this` with the result of a generalized subscripting operation. The behavior is undefined if  does not equal the length of `other` or if any value on the left depends on the value on the right (e.g. `1=v = v[v > 2]`).
8. Assigns the contents of initializer list `il`. Equivalent to `1=*this = valarray(il)`.

## Parameters


### Parameters

- `other` - another numeric array (or a mask) to assign
- `val` - the value to initialize each element with
- `il` - initializer list to assign

## Return value

`*this`

## Exceptions

@1,3-8@

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <valarray>

void print(const char* rem, const std::valarray<int>& v)
{
    std::cout << std::left << std::setw(36) << rem << std::right;
    for (int n : v)
        std::cout << std::setw(3) << n;
    std::cout << '\n';
}

int main()
{
    std::valarray<int> v1(3);
    v1 = -1; // (3) from a scalar 
    print("assigned from scalar: ", v1);

    v1 = {1, 2, 3, 4, 5, 6}; // (8): from initializer list of different size
    print("assigned from initializer_list:", v1);

    std::valarray<int> v2(3);
    v2 = v1[std::slice(0, 3, 2)]; // (4): from slice array
    print("every 2nd element starting at pos 0:", v2);

    v2 = v1[v1 % 2 == 0]; // (6): from mask array
    print("values that are even:", v2);

    std::valarray<std::size_t> idx = {0, 1, 2, 4}; // index array
    v2.resize(4); // sizes must match when assigning from gen subscript
    v2 = v1[idx]; // (7): from indirect array
    print("values at positions 0, 1, 2, 4:", v2);
}
```


**Output:**
```
assigned from scalar:                -1 -1 -1
assigned from initializer_list:       1  2  3  4  5  6
every 2nd element starting at pos 0:  1  3  5
values that are even:                 2  4  6
values at positions 0, 1, 2, 4:       1  2  3  5
```


## Defect reports


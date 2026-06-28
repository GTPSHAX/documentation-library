---
title: std::valarray::valarray
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/valarray
---


```cpp
dcl|num=1|
valarray();
dcl|num=2|
explicit valarray( std::size_t count );
dcl|num=3|
valarray( const T& val, std::size_t count );
dcl|num=4|
valarray( const T* vals, std::size_t count );
dcl|num=5|
valarray( const valarray& other );
dcl|num=6|since=c++11|
valarray( valarray&& other ) noexcept;
dcl|num=7|
valarray( const std::slice_array<T>& sa );
dcl|num=8|
valarray( const std::gslice_array<T>& gsa );
dcl|num=9|
valarray( const std::mask_array<T>& ma );
dcl|num=10|
valarray( const std::indirect_array<T>& ia );
dcl|num=11|since=c++11|
valarray( std::initializer_list<T> il );
```

Constructs new numeric array from various sources.
1. Default constructor. Constructs an empty numeric array.
2. Constructs a numeric array with `count` copies of value-initialized elements.
3. Constructs a numeric array with `count` copies of `val`.
4. Constructs a numeric array with copies of `count` values from an array pointed to by `vals`. If this array contains less than `count` values, the behavior is undefined.
5. Copy constructor. Constructs the numeric array with the copy of the contents of `other`.
6. Move constructor. Constructs the container with the contents of `other` using move semantics.
@7-10@ Converting constructor. Convert the corresponding data structure to a `valarray`.
11. Constructs the numeric array with the contents of the initializer list `il`.

## Parameters


### Parameters

- `count` - the number of elements to construct
- `val` - the value to initialize the elements with
- `vals` - pointer to a C array to use as source to initialize the contents
- `other` - another numeric array to use as source to initialize the contents
- `sa` - slice array to initialize the elements with
- `gsa` - generic slice array to initialize the elements with
- `ma` - mask array to initialize the elements with
- `ia` - indirect array to initialize the elements with
- `il` - initializer list to initialize the elements with

## Exceptions

@1-5, 7-11@

## Example


---
title: operators (std::valarray)
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/operator_cmp
---


# 1=operator==,!=,<,<=,>,>=small|(std::valarray)


```cpp
**Header:** `<`valarray`>`
dcl|num=1|1=
template< class T >
std::valarray<bool> operator==( const std::valarray<T>& lhs, const std::valarray<T>& rhs );
template< class T >
std::valarray<bool> operator!=( const std::valarray<T>& lhs, const std::valarray<T>& rhs );
template< class T >
std::valarray<bool> operator< ( const std::valarray<T>& lhs, const std::valarray<T>& rhs );
template< class T >
std::valarray<bool> operator<=( const std::valarray<T>& lhs, const std::valarray<T>& rhs );
template< class T >
std::valarray<bool> operator> ( const std::valarray<T>& lhs, const std::valarray<T>& rhs );
template< class T >
std::valarray<bool> operator>=( const std::valarray<T>& lhs, const std::valarray<T>& rhs );
dcl|num=2|1=
template< class T >
std::valarray<bool> operator==( const typename std::valarray<T>::value_type & lhsv,
const std::valarray<T>& rhs );
template< class T >
std::valarray<bool> operator!=( const typename std::valarray<T>::value_type & lhsv,
const std::valarray<T>& rhs );
template< class T >
std::valarray<bool> operator< ( const typename std::valarray<T>::value_type & lhsv,
const std::valarray<T>& rhs );
template< class T >
std::valarray<bool> operator<=( const typename std::valarray<T>::value_type & lhsv,
const std::valarray<T>& rhs );
template< class T >
std::valarray<bool> operator> ( const typename std::valarray<T>::value_type & lhsv,
const std::valarray<T>& rhs );
template< class T >
std::valarray<bool> operator>=( const typename std::valarray<T>::value_type & lhsv,
const std::valarray<T>& rhs );
dcl|num=3|1=
template< class T >
std::valarray<bool> operator==( const std::valarray<T>& lhs,
const typename std::valarray<T>::value_type & rhsv );
template< class T >
std::valarray<bool> operator!=( const std::valarray<T>& lhs,
const typename std::valarray<T>::value_type & rhsv );
template< class T >
std::valarray<bool> operator< ( const std::valarray<T>& lhs,
const typename std::valarray<T>::value_type & rhsv );
template< class T >
std::valarray<bool> operator<=( const std::valarray<T>& lhs,
const typename std::valarray<T>::value_type & rhsv );
template< class T >
std::valarray<bool> operator> ( const std::valarray<T>& lhs,
const typename std::valarray<T>::value_type & rhsv );
template< class T >
std::valarray<bool> operator>=( const std::valarray<T>& lhs,
const typename std::valarray<T>::value_type & rhsv );
```

Compares each value within the numeric array with another value.
1. Returns a numeric array of `bool` containing elements each of which is obtained by applying the indicated comparison operator to the corresponding values of `lhs` and `rhs`.
The behavior is undefined if `1=size() != v.size()`.
2. Returns a numeric array of `bool` containing elements each of which is obtained by applying the indicated comparison operator to `lhsv` and the corresponding value of `rhs`.
3. Returns a numeric array of `bool` containing elements each of which is obtained by applying the indicated comparison operator to the corresponding value of `lhs` and `rhsv`.

## Parameters


### Parameters

- `lhs, rhs` - numeric arrays to compare
- `lhsv, rhsv` - values to compare to each element within a numeric array

## Return value

A numeric array of `bool` containing comparison results of corresponding elements.

## Notes

Each of the operators can only be instantiated if the following requirements are met:
:* The indicated operator can be applied to type `T`.
:* The result value can be unambiguously converted to `bool`.

## Example


### Example

```cpp
#include <iostream>
#include <valarray>

int main()
{
    // zero all negatives in a valarray
    std::valarray<int> v = {1, -1, 0, -3, 10, -1, -2};
    std::cout << "Before: ";
    for (auto n : v)
        std::cout << n << ' ';
    std::cout << '\n';
    v[v < 0] = 0;
    std::cout << "After: ";
    for (auto n : v)
        std::cout << n << ' ';
    std::cout << '\n';

    // convert the valarray<bool> result of == to a single bool
    std::valarray<int> a = {1, 2, 3};
    std::valarray<int> b = {2, 4, 6};

    std::cout << "2*a == b is " << std::boolalpha
              << (2 * a == b).min() << '\n';
}
```


**Output:**
```
Before: 1 -1 0 -3 10 -1 -2
After: 1 0 0 0 10 0 0
2*a == b is true
```


## Defect reports


---
title: std::minmax
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/minmax
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|since=c++11|constexpr=c++14|
template< class T >
std::pair<const T&, const T&> minmax( const T& a, const T& b );
dcla|num=2|since=c++11|constexpr=c++14|
template< class T, class Compare >
std::pair<const T&, const T&> minmax( const T& a, const T& b,
Compare comp );
dcla|num=3|since=c++11|constexpr=c++14|
template< class T >
std::pair<T, T> minmax( std::initializer_list<T> ilist );
dcla|num=4|since=c++11|constexpr=c++14|
template< class T, class Compare >
std::pair<T, T> minmax( std::initializer_list<T> ilist,
Compare comp );
```

Returns the lowest and the greatest of the given values.
@1,2@ Returns references to the smaller and the greater of `a` and `b`.
:@1@ Uses `operator<` to compare the values.
:@@ If `T` is not *LessThanComparable*, the behavior is undefined.
:@2@ Use the comparison function `comp` to compare the values.
@3,4@ Returns the smallest and the greatest of the values in initializer list `ilist`.
@@ If `ilist.size()` is zero, or `T` is not *CopyConstructible*, the behavior is undefined.
:@3@ Uses `operator<` to compare the values.
:@@ If `T` is not *LessThanComparable*, the behavior is undefined.
:@4@ Use the comparison function `comp` to compare the values.

## Parameters


### Parameters

- `a, b` - the values to compare
- `ilist` - initializer list with the values to compare

## Return value

@1,2@ Returns the result of `std::pair<const T&, const T&>(a, b)` if `a < b` or if `a` is equivalent to `b`. Returns the result of `std::pair<const T&, const T&>(b, a)` if `b < a`.
@3,4@ A pair with the smallest value in `ilist` as the first element and the greatest as the second. If several elements are equivalent to the smallest, the leftmost such element is returned. If several elements are equivalent to the largest, the rightmost such element is returned.

## Complexity

1. Exactly one comparison using `operator<`.
2. Exactly one application of the comparison function `comp`.
@3,4@ Given  as `ilist.size()`:
:@3@ At most mathjax-or|\(\scriptsize \frac{3N}{2}\)| comparisons using `operator<`.
:@4@ At most mathjax-or|\(\scriptsize \frac{3N}{2}\)| applications of the comparison function `comp`.

## Possible implementation

eq impl
|title1=minmax (1)|ver1=1|1=
template<class T>
constexpr std::pair<const T&, const T&> minmax(const T& a, const T& b)
{
return (b < a) ? std::pair<const T&, const T&>(b, a)
: std::pair<const T&, const T&>(a, b);
}
|title2=minmax (2)|ver2=2|2=
template<class T, class Compare>
constexpr std::pair<const T&, const T&> minmax(const T& a, const T& b, Compare comp)
{
return comp(b, a) ? std::pair<const T&, const T&>(b, a)
: std::pair<const T&, const T&>(a, b);
}
|title3=minmax (3)|ver3=3|3=
template<class T>
constexpr std::pair<T, T> minmax(std::initializer_list<T> ilist)
{
auto p = std::minmax_element(ilist.begin(), ilist.end());
return std::pair(*p.first, *p.second);
}
|title4=minmax (4)|ver4=4|4=
template<class T, class Compare>
constexpr std::pair<T, T> minmax(std::initializer_list<T> ilist, Compare comp)
{
auto p = std::minmax_element(ilist.begin(), ilist.end(), comp);
return std::pair(*p.first, *p.second);
}

## Notes

For overloads , if one of the parameters is a temporary, the reference returned becomes a dangling reference at the end of the full expression that contains the call to `minmax`:

```cpp
int n = 1;
auto p = std::minmax(n, n + 1);
int m = p.first; // ok
int x = p.second; // undefined behavior

// Note that structured bindings have the same issue
auto [mm, xx] = std::minmax(n, n + 1);
xx; // undefined behavior
```


## Example


### Example

```cpp
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> v{3, 1, 4, 1, 5, 9, 2, 6};
    std::srand(std::time(0));
    std::pair<int, int> bounds = std::minmax(std::rand() % v.size(),
                                             std::rand() % v.size());

    std::cout << "v[" << bounds.first << "," << bounds.second << "]: ";
    for (int i = bounds.first; i < bounds.second; ++i)
        std::cout << v[i] << ' ';
    std::cout << '\n';
}
```


**Output:**
```
v[2,7]: 4 1 5 9 2
```


## Defect reports


## See also


| cpp/algorithm/dsc min | (see dedicated page) |
| cpp/algorithm/dsc max | (see dedicated page) |
| cpp/algorithm/dsc minmax_element | (see dedicated page) |
| cpp/algorithm/ranges/dsc minmax | (see dedicated page) |


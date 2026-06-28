---
title: std::valarray::apply
type: Numerics
source: https://en.cppreference.com/w/cpp/numeric/valarray/apply
---


```cpp
dcl|
valarray<T> apply( T func(T) ) const;
dcl|
valarray<T> apply( T func(const T&) ) const;
```

Returns a new valarray of the same size with values which are acquired by applying function `func` to the previous values of the elements.

## Parameters


### Parameters

- `func` - function to apply to the values

## Return value

The resulting valarray with values acquired by applying function `func`.

## Notes

===Possible implementation===
Following straightforward implementations can be replaced by expression templates for a higher efficiency.
eq fun|1=
template<class T>
valarray<T> valarray<T>::apply(T func(T)) const
{
valarray<T> other = *this;
for (T& i : other)
i = func(i);
return other;
}
template<class T>
valarray<T> valarray<T>::apply(T func(const T&)) const
{
valarray<T> other = *this;
for (T& i : other)
i = func(i);
return other;
}

## Example


### Example

```cpp
#include <cmath>
#include <iostream>
#include <valarray>

int main()
{
    std::valarray<int> v = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    v = v.apply([](int n) -> int
                {
                    return std::round(std::tgamma(n + 1));
                });
    for (auto n : v)
        std::cout << n << ' ';
    std::cout << '\n';
}
```


**Output:**
```
1 2 6 24 120 720 5040 40320 362880 3628800
```


## See also


| cpp/algorithm/dsc for_each | (see dedicated page) |
| cpp/algorithm/ranges/dsc for_each | (see dedicated page) |


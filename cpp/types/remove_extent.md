---
title: std::remove_extent
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/remove_extent
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|1=
template< class T >
struct remove_extent;
```

If `T` is an array of some type `X`, provides the member typedef `type` equal to `X`, otherwise `type` is `T`. Note that if T is a multidimensional array, only the first dimension is removed.

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types


```cpp
dcl|since=c++14|1=
template< class T >
using remove_extent_t = typename remove_extent<T>::type;
```


## Possible implementation

eq fun
|1=
template<class T>
struct remove_extent { using type = T; };
template<class T>
struct remove_extent<T[]> { using type = T; };
template<class T, std::size_t N>
struct remove_extent<T[N]> { using type = T; };

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <type_traits>

template<class A>
    std::enable_if_t<std::rank_v<A> == 1>
print_1d(const A& a)
{
    std::copy(a, a + std::extent_v<A>,
        std::ostream_iterator<std::remove_extent_t<A>>(std::cout, " "));
    std::cout << '\n';
}

int main()
{
    int a[][3] = {<!---->{1, 2, 3}, {4, 5, 6}<!---->};
//  print_1d(a); // compile-time error
    print_1d(a[1]);
}
```


**Output:**
```
4 5 6
```


## See also


| cpp/types/dsc is_array | (see dedicated page) |
| cpp/types/dsc rank | (see dedicated page) |
| cpp/types/dsc extent | (see dedicated page) |
| cpp/types/dsc remove_all_extents | (see dedicated page) |


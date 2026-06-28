---
title: std::remove_all_extents
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/remove_all_extents
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|1=
template< class T >
struct remove_all_extents;
```

If `T` is a multidimensional array of some type `X`, provides the member typedef `type` equal to `X`, otherwise `type` is `T`.

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types


```cpp
dcl|since=c++14|1=
template< class T >
using remove_all_extents_t = typename remove_all_extents<T>::type;
```


## Possible implementation

eq fun
|1=
template<class T>
struct remove_all_extents { typedef T type; };
template<class T>
struct remove_all_extents<T[]>
{
typedef typename remove_all_extents<T>::type type;
};
template<class T, std::size_t N>
struct remove_all_extents<T[N]>
{
typedef typename remove_all_extents<T>::type type;
};

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>
#include <typeinfo>

template<class A>
void info(const A&)
{
    typedef typename std::remove_all_extents<A>::type Type;
    std::cout << "underlying type: " << typeid(Type).name() << '\n';
}

int main()
{
    float a0;
    float a1[1][2][3];
    float a2[1][1][1][1][2];
    float* a3;
    int a4[3][2];
    double a5[2][3];
    struct X { int m; } x0[3][3];

    info(a0);
    info(a1);
    info(a2);
    info(a3);
    info(a4);
    info(a5);
    info(x0);
}
```


**Output:**
```
underlying type: float
underlying type: float
underlying type: float
underlying type: float*
underlying type: int
underlying type: double
underlying type: main::X
```


## See also


| cpp/types/dsc is_array | (see dedicated page) |
| cpp/types/dsc rank | (see dedicated page) |
| cpp/types/dsc extent | (see dedicated page) |
| cpp/types/dsc remove_extent | (see dedicated page) |


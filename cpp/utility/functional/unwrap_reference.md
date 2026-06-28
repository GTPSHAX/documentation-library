---
title: std::unwrap_reference
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/unwrap_reference
---


```cpp
**Header:** `<`type_traits`>`
**Header:** `<`functional`>`
dcl|num=1|since=c++20|
template< class T >
struct unwrap_reference;
dcl|num=2|since=c++20|
template< class T >
struct unwrap_ref_decay;
```

Unwraps any `std::reference_wrapper`: changing `std::reference_wrapper<U>` to `U&`.
1. If `T` is a specialization of `std::reference_wrapper`, unwraps it; otherwise, `T` remains the same.
2. If the decayed `T` is a specialization of `std::reference_wrapper`, unwraps it; otherwise, `T` is decayed.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| dsc|`type`| | |
| `U&` if `T` is `std::reference_wrapper<U>`; `T` otherwise<br> | |
| `U&` if `std::decay_t<T>` is `std::reference_wrapper<U>`; `std::decay_t<T>` otherwise | |


## Helper types


```cpp
dcl|num=1|since=c++20|1=
template<class T>
using unwrap_reference_t = unwrap_reference<T>::type;
dcl|num=2|since=c++20|1=
template<class T>
using unwrap_ref_decay_t = unwrap_ref_decay<T>::type;
```


## Possible implementation

eq fun|1=
template<class T>
struct unwrap_reference { using type = T; };
template<class U>
struct unwrap_reference<std::reference_wrapper<U>> { using type = U&; };
template<class T>
struct unwrap_ref_decay : std::unwrap_reference<std::decay_t<T>> {};

## Notes

`std::unwrap_ref_decay` performs the same transformation as used by `std::make_pair` and `std::make_tuple`.

## Example


### Example

```cpp
#include <cassert>
#include <functional>
#include <iostream>
#include <type_traits>

int main()
{
    static_assert(std::is_same_v<std::unwrap_reference_t<int>, int>);
    static_assert(std::is_same_v<std::unwrap_reference_t<const int>, const int>);
    static_assert(std::is_same_v<std::unwrap_reference_t<int&>, int&>);
    static_assert(std::is_same_v<std::unwrap_reference_t<int&&>, int&&>);
    static_assert(std::is_same_v<std::unwrap_reference_t<int*>, int*>);

    {
        using T = std::reference_wrapper<int>;
        using X = std::unwrap_reference_t<T>;
        static_assert(std::is_same_v<X, int&>);
    }
    {
        using T = std::reference_wrapper<int&>;
        using X = std::unwrap_reference_t<T>;
        static_assert(std::is_same_v<X, int&>);
    }

    static_assert(std::is_same_v<std::unwrap_ref_decay_t<int>, int>);
    static_assert(std::is_same_v<std::unwrap_ref_decay_t<const int>, int>);
    static_assert(std::is_same_v<std::unwrap_ref_decay_t<const int&>, int>);

    {
        using T = std::reference_wrapper<int&&>;
        using X = std::unwrap_ref_decay_t<T>;
        static_assert(std::is_same_v<X, int&>);
    }

    {
        auto reset = []<typename T>(T&& z)
        {
        //  x = 0; // Error: does not work if T is reference_wrapper<>
            // converts T&& into T& for ordinary types
            // converts T&& into U& for reference_wrapper<U>
            decltype(auto) r = std::unwrap_reference_t<T>(z);
            std::cout << "r: " << r << '\n';
            r = 0; // OK, r has reference type
        };

        int x = 1;
        reset(x);
        assert(x == 0);

        int y = 2;
        reset(std::ref(y));
        assert(y == 0);
    }
}
```


**Output:**
```
r: 1
r: 2
```


## See also


| cpp/utility/functional/dsc reference_wrapper | (see dedicated page) |
| cpp/utility/pair/dsc make_pair | (see dedicated page) |
| cpp/utility/tuple/dsc make_tuple | (see dedicated page) |


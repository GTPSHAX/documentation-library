---
title: std::remove_reference
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/remove_reference
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|1=
template< class T >
struct remove_reference;
```

If the type `T` is a reference type, provides the member typedef `type` which is the type referred to by `T`. Otherwise `type` is `T`.

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types


```cpp
dcl|since=c++14|1=
template< class T >
using remove_reference_t = typename remove_reference<T>::type;
```


## Possible implementation

eq fun
|1=
template<class T> struct remove_reference { typedef T type; };
template<class T> struct remove_reference<T&> { typedef T type; };
template<class T> struct remove_reference<T&&> { typedef T type; };

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>

int main()
{
    std::cout << std::boolalpha;

    std::cout << "std::remove_reference<int>::type is int? "
              << std::is_same<int, std::remove_reference<int>::type>::value << '\n';
    std::cout << "std::remove_reference<int&>::type is int? "
              << std::is_same<int, std::remove_reference<int&>::type>::value << '\n';
    std::cout << "std::remove_reference<int&&>::type is int? "
              << std::is_same<int, std::remove_reference<int&&>::type>::value << '\n';
    std::cout << "std::remove_reference<const int&>::type is const int? "
              << std::is_same<const int,
                              std::remove_reference<const int&>::type>::value << '\n';
}
```


**Output:**
```
std::remove_reference<int>::type is int? true
std::remove_reference<int&>::type is int? true
std::remove_reference<int&&>::type is int? true
std::remove_reference<const int&>::type is const int? true
```


## See also


| cpp/types/dsc is_reference | (see dedicated page) |
| cpp/types/dsc add_reference | (see dedicated page) |
| cpp/types/dsc remove_cvref | (see dedicated page) |


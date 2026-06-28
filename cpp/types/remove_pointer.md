---
title: std::remove_pointer
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/remove_pointer
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|1=
template< class T >
struct remove_pointer;
```

Provides the member typedef `type` which is the type pointed to by `T`, or, if `T` is not a pointer, then `type` is the same as `T`.

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types


```cpp
dcl|since=c++14|1=
template< class T >
using remove_pointer_t = typename remove_pointer<T>::type;
```


## Possible implementation

eq fun
|1=
template<class T> struct remove_pointer { typedef T type; };
template<class T> struct remove_pointer<T*> { typedef T type; };
template<class T> struct remove_pointer<T* const> { typedef T type; };
template<class T> struct remove_pointer<T* volatile> { typedef T type; };
template<class T> struct remove_pointer<T* const volatile> { typedef T type; };

## Example


### Example

```cpp
#include <type_traits>

static_assert
(
    std::is_same_v<int, int> == true &&
    std::is_same_v<int, int*> == false &&
    std::is_same_v<int, int**> == false &&
    std::is_same_v<int, std::remove_pointer_t<int>> == true &&
    std::is_same_v<int, std::remove_pointer_t<int*>> == true &&
    std::is_same_v<int, std::remove_pointer_t<int**>> == false &&
    std::is_same_v<int, std::remove_pointer_t<int* const>> == true &&
    std::is_same_v<int, std::remove_pointer_t<int* volatile>> == true &&
    std::is_same_v<int, std::remove_pointer_t<int* const volatile>> == true
);

int main() {}
```


## See also


| cpp/types/dsc is_pointer | (see dedicated page) |
| cpp/types/dsc add_pointer | (see dedicated page) |


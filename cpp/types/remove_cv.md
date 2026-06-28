---
title: std::remove_const
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/remove_cv
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|num=1|1=
template< class T >
struct remove_cv;
dcl|since=c++11|num=2|1=
template< class T >
struct remove_const;
dcl|since=c++11|num=3|1=
template< class T >
struct remove_volatile;
```

Provides the member typedef `type` which is the same as `T`, except that its topmost cv-qualifiers are removed.
1. Removes the topmost `const`, or the topmost `volatile`, or both, if present.
2. Removes the topmost `const`.
3. Removes the topmost `volatile`.

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types


```cpp
dcl|since=c++14|1=
template< class T >
using remove_cv_t = typename remove_cv<T>::type;
dcl|since=c++14|1=
template< class T >
using remove_const_t = typename remove_const<T>::type;
dcl|since=c++14|1=
template< class T >
using remove_volatile_t = typename remove_volatile<T>::type;
```


## Possible implementation

eq fun
|1=
template<class T> struct remove_cv { typedef T type; };
template<class T> struct remove_cv<const T> { typedef T type; };
template<class T> struct remove_cv<volatile T> { typedef T type; };
template<class T> struct remove_cv<const volatile T> { typedef T type; };
template<class T> struct remove_const { typedef T type; };
template<class T> struct remove_const<const T> { typedef T type; };
template<class T> struct remove_volatile { typedef T type; };
template<class T> struct remove_volatile<volatile T> { typedef T type; };

## Example


### Example

```cpp
#include <type_traits>

template<typename U, typename V>
constexpr bool same = std::is_same_v<U, V>;

static_assert
(
    same<std::remove_cv_t<int>, int> &&
    same<std::remove_cv_t<const int>, int> &&
    same<std::remove_cv_t<volatile int>, int> &&
    same<std::remove_cv_t<const volatile int>, int> &&
    // remove_cv only works on types, not on pointers
    not same<std::remove_cv_t<const volatile int*>, int*> &&
    same<std::remove_cv_t<const volatile int*>, const volatile int*> &&
    same<std::remove_cv_t<const int* volatile>, const int*> &&
    same<std::remove_cv_t<int* const volatile>, int*>
);

int main() {}
```


## See also


| cpp/types/dsc is_const | (see dedicated page) |
| cpp/types/dsc is_volatile | (see dedicated page) |
| cpp/types/dsc add_cv | (see dedicated page) |
| cpp/types/dsc remove_cvref | (see dedicated page) |


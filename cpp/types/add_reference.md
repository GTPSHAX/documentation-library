---
title: std::add_lvalue_reference
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/add_reference
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|num=1|1=
template< class T >
struct add_lvalue_reference;
dcl|since=c++11|num=2|1=
template< class T >
struct add_rvalue_reference;
```

Creates an lvalue or rvalue reference type of `T`.
1. If `T` is a function type that has no cv- or ref- qualifier or an object type, provides a member typedef `type` which is `T&`. If `T` is an rvalue reference to some type `U`, then `type` is `U&`. Otherwise, `type` is `T`.
2. If `T` is a function type that has no cv- or ref- qualifier or an object type, provides a member typedef `type` which is `T&&`, otherwise `type` is `T`.

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types


```cpp
dcl|since=c++14|1=
template< class T >
using add_lvalue_reference_t = typename add_lvalue_reference<T>::type;
dcl|since=c++14|1=
template< class T >
using add_rvalue_reference_t = typename add_rvalue_reference<T>::type;
```


## Notes

These type transformations honor reference collapsing rules:
* `std::add_lvalue_reference<T&>::type` is `T&`
* `std::add_lvalue_reference<T&&>::type` is `T&`
* `std::add_rvalue_reference<T&>::type` is `T&`
* `std::add_rvalue_reference<T&&>::type` is `T&&`
The major difference to directly using `T&` is that `std::add_lvalue_reference<void>::type` is `void`, while `void&` leads to a compilation error.

## Possible implementation

eq fun
|1=
namespace detail
{
template<class T>
struct type_identity { using type = T; }; // or use std::type_identity (since C++20)
template<class T> // Note that `cv void&` is a substitution failure
auto try_add_lvalue_reference(int) -> type_identity<T&>;
template<class T> // Handle T = cv void case
auto try_add_lvalue_reference(...) -> type_identity<T>;
template<class T>
auto try_add_rvalue_reference(int) -> type_identity<T&&>;
template<class T>
auto try_add_rvalue_reference(...) -> type_identity<T>;
} // namespace detail
template<class T>
struct add_lvalue_reference
: decltype(detail::try_add_lvalue_reference<T>(0)) {};
template<class T>
struct add_rvalue_reference
: decltype(detail::try_add_rvalue_reference<T>(0)) {};

## Example


### Example

```cpp
#include <type_traits>

int main()
{
    using non_ref = int;

    using l_ref = typename std::add_lvalue_reference_t<non_ref>;
    static_assert(std::is_lvalue_reference_v<l_ref>);

    using r_ref = typename std::add_rvalue_reference_t<non_ref>;
    static_assert(std::is_rvalue_reference_v<r_ref>);

    using void_ref = std::add_lvalue_reference_t<void>;
    static_assert(!std::is_reference_v<void_ref>);
}
```


## Defect reports


## See also


| cpp/types/dsc is_reference | (see dedicated page) |
| cpp/types/dsc remove_reference | (see dedicated page) |
| cpp/types/dsc remove_cvref | (see dedicated page) |


---
title: std::add_pointer
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/add_pointer
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++11|1=
template< class T >
struct add_pointer;
```

If `T` is a reference type, then provides the member typedef `type` which is a pointer to the referred type.
Otherwise, if `T` names an object type, a function type that is not cv- or ref-qualified, or a (possibly cv-qualified) `void` type, provides the member typedef `type` which is the type `T*`.
Otherwise (if `T` is a cv- or ref-qualified function type), provides the member typedef `type` which is the type `T`.

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types


```cpp
dcl|since=c++14|1=
template< class T >
using add_pointer_t = typename add_pointer<T>::type;
```


## Possible implementation

eq fun
|1=
namespace detail
{
template<class T>
struct type_identity { using type = T; }; // or use std::type_identity (since C++20)
template<class T>
auto try_add_pointer(int)
-> type_identity<typename std::remove_reference<T>::type*>;  // usual case
template<class T>
auto try_add_pointer(...)
-> type_identity<T>;  // unusual case (cannot form std::remove_reference<T>::type*)
} // namespace detail
template<class T>
struct add_pointer : decltype(detail::try_add_pointer<T>(0)) {};

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>

template<typename F, typename Class>
void ptr_to_member_func_cvref_test(F Class::*)
{
    // F is an "abominable function type"
    using FF = std::add_pointer_t<F>;
    static_assert(std::is_same_v<F, FF>, "FF should be precisely F");
}

struct S
{
    void f_ref() & {}
    void f_const() const {}
};

int main()
{
    int i = 123;
    int& ri = i;
    typedef std::add_pointer<decltype(i)>::type IntPtr;
    typedef std::add_pointer<decltype(ri)>::type IntPtr2;
    IntPtr pi = &i;
    std::cout << "i = " << i << '\n';
    std::cout << "*pi = " << *pi << '\n';

    static_assert(std::is_pointer_v<IntPtr>, "IntPtr should be a pointer");
    static_assert(std::is_same_v<IntPtr, int*>, "IntPtr should be a pointer to int");
    static_assert(std::is_same_v<IntPtr2, IntPtr>, "IntPtr2 should be equal to IntPtr");

    typedef std::remove_pointer<IntPtr>::type IntAgain;
    IntAgain j = i;
    std::cout << "j = " << j << '\n';

    static_assert(!std::is_pointer_v<IntAgain>, "IntAgain should not be a pointer");
    static_assert(std::is_same_v<IntAgain, int>, "IntAgain should be equal to int");

    ptr_to_member_func_cvref_test(&S::f_ref);
    ptr_to_member_func_cvref_test(&S::f_const);
}
```


**Output:**
```
i = 123
*pi = 123
j = 123
```


## Defect reports


## See also


| cpp/types/dsc is_pointer | (see dedicated page) |
| cpp/types/dsc remove_pointer | (see dedicated page) |


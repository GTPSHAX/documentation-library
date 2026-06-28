---
title: std::is_pointer
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_pointer
---

cpp/types/traits/is|1=is_pointer
|description=
Checks whether `T` is a pointer to object or function (including pointer to `void`, but excluding pointer to member) or a cv-qualified version thereof. Provides the member constant `value` which is equal to `true`, if `T` is an object/function pointer type. Otherwise, `value` is equal to `false`.
|inherit_desc=`T` is a pointer type

## Possible implementation

eq fun
|1=
template<class T>
struct is_pointer : std::false_type {};
template<class T>
struct is_pointer<T*> : std::true_type {};
template<class T>
struct is_pointer<T* const> : std::true_type {};
template<class T>
struct is_pointer<T* volatile> : std::true_type {};
template<class T>
struct is_pointer<T* const volatile> : std::true_type {};

## Example


### Example

```cpp
#include <type_traits>

int main()
{
    struct A
    {
        int m;
        void f() {}
    };

    int A::*mem_data_ptr = &A::m;     // a pointer to member data
    void (A::*mem_fun_ptr)() = &A::f; // a pointer to member function

    static_assert(
           ! std::is_pointer<A>::value
        && ! std::is_pointer_v<A>    // same thing as above, but in C++17!
        && ! std::is_pointer<A>()    // same as above, using inherited operator bool
        && ! std::is_pointer<A>{}    // ditto
        && ! std::is_pointer<A>()()  // same as above, using inherited operator()
        && ! std::is_pointer<A>{}()  // ditto
        &&   std::is_pointer_v<A*>
        &&   std::is_pointer_v<A const* volatile>
        && ! std::is_pointer_v<A&>
        && ! std::is_pointer_v<decltype(mem_data_ptr)>
        && ! std::is_pointer_v<decltype(mem_fun_ptr)>
        &&   std::is_pointer_v<void*>
        && ! std::is_pointer_v<int>
        &&   std::is_pointer_v<int*>
        &&   std::is_pointer_v<int**>
        && ! std::is_pointer_v<int[10]>
        && ! std::is_pointer_v<std::nullptr_t>
        &&   std::is_pointer_v<void (*)()>
    );
}
```


## See also


| cpp/types/dsc is_member_pointer | (see dedicated page) |
| cpp/types/dsc is_member_object_pointer | (see dedicated page) |
| cpp/types/dsc is_member_function_pointer | (see dedicated page) |
| cpp/types/dsc is_array | (see dedicated page) |
| cpp/types/dsc is_scalar | (see dedicated page) |


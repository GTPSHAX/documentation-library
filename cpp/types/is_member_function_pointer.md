---
title: std::is_member_function_pointer
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_member_function_pointer
---

cpp/types/traits/is|1=is_member_function_pointer
|description=
Checks whether `T` is a non-static member function pointer. Provides the member constant `value` which is equal to `true`, if `T` is a non-static member function pointer type. Otherwise, `value` is equal to `false`.
|inherit_desc=`T` is a member function pointer type

## Possible implementation

eq fun
|1=
template<class T>
struct is_member_function_pointer_helper : std::false_type {};
template<class T, class U>
struct is_member_function_pointer_helper<T U::*> : std::is_function<T> {};
template<class T>
struct is_member_function_pointer
: is_member_function_pointer_helper<typename std::remove_cv<T>::type> {};

## Example


### Example

```cpp
#include <type_traits>

class A
{
public:
    void member() {}
};

int main()
{
    // fails at compile time if A::member is a data member and not a function
    static_assert(std::is_member_function_pointer<decltype(&A::member)>::value,
                  "A::member is not a member function."); 
}
```


## See also


| cpp/types/dsc is_pointer | (see dedicated page) |
| cpp/types/dsc is_member_object_pointer | (see dedicated page) |
| cpp/types/dsc is_member_pointer | (see dedicated page) |


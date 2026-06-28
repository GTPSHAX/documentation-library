---
title: std::is_member_pointer
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_member_pointer
---

cpp/types/traits/is|1=is_member_pointer
|description=
If `T` is pointer to non-static member object or a pointer to non-static member function, provides the member constant `value` equal `true`. For any other type, `value` is `false`.
|inherit_desc=`T` is a member pointer type

## Possible implementation

eq fun
|1=
template<class T>
struct is_member_pointer_helper : std::false_type {};
template<class T, class U>
struct is_member_pointer_helper<T U::*> : std::true_type {};
template<class T>
struct is_member_pointer : is_member_pointer_helper<typename std::remove_cv<T>::type> {};

## Example


### Example

```cpp
#include <cassert>
#include <type_traits>

static_assert(!std::is_member_pointer_v<int*>);

struct S
{
    int i{42};
    int foo() { return 0xF00; }
};
using mem_int_ptr_t = int S::*;
using mem_fun_ptr_t = int (S::*)();
static_assert(std::is_member_pointer_v<mem_int_ptr_t>);
static_assert(std::is_member_pointer_v<mem_fun_ptr_t>);

int main()
{
    S s;

    mem_int_ptr_t pm = &S::i;
    assert(s.i == s.*pm);

    mem_fun_ptr_t pmf = &S::foo;
    assert((s.*pmf)() == s.foo());
}
```


## See also


| cpp/types/dsc is_pointer | (see dedicated page) |
| cpp/types/dsc is_member_object_pointer | (see dedicated page) |
| cpp/types/dsc is_member_function_pointer | (see dedicated page) |


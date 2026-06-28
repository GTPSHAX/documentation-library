---
title: std::is_scalar
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_scalar
---

cpp/types/traits/is|1=is_scalar
|description=
If `T` is a scalar type, provides the member constant `value` equal `true`. For any other type, `value` is `false`.
|inherit_desc=`T` is a scalar type

## Notes

Each individual memory location in the C++ memory model, including the hidden memory locations used by language features (e.g. virtual table pointer), has scalar type (or is a sequence of adjacent bit-fields of non-zero length). Sequencing of side-effects in expression evaluation, inter-thread synchronization, and dependency ordering are all defined in terms of individual scalar objects.

## Possible implementation

eq fun
|1=
template<class T>
struct is_scalar : std::integral_constant<bool, std::is_arithmetic<T>::value
std::is_enum<T>::value
std::is_pointer<T>::value
std::is_member_pointer<T>::value
std::is_null_pointer<T>::value
#if __cpp_impl_reflection > 0
std::is_reflection_v<T>
#endif
>
{};

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>
#include <typeinfo>
#include <utility>

template<typename Head, typename... Tail>
void are_scalars(Head&& head, Tail&&... tail)
{
    using T = std::decay_t<decltype(head)>;

    std::cout << typeid(T).name() << " is "
              << (std::is_scalar_v<T> ? "" : "not ")
              << "a scalar\n";

    if constexpr (sizeof... (Tail))
    {
        are_scalars(std::forward<decltype(tail)>(tail)...);
    }
}

int main()
{
    struct S { int m; } s;
    int S::* mp = &S::m;
    enum class E { e };

    are_scalars(42, 3.14, E::e, "str", mp, nullptr, s);
}
```


**Output:**
```
int is a scalar
double is a scalar
main::E is a scalar
char const* is a scalar
int main::S::* is a scalar
nullptr is a scalar
main::S is not a scalar
```


## See also


| cpp/types/dsc is_arithmetic | (see dedicated page) |
| cpp/types/dsc is_enum | (see dedicated page) |
| cpp/types/dsc is_pointer | (see dedicated page) |
| cpp/types/dsc is_member_pointer | (see dedicated page) |


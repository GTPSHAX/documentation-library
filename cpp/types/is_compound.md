---
title: std::is_compound
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_compound
---

cpp/types/traits/is|1=is_compound
|description=
If `T` is a compound type (that is, array, function, object pointer, function pointer, member object pointer, member function pointer, reference, class, union, or enumeration, including any cv-qualified variants), provides the member constant `value` equal `true`. For any other type, `value` is `false`.
|inherit_desc=`T` is a compound type

## Notes

Compound types are the types that are constructed from fundamental types. Any C++ type is either fundamental or compound.

## Possible implementation

eq fun
|1=
template<class T>
struct is_compound : std::integral_constant<bool, !std::is_fundamental<T>::value> {};

## Example


### Example

```cpp
#include <type_traits>
#include <iostream>

static_assert(not std::is_compound_v<int>);
static_assert(std::is_compound_v<int*>);
static_assert(std::is_compound_v<int&>);

void f();
static_assert(std::is_compound_v<decltype(f)>);
static_assert(std::is_compound_v<decltype(&f)>);

static_assert(std::is_compound_v<char[100]>);

class C {};
static_assert(std::is_compound_v<C>);

union U {};
static_assert(std::is_compound_v<U>);

enum struct E { e };
static_assert(std::is_compound_v<E>);
static_assert(std::is_compound_v<decltype(E::e)>);

struct S
{
    int i : 8;
    int j;
    void foo();
};
static_assert(not std::is_compound_v<decltype(S::i)>);
static_assert(not std::is_compound_v<decltype(S::j)>);
static_assert(std::is_compound_v<decltype(&S::j)>);
static_assert(std::is_compound_v<decltype(&S::foo)>);

int main()
{
    std::cout << "All checks have passed\n";
}
```


## See also


| cpp/types/dsc is_fundamental | (see dedicated page) |
| cpp/types/dsc is_scalar | (see dedicated page) |
| cpp/types/dsc is_object | (see dedicated page) |
| cpp/types/dsc is_array | (see dedicated page) |


---
title: std::reference_constructs_from_temporary
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/reference_constructs_from_temporary
---

ddcl|header=type_traits|since=c++23|
template< class T, class U >
struct reference_constructs_from_temporary;
Let `V` be `std::remove_cv_t<U>` if `U` is a scalar type or ''cv'' `void`, or `U` otherwise. If `T` is a reference type, and given a hypothetic expression `e` such that `decltype(e)` is `V`, the variable definition `T ref(e);` is well-formed and binds a temporary object to `ref`, then provides the member constant `value` equal to `true`. Otherwise, `value` is `false`.
If `T` is an lvalue reference type to a const- but not volatile-qualified object type or an rvalue reference type, both `std::remove_reference_t<T>` and `std::remove_reference_t<U>` shall be complete types, ''cv'' `void`, or an ; otherwise the behavior is undefined.
If an instantiation of a template above depends, directly or indirectly, on an incomplete type, and that instantiation could yield a different result if that type were hypothetically completed, the behavior is undefined.

## Helper variable template

ddcl|since=c++23|1=
template< class T, class U >
inline constexpr bool reference_constructs_from_temporary_v =
std::reference_constructs_from_temporary<T, U>::value;

## Notes

`std::reference_constructs_from_temporary` can be used for rejecting some cases that always produce dangling references.
It is also possible to use member initializer list to reject binding a temporary object to a reference if the compiler has implemented `CWG1696`.

## Example


### Example

```cpp
#include <type_traits>

static_assert(std::reference_constructs_from_temporary_v<int&&, int> == true);
static_assert(std::reference_constructs_from_temporary_v<const int&, int> == true);
static_assert(std::reference_constructs_from_temporary_v<int&&, int&&> == false);
static_assert(std::reference_constructs_from_temporary_v<const int&, int&&> == false);
static_assert(std::reference_constructs_from_temporary_v<int&&, long&&> == true);
static_assert(std::reference_constructs_from_temporary_v<int&&, long> == true);

int main() {}
```


## See also


| cpp/types/dsc is_constructible | (see dedicated page) |
| cpp/utility/tuple/dsc constructor | (see dedicated page) |
| cpp/utility/pair/dsc constructor | (see dedicated page) |
| cpp/utility/dsc make_from_tuple | (see dedicated page) |


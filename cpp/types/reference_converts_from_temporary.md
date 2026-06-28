---
title: std::reference_converts_from_temporary
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/reference_converts_from_temporary
---

ddcl|header=type_traits|since=c++23|
template< class T, class U >
struct reference_converts_from_temporary;
Let `V` be `std::remove_cv_t<U>` if `U` is a scalar type or ''cv'' `void`, or `U` otherwise. If `T` is a reference type, and given a hypothetical expression `e` such that `decltype(e)` is `V`, the variable definition `1=T ref = e;` is well-formed and binds a temporary object to `ref`, then provides the member constant `value` equal to `true`. Otherwise, `value` is `false`.
If `T` is an lvalue reference type to a const- but not volatile-qualified object type or an rvalue reference type, both `std::remove_reference_t<T>` and `std::remove_reference_t<U>` shall be complete types, ''cv'' `void`, or an ; otherwise the behavior is undefined.
If an instantiation of a template above depends, directly or indirectly, on an incomplete type, and that instantiation could yield a different result if that type were hypothetically completed, the behavior is undefined.

## Helper variable template

ddcl|since=c++23|1=
template< class T, class U >
constexpr bool reference_converts_from_temporary_v =
std::reference_converts_from_temporary<T, U>::value;

## Notes

`std::reference_converts_from_temporary` can be used for rejecting some cases that always produce dangling references.

## Example


### Example

```cpp
#include <type_traits>

int main() {}

static_assert(
    std::reference_converts_from_temporary_v<int&&, int> == true &&
    std::reference_converts_from_temporary_v<const int&, int> == true &&
    std::reference_converts_from_temporary_v<int&&, int&&> == false &&
    std::reference_converts_from_temporary_v<const int&, int&&> == false &&
    std::reference_converts_from_temporary_v<int&&, long&&> == true &&
    std::reference_converts_from_temporary_v<int&&, long> == true);
```


## See also


| cpp/types/dsc is_convertible | (see dedicated page) |
| cpp/utility/functional/dsc invoke | (see dedicated page) |
| cpp/utility/functional/dsc bind | (see dedicated page) |
| cpp/utility/variant/dsc visit2 | (see dedicated page) |
| cpp/utility/functional/function/dsc constructor | (see dedicated page) |
| cpp/utility/functional/move_only_function/dsc constructor | (see dedicated page) |
| cpp/thread/packaged_task/dsc constructor | (see dedicated page) |


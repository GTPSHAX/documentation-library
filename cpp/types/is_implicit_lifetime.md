---
title: std::is_implicit_lifetime
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_implicit_lifetime
---

cpp/types/traits/is|1=is_implicit_lifetime
|std=c++23
|description=
If `T` is an implicit-lifetime type, provides the member constant `value` equal to `true`. For any other type, `value` is `false`.
The behavior is undefined if `T` is an incomplete type other than an array type or (possibly cv-qualified) `void`.
|inherit_desc=`T` is an implicit-lifetime type

## Notes


## Example


### Example

```cpp
// The following types are collectively called implicit-lifetime types:
// * scalar types:
//     * arithmetic types
//     * enumeration types
//     * pointer types
//     * pointer-to-member types
//     * std::nullptr_t
// * implicit-lifetime class types
//     * is an aggregate whose destructor is not user-provided
//     * has at least one trivial eligible constructor and a trivial,
//       non-deleted destructor
// * array types
// * cv-qualified versions of these types.
#include <type_traits>

static_assert(std::is_implicit_lifetime_v<int>); // arithmetic type is a scalar type
static_assert(std::is_implicit_lifetime_v<const int>); // cv-qualified a scalar type

enum E { e };
static_assert(std::is_implicit_lifetime_v<E>); // enumeration type is a scalar type
static_assert(std::is_implicit_lifetime_v<int*>); // pointer type is a scalar type
static_assert(std::is_implicit_lifetime_v<std::nullptr_t>); // scalar type

struct S { int x, y; };
// S is an implicit-lifetime class: an aggregate without user-provided destructor
static_assert(std::is_implicit_lifetime_v<S>);

static_assert(std::is_implicit_lifetime_v<int S::*>); // pointer-to-member

struct X { ~X() = delete; };
// X is not implicit-lifetime class due to deleted destructor
static_assert(!std::is_implicit_lifetime_v<X>);

static_assert(std::is_implicit_lifetime_v<int[8]>); // array type
static_assert(std::is_implicit_lifetime_v<volatile int[8]>); // cv-qualified array type

int main() {}
```


## See also


| cpp/types/dsc is_scalar | (see dedicated page) |
| cpp/types/dsc is_array | (see dedicated page) |
| cpp/types/dsc is_aggregate | (see dedicated page) |
| cpp/memory/dsc start_lifetime_as | (see dedicated page) |


---
title: std::is_scoped_enum
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_scoped_enum
---

cpp/types/traits/is|1=is_scoped_enum
|std=c++23
|description=
Checks whether `T` is a scoped enumeration type. Provides the member constant `value` which is equal to `true`, if `T` is a scoped enumeration type. Otherwise, `value` is equal to `false`.
|inherit_desc=`T` is a scoped enumeration type

## Notes


## Possible implementation

eq fun|1=
namespace detail
{
void test_conversion(...);          // selected when E is complete and scoped
void test_conversion(int) = delete; // selected when E is complete and unscoped
template<class E>
concept is_scoped_enum_impl =
std::is_enum_v<E> &&                        // checked first
requires { detail::test_conversion(E{}); }; // ill-formed before overload resolution
// when E is incomplete
} // namespace detail
template<class T>
struct is_scoped_enum : std::bool_constant<detail::is_scoped_enum_impl<T>> {};

## Example


### Example

```cpp
#include <type_traits>

static_assert(std::is_scoped_enum_v<int> == false);

class A {};
static_assert(std::is_scoped_enum_v<A> == false);

enum B { self_test = std::is_scoped_enum_v<B> };
static_assert(std::is_scoped_enum_v<B> == false);
static_assert(!self_test);

enum struct C { final, import, module };
static_assert(std::is_scoped_enum_v<C> == true);

enum class D : int { pre, post, override };
static_assert(std::is_scoped_enum_v<D> == true);

enum class E;
static_assert(std::is_scoped_enum_v<E> == true);

int main() {}
```


## See also


| cpp/types/dsc is_integral | (see dedicated page) |
| cpp/types/dsc is_arithmetic | (see dedicated page) |
| cpp/types/dsc is_scalar | (see dedicated page) |
| cpp/types/dsc is_enum | (see dedicated page) |


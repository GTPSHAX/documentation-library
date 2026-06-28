---
title: std::is_polymorphic
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_polymorphic
---

cpp/types/traits/is|1=is_polymorphic
|description=
If `T` is a polymorphic class (that is, a non-union class that declares or inherits at least one virtual function), provides the member constant `value` equal to `true`. For any other type, `value` is `false`.
If `T` is an incomplete non-union class type, the behavior is undefined.
|inherit_desc=`T` is a polymorphic class type

## Possible implementation

eq fun|1=
namespace detail
{
template<class T>
std::true_type detect_is_polymorphic(
decltype(dynamic_cast<const volatile void*>(static_cast<T*>(nullptr)))
);
template<class T>
std::false_type detect_is_polymorphic(...);
} // namespace detail
template<class T>
struct is_polymorphic : decltype(detail::detect_is_polymorphic<T>(nullptr)) {};

## Example


### Example

```cpp
#include <type_traits>

struct A { int m; };
static_assert(!std::is_polymorphic_v<A>);

struct B { virtual void foo(); };
static_assert(std::is_polymorphic_v<B>);

struct C : B {};
static_assert(std::is_polymorphic_v<C>);

struct D { virtual ~D() = default; };
static_assert(std::is_polymorphic_v<D>);

// Uses inheritance, but not the virtual keyword:
struct E : A {};
static_assert(!std::is_polymorphic_v<E>);

struct F : virtual A {};
static_assert(!std::is_polymorphic_v<F>);

struct AX : A {};
struct AY : A {};
struct XY : virtual AX, virtual AY {};
static_assert(!std::is_polymorphic_v<XY>);

int main() {}
```


## Defect reports


## See also


| cpp/types/dsc is_class | (see dedicated page) |
| cpp/types/dsc is_abstract | (see dedicated page) |
| cpp/types/dsc has_virtual_destructor | (see dedicated page) |


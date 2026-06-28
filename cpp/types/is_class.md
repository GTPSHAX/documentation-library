---
title: std::is_class
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_class
---

cpp/types/traits/is|1=is_class
|description=
Checks whether `T` is a non-union class type. Provides the member constant `value` which is equal to `true`, if `T` is a class type (but not union). Otherwise, `value` is equal to `false`.
|inherit_desc=`T` is a non-union class type

## Possible implementation

eq fun
|1=
namespace detail
{
template<class T>
std::integral_constant<bool, !std::is_union<T>::value> test(int T::*);
template<class>
std::false_type test(...);
}
template<class T>
struct is_class : decltype(detail::test<T>(nullptr)) {};

## Example


### Example

```cpp
#include <type_traits>

struct A {};
static_assert(std::is_class<A>::value);

class B {};
static_assert(std::is_class_v<B>);
static_assert(not std::is_class_v<B*>);
static_assert(not std::is_class_v<B&>);
static_assert(std::is_class_v<const B>);

enum class E {};
static_assert(not std::is_class<E>::value);

union U { class UC {}; };
static_assert(not std::is_class_v<U>);
static_assert(std::is_class_v<U::UC>);

static_assert(not std::is_class_v<int>);

static_assert(std::is_class_v<struct S>, "incomplete class");
static_assert(std::is_class_v<class C>, "incomplete class");

int main() {}
```


## See also


| cpp/types/dsc is_union | (see dedicated page) |


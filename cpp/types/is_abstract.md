---
title: std::is_abstract
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_abstract
---

cpp/types/traits/is|1=is_abstract
|description=
If `T` is an  (that is, a non-union class that declares or inherits at least one pure virtual function), provides the member constant `value` equal to `true`. For any other type, `value` is `false`.
If `T` is an incomplete non-union class type, the behavior is undefined.
|inherit_desc=`T` is an  type

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>

struct A { int m; };
static_assert(std::is_abstract_v<A> == false);

struct B { virtual void foo(); };
static_assert(std::is_abstract_v<B> == false);

struct C { virtual void foo() = 0; };
static_assert(std::is_abstract_v<C> == true);

struct D : C {};
static_assert(std::is_abstract_v<D> == true);

int main() {}
```


## Defect reports


## See also


| cpp/types/dsc is_class | (see dedicated page) |
| cpp/types/dsc is_polymorphic | (see dedicated page) |


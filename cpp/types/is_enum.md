---
title: std::is_enum
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_enum
---

cpp/types/traits/is|1=is_enum
|description=
Checks whether `T` is an enumeration type. Provides the member constant `value` which is equal to `true`, if `T` is an enumeration type. Otherwise, `value` is equal to `false`.
|inherit_desc=`T` is an enumeration type

## Example


### Example

```cpp
#include <type_traits>

struct A { enum E {}; };
static_assert(std::is_enum_v<A> == false);
static_assert(std::is_enum_v<A::E> == true);

enum E {};
static_assert(std::is_enum_v<E> == true);

enum class Ec : int {};
static_assert(std::is_enum_v<Ec> == true);

static_assert(std::is_enum_v<int> == false);

int main() {}
```


## See also


| cpp/types/dsc is_integral | (see dedicated page) |
| cpp/types/dsc is_arithmetic | (see dedicated page) |
| cpp/types/dsc is_scalar | (see dedicated page) |
| cpp/types/dsc is_scoped_enum | (see dedicated page) |


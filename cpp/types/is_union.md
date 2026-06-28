---
title: std::is_union
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_union
---

cpp/types/traits/is|1=is_union
|description=
Checks whether `T` is a union type. Provides the member constant `value`, which is equal to `true` if `T` is a union type. Otherwise, `value` is equal to `false`.
|inherit_desc=`T` is a union type

## Example


### Example

```cpp
#include <type_traits>

struct A {};
static_assert(!std::is_union_v<A>);

typedef union
{
    int a;
    float b;
} B;
static_assert(std::is_union_v<B>);

struct C { B d; };
static_assert(!std::is_union_v<C>);

static_assert(!std::is_union_v<int>);

int main() {}
```


## See also


| cpp/types/dsc is_class | (see dedicated page) |


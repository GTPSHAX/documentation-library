---
title: std::is_trivial
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_trivial
---

cpp/types/traits/is|1=is_trivial
|description=
If `T` is a trivial type, provides the member constant `value` equal to `true`. For any other type, `value` is `false`.
If `std::remove_all_extents_t<T>` is an incomplete type and not (possibly cv-qualified) `void`, the behavior is undefined.
|inherit_desc=`T` is a trivial type
|deprecated=c++26

## Example


### Example

```cpp
#include <type_traits>

struct A { int m; };
static_assert(std::is_trivial_v<A> == true);

struct B { B() {} };
static_assert(std::is_trivial_v<B> == false);

// The following class shows why std::is_trivial(_v) may be a pitfall.
class C
{
private:
    C() = default;
};

static_assert(std::is_trivial_v<C> == true);
static_assert(std::is_trivially_default_constructible_v<C> == false);

int main() {}
```


## Defect reports


## See also


| cpp/types/dsc is_trivially_copyable | (see dedicated page) |
| cpp/types/dsc is_default_constructible | (see dedicated page) |


---
title: std::is_standard_layout
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_standard_layout
---

cpp/types/traits/is|1=is_standard_layout
|description=
If `T` is a standard-layout type, provides the member constant `value` equal to `true`. For any other type, `value` is `false`.
If `std::remove_all_extents_t<T>` is an incomplete type and not (possibly cv-qualified) `void`, the behavior is undefined.
|inherit_desc=`T` is a standard-layout type

## Notes

A pointer to a standard-layout class may be converted (with `reinterpret_cast`) to a pointer to its first non-static data member (see empty base optimization) and vice versa.
If a standard-layout union holds two or more standard-layout structs, it is permitted to inspect the common initial part of them.
The macro `offsetof` is only guaranteed to be usable with standard-layout classes.

## Example


### Example

```cpp
#include <type_traits>

struct A { int m; };
static_assert(std::is_standard_layout_v<A> == true);

class B: public A { int m; };
static_assert(std::is_standard_layout_v<B> == false);

struct C { virtual void foo(); };
static_assert(std::is_standard_layout_v<C> == false);

int main() {}
```


## Defect reports


## See also


| cpp/types/dsc is_trivially_copyable | (see dedicated page) |
| cpp/types/dsc is_pod | (see dedicated page) |
| cpp/types/dsc offsetof | (see dedicated page) |


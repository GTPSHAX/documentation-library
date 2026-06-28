---
title: std::is_pod
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_pod
---

cpp/types/traits/is|1=is_pod
|deprecated=c++20
|description=If `T` is a POD type ("plain old data type"), provides the member constant `value` equal to `true`. For any other type, `value` is `false`.
If `std::remove_all_extents_t<T>` is an incomplete type and not (possibly cv-qualified) `void`, the behavior is undefined.
|inherit_desc= `T` is a POD type

## Example


### Example

```cpp
#include <type_traits>

struct A { int m; };
static_assert(std::is_pod_v<A> == true);

class B: public A { int m; };
static_assert(std::is_pod_v<B> == false);

struct C { virtual void foo(); };
static_assert(std::is_pod_v<C> == false);

int main() {}
```


## Defect reports


## See also


| cpp/types/dsc is_standard_layout | (see dedicated page) |
| cpp/types/dsc is_trivial | (see dedicated page) |
| cpp/types/dsc is_scalar | (see dedicated page) |


## External links


---
title: std::is_literal_type
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_literal_type
---

cpp/types/traits/is|1=is_literal_type
|deprecated=c++17
|removed=c++20
|description=
(This type trait has been deprecated<ref></ref> and removed as offering negligible value to generic code.)
If `T` satisfies all requirements of *LiteralType*, provides the member constant `value` equal to `true`. For any other type, `value` is `false`.
If `std::remove_all_extents_t<T>` is an incomplete type and not (possibly cv-qualified) `void`, the behavior is undefined.
|inherit_desc= `T` is a literal type

## Notes

Only literal types may be used as parameters to or returned from s. Only literal classes may have constexpr member functions.

## Example


### Example

```cpp
#include <type_traits>

struct A { int m; };
static_assert(std::is_literal_type_v<A> == true);

struct B { virtual ~B(); };
static_assert(std::is_literal_type_v<B> == false);

int main() {}
```


## Defect reports


## External links


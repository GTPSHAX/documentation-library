---
title: std::has_virtual_destructor
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/has_virtual_destructor
---

cpp/types/traits/is|1=has_virtual_destructor
|description=
If `T` is a type with a virtual destructor, the base characteristic is `std::true_type`. For any other type, the base characteristic is `std::false_type`.
If `T` is an incomplete non-union class type, the behavior is undefined.
|inherit_desc=`T` has a virtual destructor

## Notes

If a class `C` has a public virtual destructor, it can be derived from, and the derived object can be safely deleted through a pointer to the base object ([http://www.gotw.ca/publications/mill18.htm  GotW #18]). In this case, `std::is_polymorphic<C>::value` is `true`.

## Example


### Example

```cpp
#include <type_traits>

struct S {};
static_assert(!std::has_virtual_destructor_v<S>);

struct B { virtual ~B() {} };
static_assert(std::has_virtual_destructor_v<B>);

struct D : B { ~D() {} };
static_assert(std::has_virtual_destructor_v<D>);

int main()
{
    B* pd = new D;
    delete pd;
}
```


## Defect reports


## See also


| cpp/types/dsc is_destructible | (see dedicated page) |
| cpp/types/dsc is_polymorphic | (see dedicated page) |


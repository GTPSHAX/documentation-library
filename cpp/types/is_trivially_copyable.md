---
title: std::is_trivially_copyable
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_trivially_copyable
---

cpp/types/traits/is|1=is_trivially_copyable
|description=
If `T` is a trivially copyable type, provides the member constant `value` equal to `true`. For any other type, `value` is `false`.
If `std::remove_all_extents_t<T>` is an incomplete type and not (possibly cv-qualified) `void`, the behavior is undefined.
|inherit_desc=`T` is a trivially copyable type

## Notes

Objects of trivially-copyable types that are not potentially-overlapping subobjects are the only C++ objects that may be safely copied with `std::memcpy` or serialized to/from binary files with  / .

## Example


### Example

```cpp
#include <type_traits>

struct A { int m; };
static_assert(std::is_trivially_copyable_v<A> == true);

struct B { B(B const&) {} };
static_assert(std::is_trivially_copyable_v<B> == false);

struct C { virtual void foo(); };
static_assert(std::is_trivially_copyable_v<C> == false);

struct D
{
    int m;

    D(D const&) = default; // -> trivially copyable
    D(int x) : m(x + 1) {}
};
static_assert(std::is_trivially_copyable_v<D> == true);

int main() {}
```


## Defect reports


## See also


| cpp/types/dsc is_trivial | (see dedicated page) |


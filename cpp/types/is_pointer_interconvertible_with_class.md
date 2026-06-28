---
title: std::is_pointer_interconvertible_with_class
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_pointer_interconvertible_with_class
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++20|
template< class S, class M >
constexpr bool is_pointer_interconvertible_with_class( M S::* mp ) noexcept;
```

Given an object `s` of type `S`, determines whether `s.*mp` refers to a subobject of `s` and `s` is pointer-interconvertible with its subobject `s.*mp`. The program is ill-formed if `S` is not a complete type.
If `S` is not a *StandardLayoutType*, or `M` is not an object type, or `mp` is equal to `nullptr`, the result is always `false`.

## Parameters


### Parameters

- `mp` - a pointer-to-member to detect

## Return value

`true` if `s.*mp` refers a subobject of `s` and `s` is pointer-interconvertible with its subobject `s.*mp`, otherwise `false`, where `s` is an object of type `S`.

## Notes

The type of a pointer-to-member expression `&S::m` is not always `M S::*`, where `m` is of type `M`, because `m` may be a member inherited from a base class of `S`. The template arguments can be specified in order to avoid potentially surprising results.
If there is a value `mp` of type `M S::*` such that `1=std::is_pointer_interconvertible_with_class(mp) == true`, then `reinterpret_cast<M&>(s)` has well-defined result and it refers the same subobject as `s.*mp`, where `s` is a valid lvalue of type `S`.
On common platforms, the bit pattern of `mp` is all zero if `1=std::is_pointer_interconvertible_with_class(mp) == true`.
feature test macro|__cpp_lib_is_pointer_interconvertible|value=201907L|std=C++20|Pointer-interconvertibility traits:
* `std::is_pointer_interconvertible_base_of`,
* `std::is_pointer_interconvertible_with_class`

## Example


### Example

```cpp
#include <type_traits>

struct Foo { int x; };
struct Bar { int y; };

struct Baz : Foo, Bar {}; // not standard-layout

static_assert( not std::is_same_v<decltype(&Baz::x), int Baz::*> );
static_assert( std::is_pointer_interconvertible_with_class(&Baz::x) );
static_assert( not std::is_pointer_interconvertible_with_class<Baz, int>(&Baz::x) );

int main() { }
```


## See also


| cpp/types/dsc is_standard_layout | (see dedicated page) |
| cpp/types/dsc is_member_object_pointer | (see dedicated page) |


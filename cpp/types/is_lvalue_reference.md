---
title: std::is_lvalue_reference
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_lvalue_reference
---

cpp/types/traits/is|1=is_lvalue_reference
|description=
Checks whether `T` is an lvalue reference type. Provides the member constant `value` which is equal to `true`, if `T` is an lvalue reference type. Otherwise, `value` is equal to `false`.
|inherit_desc=`T` is an lvalue reference type

## Possible implementation

eq fun
|1=
template<class T> struct is_lvalue_reference     : std::false_type {};
template<class T> struct is_lvalue_reference<T&> : std::true_type {};

## Example


### Example

```cpp
#include <type_traits>

class A {};
static_assert(std::is_lvalue_reference_v<A> == false);
static_assert(std::is_lvalue_reference_v<A&> == true);
static_assert(std::is_lvalue_reference_v<A&&> == false);

static_assert(std::is_lvalue_reference_v<int> == false);
static_assert(std::is_lvalue_reference_v<int&> == true);
static_assert(std::is_lvalue_reference_v<int&&> == false);

int main() {}
```


## See also


| cpp/types/dsc is_reference | (see dedicated page) |
| cpp/types/dsc is_rvalue_reference | (see dedicated page) |


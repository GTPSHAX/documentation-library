---
title: std::is_null_pointer
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_null_pointer
---

cpp/types/traits/is|1=is_null_pointer
|std=c++11
|description=
Checks whether `T` is the type `std::nullptr_t`.
Provides the member constant `value` that is equal to `true`, if `T` is the type `std::nullptr_t`, `const std::nullptr_t`, `volatile std::nullptr_t`, or `const volatile std::nullptr_t`.
Otherwise, `value` is equal to `false`.
|inherit_desc=`T` is the type `std::nullptr_t` (possibly cv-qualified)

## Possible implementation

eq fun
|1=
template<class T>
struct is_null_pointer : std::is_same<std::nullptr_t, std::remove_cv_t<T>> {};

## Notes

`std::is_pointer` is `false` for `std::nullptr_t` because it is not a built-in pointer type.
In libc++, `std::is_null_pointer` is not available in C++11 mode.

## Example


### Example

```cpp
#include <type_traits>

static_assert(std::is_null_pointer_v<decltype(nullptr)>);
static_assert(!std::is_null_pointer_v<int*>);
static_assert(!std::is_pointer_v<decltype(nullptr)>);
static_assert(std::is_pointer_v<int*>);

int main()
{
}
```


## Defect reports


## See also


| cpp/types/dsc is_void | (see dedicated page) |
| cpp/types/dsc is_array | (see dedicated page) |
| cpp/types/dsc is_pointer | (see dedicated page) |
| cpp/types/dsc is_enum | (see dedicated page) |
| cpp/types/dsc is_union | (see dedicated page) |
| cpp/types/dsc is_class | (see dedicated page) |
| cpp/types/dsc is_function | (see dedicated page) |
| cpp/types/dsc is_object | (see dedicated page) |


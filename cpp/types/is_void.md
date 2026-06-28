---
title: std::is_void
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_void
---

cpp/types/traits/is|1=is_void
|description=
Checks whether `T` is a void type. Provides the member constant `value` that is equal to `true`, if `T` is the type `void`, `const void`, `volatile void`, or `const volatile void`. Otherwise, `value` is equal to `false`.
|inherit_desc=`T` is the type `void` (possibly cv-qualified)

## Possible implementation

eq fun|
template<class T>
struct is_void : std::is_same<void, typename std::remove_cv<T>::type> {};

## Example


### Example

```cpp
#include <type_traits>

void foo();

static_assert
(
    std::is_void_v<void> == true and
    std::is_void_v<const void> == true and
    std::is_void_v<volatile void> == true and
    std::is_void_v<void*> == false and
    std::is_void_v<int> == false and
    std::is_void_v<decltype(foo)> == false and
    std::is_void_v<std::is_void<void>> == false
);

int main() {}
```


## See also


| cpp/types/dsc is_array | (see dedicated page) |
| cpp/types/dsc is_pointer | (see dedicated page) |
| cpp/types/dsc is_enum | (see dedicated page) |
| cpp/types/dsc is_union | (see dedicated page) |
| cpp/types/dsc is_class | (see dedicated page) |
| cpp/types/dsc is_function | (see dedicated page) |
| cpp/types/dsc is_object | (see dedicated page) |


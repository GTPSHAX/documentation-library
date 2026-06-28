---
title: std::is_final
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_final
---

cpp/types/traits/is|1=is_final
|std=c++14
|description=If `T` is a  class, provides the member constant `value` equal `true`. For any other type, `value` is `false`.
If `T` is an incomplete class type, the behavior is undefined.
|inherit_desc= `T` is a final class type

## Notes

`std::is_final` is introduced by the resolution of .
A  can be declared `final` (and `std::is_final` will detect that), even though unions cannot be used as bases in any case.

## Example


### Example

```cpp
#include <type_traits>

class A {};
static_assert(std::is_final_v<A> == false);

class B final {};
static_assert(std::is_final_v<B> == true);

union U final
{
    int x;
    double d;
};
static_assert(std::is_final_v<U> == true);

int main()
{
}
```


## See also


| cpp/types/dsc is_class | (see dedicated page) |
| cpp/types/dsc is_polymorphic | (see dedicated page) |


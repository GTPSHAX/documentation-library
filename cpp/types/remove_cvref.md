---
title: std::remove_cvref
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/remove_cvref
---


```cpp
**Header:** `<`type_traits`>`
dcl|since=c++20|1=
template< class T >
struct remove_cvref;
```

If the type `T` is a reference type, provides the member typedef `type` which is the type referred to by `T` with its topmost cv-qualifiers removed. Otherwise `type` is `T` with its topmost cv-qualifiers removed.

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types


```cpp
dcl|since=c++20|1=
template< class T >
using remove_cvref_t = remove_cvref<T>::type;
```


## Possible implementation

eq fun
|1=
template<class T>
struct remove_cvref
{
using type = std::remove_cv_t<std::remove_reference_t<T>>;
};

## Notes


## Example


### Example

```cpp
#include <type_traits>

int main()
{
    static_assert(std::is_same_v<std::remove_cvref_t<int>, int>);
    static_assert(std::is_same_v<std::remove_cvref_t<int&>, int>);
    static_assert(std::is_same_v<std::remove_cvref_t<int&&>, int>);
    static_assert(std::is_same_v<std::remove_cvref_t<const int&>, int>);
    static_assert(std::is_same_v<std::remove_cvref_t<const int[2]>, int[2]>);
    static_assert(std::is_same_v<std::remove_cvref_t<const int(&)[2]>, int[2]>);
    static_assert(std::is_same_v<std::remove_cvref_t<int(int)>, int(int)>);
}
```


## See also


| cpp/types/dsc remove_cv | (see dedicated page) |
| cpp/types/dsc remove_reference | (see dedicated page) |
| cpp/types/dsc decay | (see dedicated page) |


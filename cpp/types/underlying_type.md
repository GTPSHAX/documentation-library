---
title: std::underlying_type
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/underlying_type
---

ddcl|header=type_traits|since=c++11|
template< class T >
struct underlying_type;
If `T` is a complete enumeration (enum) type, provides a member typedef `type` that names the underlying type of `T`.
rrev multi|until1=c++20|rev1=
Otherwise, the behavior is undefined.
|rev2=
Otherwise, if `T` is not an enumeration type, there is no member `type`. Otherwise (`T` is an incomplete enumeration type), the program is ill-formed.

## Member types


| Item | Description |
|------|-------------|
| **Name** | Definition |


## Helper types


```cpp
dcl|since=c++14|1=
template< class T >
using underlying_type_t = typename underlying_type<T>::type;
```


## Notes

Each enumeration type has an ''underlying type'', which can be
# Specified explicitly (both scoped and unscoped enumerations);
# Omitted, in which case it is `int` for scoped enumerations or an implementation-defined integral type capable of representing all values of the enum (for unscoped enumerations).

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>

enum e1 {};
enum class e2 {};
enum class e3 : unsigned {};
enum class e4 : int {};

int main()
{
    constexpr bool e1_t = std::is_same_v<std::underlying_type_t<e1>, int>;
    constexpr bool e2_t = std::is_same_v<std::underlying_type_t<e2>, int>;
    constexpr bool e3_t = std::is_same_v<std::underlying_type_t<e3>, int>;
    constexpr bool e4_t = std::is_same_v<std::underlying_type_t<e4>, int>;

    std::cout
        << "underlying type for 'e1' is " << (e1_t ? "int" : "non-int") << '\n'
        << "underlying type for 'e2' is " << (e2_t ? "int" : "non-int") << '\n'
        << "underlying type for 'e3' is " << (e3_t ? "int" : "non-int") << '\n'
        << "underlying type for 'e4' is " << (e4_t ? "int" : "non-int") << '\n';
}
```


**Output:**
```
underlying type for 'e1' is non-int
underlying type for 'e2' is int
underlying type for 'e3' is non-int
underlying type for 'e4' is int
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2396 | C++11 | incomplete enumeration types were allowed | complete enumeration type required |


## See also


| cpp/types/dsc is_enum | (see dedicated page) |
| cpp/types/dsc is_scoped_enum | (see dedicated page) |
| cpp/utility/dsc to_underlying | (see dedicated page) |


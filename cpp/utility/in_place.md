---
title: std::in_place_type_t
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/in_place
---


```cpp
**Header:** `<`utility`>`
dcl|num=1|since=c++17|1=
struct in_place_t { explicit in_place_t() = default; };
dcl|num=2|since=c++17|1=
inline constexpr std::in_place_t in_place {};
dcl|num=3|since=c++17|1=
template< class T >
struct in_place_type_t { explicit in_place_type_t() = default; };
dcl|num=4|since=c++17|1=
template< class T >
constexpr std::in_place_type_t<T> in_place_type {};
dcl|num=5|since=c++17|1=
template< std::size_t I >
struct in_place_index_t { explicit in_place_index_t() = default; };
dcl|num=6|since=c++17|1=
template< std::size_t I >
constexpr std::in_place_index_t<I> in_place_index {};
```

@1,3,5@ The type/type templates `std::in_place_t`, `std::in_place_type_t` and `std::in_place_index_t` can be used in the constructor's parameter list to match the intended tag.
@2,4,6@ The corresponding `std::in_place`, `std::in_place_type`, and `std::in_place_index` instances of  are disambiguation tags that can be passed to the constructors to indicate that the contained object should be constructed in-place, and (for the latter two) the type of the object to be constructed.

## Standard library

The following standard library types use  as disambiguation tags:


| cpp/utility/dsc any | (see dedicated page) |
| cpp/utility/dsc expected | (see dedicated page) |
| cpp/utility/functional/dsc move_only_function | (see dedicated page) |
| cpp/utility/dsc optional | (see dedicated page) |
| cpp/utility/dsc variant | (see dedicated page) |


## See also


| cpp/container/dsc sorted_unique | (see dedicated page) |
| cpp/container/dsc sorted_equivalent | (see dedicated page) |


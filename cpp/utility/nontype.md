---
title: std::nontype_t
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/nontype
---


```cpp
**Header:** `<`utility`>`
dcl|num=1|since=c++26|1=
template< auto V >
struct nontype_t { explicit nontype_t() = default; };
dcl|num=2|since=c++26|1=
template< auto V >
constexpr std::nontype_t<V> nontype {};
```

1. The class template `std::nontype_t` can be used in the constructor's parameter list to match the intended tag.
2. The corresponding `std::nontype` instance of  is a disambiguation argument tag that can be passed to the constructors of `std::function_ref` to indicate that the contained object should be constructed with the value of the non-type template parameter `V`.

## Template parameters


### Parameters

- `V` - non-type template parameter of a structural type.

## See also


| cpp/utility/functional/dsc function_ref | (see dedicated page) |


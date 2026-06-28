---
title: std::function_ref::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/function_ref/operator=
---


```cpp
dcl|num=1|since=c++26|1=
constexpr function_ref& operator=( const function_ref& ) noexcept = default;
dcl|num=2|since=c++26|1=
template< class T >
constexpr function_ref& operator=( T ) = delete;
```

1. Copy assignment operator is explicitly-defaulted. `std::function_ref` satisfies  and *TriviallyCopyable*. This defaulted assignment operator performs a shallow copy of the stored  and .
2. User-defined assignment operator is explicitly-deleted if `T` is not the same type as `std::function_ref`, `std::is_pointer_v<T>` is `false`, and `T` is not a specialization of `std::nontype_t`. This overload participates in overload resolution only if the constraints are satisfied in the conditions above.

## Return value

`*this`

## See also


| cpp/utility/functional/function_ref/dsc constructor | (see dedicated page) |
| cpp/utility/functional/copyable_function/dsc operator{{= | (see dedicated page) |
| cpp/utility/functional/function/dsc operator{{= | (see dedicated page) |
| cpp/utility/functional/move_only_function/dsc operator{{= | (see dedicated page) |


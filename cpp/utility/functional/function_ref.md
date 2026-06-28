---
title: std::function_ref
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/function_ref
---


```cpp
**Header:** `<`functional`>`
dcl|num=1|since=c++26|
template< class... >
class function_ref; // not defined
dcl|num=2|since=c++26|
template< class R, class... Args >
class function_ref<R(Args...)>;
template< class R, class... Args >
class function_ref<R(Args...) noexcept>;
template< class R, class... Args >
class function_ref<R(Args...) const>;
template< class R, class... Args >
class function_ref<R(Args...) const noexcept>;
```

Class template `std::function_ref` is a non-owning function wrapper. `std::function_ref` objects can store and invoke reference to *Callable* ''target'' - functions, lambda expressions, bind expressions, or other function objects, but not pointers to member functions and pointers to member objects. `std::nontype` can be used to construct `std::function_ref` by passing function pointers, pointers to member functions, and pointers to member objects.
`std::function_ref`s supports every possible combination of cv-qualifiers (excluding `volatile`), and noexcept-specifiers provided in its template parameter.
Every specialization of `std::function_ref` is a *TriviallyCopyable* type that satisfies .

## Member types


| Item | Description |
|------|-------------|
| **Member** | Definition |
| dsc expos mem type|FunctionPointerType|private=yes| | |
| where *noex* is `true` if `noexcept` is present in function signature as part of the template parameter of `std::function_ref`, `false` otherwise | |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Definition |


## Member functions


| cpp/utility/functional/function_ref/dsc constructor | (see dedicated page) |
| cpp/utility/functional/function_ref/dsc operator{{= | (see dedicated page) |
| cpp/utility/functional/function_ref/dsc operator() | (see dedicated page) |


## 


## Notes


## Example


## See also


| cpp/utility/functional/dsc function | (see dedicated page) |
| cpp/utility/functional/dsc copyable_function | (see dedicated page) |
| cpp/utility/functional/dsc move_only_function | (see dedicated page) |
| cpp/utility/dsc nontype | (see dedicated page) |


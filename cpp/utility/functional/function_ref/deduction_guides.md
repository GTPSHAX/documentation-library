---
title: deduction guides for std::function_ref
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/function_ref/deduction_guides
---


# deduction guides for tt|std::function_ref


```cpp
**Header:** `<`functional`>`
dcl|num=1|since=c++26|
template< class F >
function_ref( F* ) -> function_ref<F>;
dcl|num=2|since=c++26|
template< auto f >
function_ref( std::nontype_t<f> ) -> function_ref</*see below*/>;
dcl|num=3|since=c++26|
template< auto f, class T >
function_ref( std::nontype_t<f>, T&& ) -> function_ref</*see below*/>;
```

1. .
2. Let type `F` be `std::remove_pointer_t<decltype(f)>`. . The deduced type is `std::function_ref<F>`.
3. Let type `F` be `decltype(f)`. cpp/enable_if|:
* `F` is of the form `R(G::*)(A...) noexcept(E)` (optionally cv-qualified, optionally noexcept, optionally lvalue reference qualified) for a type `G`, or
* `F` is of the form `M G::*` for a type `G` and an object type `M`, in which case let `R` be `std::invoke_result_t<F, T&>`, `A...` be an empty pack, and `E` be false, or
* `F` is of the form `R(*)(G, A...) noexcept(E)` for a type `G`.
::The deduced type is `std::function_ref<R(A...) noexcept(E)>`.

## Example


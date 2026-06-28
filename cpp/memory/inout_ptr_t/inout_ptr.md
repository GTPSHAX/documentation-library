---
title: std::inout_ptr
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/inout_ptr_t/inout_ptr
---

ddcla|header=memory|since=c++23|constexpr=c++26|1=
template< class Pointer = void, class Smart, class... Args >
auto inout_ptr( Smart& s, Args&&... args );
Returns an `inout_ptr_t` with deduced template arguments that captures arguments for resetting by reference.
.

## Parameters


### Parameters

- `s` - the object (typically a smart pointer) to adapt
- `args` - the arguments for resetting to capture

## Return value

`std::inout_ptr_t<Smart, P, Args&&>(s, std::forward<Args>(args)...)`, where `P` is
* `Pointer`, if `Pointer` is not same as `void`, otherwise,
* `Smart::pointer`, if it is valid and denotes a type, otherwise,
* `Smart::element_type*`, if `Smart::element_type` is valid and denotes a type, otherwise,
* `std::pointer_traits<Smart>::element_type*`.

## Notes

Users may specify the template argument for the template parameter `Pointer`, in order to interoperate with foreign functions that take a `Pointer*`.
As all arguments for resetting are captured by reference, the returned `inout_ptr_t` should be a temporary object destroyed at the end of the full-expression containing the call to the foreign function, in order to avoid dangling references.

## Example


---
title: std::out_ptr_t::operators (void**)
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/out_ptr_t/operator_ptr
---


```cpp
dcla|num=1|since=c++23|constexpr=c++26|
operator Pointer*() const noexcept;
dcla|num=2|since=c++23|
operator void**() const noexcept;
```

Exposes the address of a `Pointer` or `void*` object to a foreign function which will generally re-initialize it.
1. Converts `*this` to the address of stored `Pointer` object.
@@ .
2. Converts `*this` to the address of a `void*` object.
@@ .
@@ .
@@ Returns a pointer `ptr` satisfying all following conditions:
* The initial value of `*ptr` is equivalent to the value of the stored `Pointer` object converted to `void*`.
* Any modification of `*ptr` that is not followed by a subsequent modification of `*this` affects the `Pointer` value used in the `destructor`.
@@ .
@@ .

## Return value

1. A pointer to the stored `Pointer` object.
2. A pointer to the `void*` object that satisfies aforementioned requirements.

## Notes

If the object pointed by the return value has not been rewritten, it is equal to `nullptr`.
On common implementations, the object representation of every `Pointer` that is a pointer type is compatible with that of `void*`, and therefore these implementations typically store the `void*` object within the storage for the `Pointer` object, no additional storage needed:
* If the implementation enables type-based alias analysis (which relies on the strict aliasing rule), a properly aligned `std::byte[sizeof(void*)]` member subobject may be used, and both conversion functions return the address of objects implicitly created within the array.
* Otherwise, a `Pointer` member subobject may be used for both conversion functions, and `operator void**` may directly returns its address `cpp/language/reinterpret_cast` to `void**`.
If `Pointer` is a pointer type whose object representation is incompatible with that of `void*`, an additional `bool` flag may be needed for recording whether `operator Pointer*` (or `operator void**`) has been called.

## Example


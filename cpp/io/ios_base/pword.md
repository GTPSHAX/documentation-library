---
title: std::ios_base::pword
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ios_base/pword
---

ddcl|
void*& pword( int index );
First, allocates or resizes the private storage (dynamic array of `void*` or another indexable data structure) sufficiently to make `index` a valid index, then returns a reference to the `void*` element of the private storage with the index `index`.
The reference may be invalidated by any operation on this `ios_base` object, including another call to `pword()`, but the stored values are retained, so that reading from `pword(index)` with the same index later will produce the same value until the next call to `std::basic_ios::copyfmt()`. The value can be used for any purpose. The index of the element must be obtained by `xalloc()`, otherwise the behavior is undefined. New elements are initialized to a null pointer.
If the function fails (possibly caused by an allocation failure) and `*this` is a base class subobject of a `basic_ios<>` object or subobject, calls `std::basic_ios<>::setstate(badbit)` which may throw `std::ios_base::failure`.

## Parameters


### Parameters

- `index` - index value of the element

## Return value

A reference to the element.

## Exceptions

May throw `std::ios_base::failure` when setting the badbit.

## Notes

If the pointers stored in `pword` require management, `register_callback()` may be used to install handlers that execute deep copy or deallocation as needed.

## Example


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-36 | C++98 | the stored value might not be<br>retained if the reference is invalidated | the stored value is retained<br>until the next call of tt |


## See also


| cpp/io/ios_base/dsc iword | (see dedicated page) |
| cpp/io/ios_base/dsc xalloc | (see dedicated page) |


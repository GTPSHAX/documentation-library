---
title: std::return_temporary_buffer
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/return_temporary_buffer
---

ddcl|header=memory|deprecated=c++17|removed=c++20|
template< class T >
void return_temporary_buffer( T* p );
Deallocates the storage referenced by `p`.
If `p` is not a pointer value returned by an earlier call to `std::get_temporary_buffer`, or has been invalidated by an intervening `std::return_temporary_buffer` call, the behavior is undefined.

## Parameters


### Parameters

- `p` - the pointer referring to the storage to be declloated

## Return value

(none)

## Exceptions

Throws nothing.

## Example


## Defect reports


## See also


| cpp/memory/dsc get_temporary_buffer | (see dedicated page) |


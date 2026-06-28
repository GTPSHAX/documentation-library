---
title: std::declare_reachable
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/gc/declare_reachable
---

ddcl|header=memory|since=c++11|removed=c++23|
void declare_reachable( void* p );
Declares the object referenced by the pointer `p` reachable. Reachable objects will not be deleted by the garbage collector or considered to be a leak by a leak detector even if all pointers to it are destroyed. An object may be declared reachable multiple times, in which case multiple calls to `std::undeclare_reachable` would be needed to remove this property. For example, a [XOR linked list](https://en.wikipedia.org/wiki/XOR linked list) needs to declare its nodes reachable if the implementation has garbage collection enabled.

## Parameters


### Parameters

- `p` - a safely-derived pointer or a null pointer

## Return value

(none)

## Exceptions

May throw `std::bad_alloc` if the system cannot allocate memory required to track reachable objects.

## See also


| cpp/memory/gc/dsc undeclare_reachable | (see dedicated page) |


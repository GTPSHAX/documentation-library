---
title: std::undeclare_reachable
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/gc/undeclare_reachable
---

ddcl|header=memory|since=c++11|removed=c++23|
template< class T >
T* undeclare_reachable( T* p );
Removes the reachable status of the object, referenced by the pointer `p`, if it was previously set by `std::declare_reachable`. If the object was declared reachable multiple times, equal number of calls to `undeclare_reachable` would be needed to remove this status. Once the object is not declared reachable and has no pointers referencing it, it may be reclaimed by garbage collector or reported as a leak by a leak detector.

## Parameters


### Parameters

- `p` - a pointer to an object previously declared reachable and not destructed since then

## Return value

A safely-derived copy of `p`.

## Exceptions

Throws nothing.

## See also


| cpp/memory/gc/dsc declare_reachable | (see dedicated page) |


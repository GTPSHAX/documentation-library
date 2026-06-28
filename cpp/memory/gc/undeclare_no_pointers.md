---
title: std::undeclare_no_pointers
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/gc/undeclare_no_pointers
---

ddcl|header=memory|since=c++11|removed=c++23|
void undeclare_no_pointers( char *p, std::size_t n );
Unregisters a range earlier registered with `std::declare_no_pointers()`.

## Parameters


### Parameters

- `p` - pointer to the beginning of the range previously registered with `std::declare_no_pointers`
- `n` - the number of bytes in the range, same value as previously used with `std::declare_no_pointers`

## Return value

(none)

## Exceptions

Throws nothing.

## See also


| cpp/memory/gc/dsc declare_no_pointers | (see dedicated page) |


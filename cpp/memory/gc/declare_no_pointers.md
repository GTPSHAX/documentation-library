---
title: std::declare_no_pointers
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/gc/declare_no_pointers
---

ddcl|header=memory|since=c++11|removed=c++23|
void declare_no_pointers( char *p, std::size_t n );
Informs the garbage collector or leak detector that the specified memory region (`n` bytes beginning at the byte pointed to by `p`) contains no traceable pointers. If any part of the region is within an allocated object, the entire region must be contained in the same object.

## Parameters


### Parameters

- `p` - pointer to the beginning of the range
- `n` - the number of bytes in the range

## Return value

(none)

## Exceptions

Throws nothing.

## See also


| cpp/memory/gc/dsc undeclare_no_pointers | (see dedicated page) |


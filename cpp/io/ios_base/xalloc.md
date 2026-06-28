---
title: std::ios_base::xalloc
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ios_base/xalloc
---

ddcl|
static int xalloc();
Returns a unique (program-wide) index value that can be used to access one `long` and one `void*` elements in the private storage of `std::ios_base` by calling `iword()` and `pword()`. The call to `xalloc` does not allocate memory.
rrev|since=c++11|
This function is thread-safe: concurrent access by multiple threads does not result in a data race.
Effectively increments the next available unique index.

## Return value

Unique integer for use as pword/iword index.

## Example


## Defect reports


## See also


| cpp/io/ios_base/dsc pword | (see dedicated page) |
| cpp/io/ios_base/dsc iword | (see dedicated page) |


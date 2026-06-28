---
title: std::basic_filebuf::~basic_filebuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/~basic_filebuf
---

ddcl|
virtual ~basic_filebuf();
Calls `close()` to close the associated file and destructs all other members of `basic_filebuf`. If an exception occurs during the destruction of the object, including the call to `close()`, it is caught and not rethrown.

## Notes

Typically called by the destructor of `std::basic_fstream`.

## Example


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-622 | C++98 | it was unclear how to handle the exception thrown during destruction | it is caught but not rethrown |


## See also


| cpp/io/basic_filebuf/dsc basic_filebuf | (see dedicated page) |
| cpp/io/basic_filebuf/dsc close | (see dedicated page) |


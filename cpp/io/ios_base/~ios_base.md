---
title: std::ios_base::~ios_base
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ios_base/~ios_base
---

ddcl |
virtual ~ios_base();
Destroys the `ios_base` object.
Before any of the member functions would yield undefined results, calls callbacks, registered by  passing `cpp/io/ios_base/event | erase_event` as parameter. Then, deallocates any memory obtained.
No operations on `rdbuf` are performed, it is not destroyed.

## Defect reports


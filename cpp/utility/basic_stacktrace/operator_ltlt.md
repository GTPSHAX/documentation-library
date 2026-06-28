---
title: std::operator<<(std::basic_stacktrace)
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/basic_stacktrace/operator_ltlt
---

ddcl | header=stacktrace | since=c++23 |
template< class Allocator >
std::ostream& operator<<( std::ostream& os, const std::basic_stacktrace<Allocator>& st );
Inserts the description of `st` into the output stream `os`. Equivalent to `return os << std::to_string(st);`.

## Parameters


### Parameters


## Return value

`os`.

## Example


## See also


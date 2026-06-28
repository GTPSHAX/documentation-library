---
title: std::basic_stacktrace::operator[]
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/basic_stacktrace/operator_at
---

ddcl|since=c++23|
const_reference operator[]( size_type pos ) const;
Returns a reference to the entry at specified location `pos`. No bounds checking is performed.

## Parameters


### Parameters

- `pos` - position of the stacktrace entry to return

## Return value

Reference to the requested entry.

## Exceptions

Throws nothing.

## Complexity

Constant.

## Example


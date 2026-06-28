---
title: std::system_error::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/error/system_error/operator=
---

ddcl|since=c++11|1=
system_error& operator=( const system_error& other ) noexcept;
Assigns the contents with those of `other`. If `*this` and `other` both have dynamic type `std::system_error` then `1=std::strcmp(what(), other.what()) == 0` after assignment.

## Parameters


### Parameters

- `other` - another `system_error` object to assign with

## Return value

`*this`

## Example


### Example


**Output:**
```
code:    [generic:33]
message: [Numerical argument out of domain]
what:    [Error info #1: Numerical argument out of domain]

code:    [system:5]
message: [Input/output error]
what:    [Error info #2: Input/output error]

code:    [system:5]
message: [Input/output error]
what:    [Error info #2: Input/output error]
```


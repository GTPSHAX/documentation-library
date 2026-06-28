---
title: std::error_code::assign
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_code/assign
---

ddcl|since=c++11|1=
void assign( int val, const error_category& cat ) noexcept;
Replaces the contents with error code value `val` and corresponding category `cat`.

## Parameters


### Parameters

- `val` - platform-dependent error code value to assign
- `cat` - error category corresponding to `val`

## Return value

(none)

## See also


| cpp/error/error_code/dsc operator{{= | (see dedicated page) |


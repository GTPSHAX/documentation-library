---
title: std::make_error_code(std::errc)
type: Utilities
source: https://en.cppreference.com/w/cpp/error/errc/make_error_code
---


# make_error_codesmall|(std::errc)

ddcl|header=system_error|since=c++11|1=
std::error_code make_error_code( std::errc e ) noexcept;
Creates error code value for `errc` enum `e`.
Equivalent to `std::error_code(static_cast<int>(e), std::generic_category())`

## Parameters


### Parameters

- `e` - error code enum to create error code for

## Return value

Error code corresponding to `e`.

## See also


| cpp/io/io_errc/dsc make_error_code | (see dedicated page) |
| cpp/thread/future_errc/dsc make_error_code | (see dedicated page) |


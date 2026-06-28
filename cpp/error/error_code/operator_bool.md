---
title: std::error_code::operator bool
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_code/operator_bool
---

ddcl|since=c++11|1=
explicit operator bool() const noexcept;
Checks if the error code value is valid, i.e. non-zero.

## Parameters

(none)

## Return value

`false` if `1=value() == 0`, `true` otherwise.

## Notes

Although this operator is often used as a convenient shorthand to check if any error was returned, as in }, such use is not robust: some error codes, for example, HTTP status code `200`, may indicate success as well.

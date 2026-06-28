---
title: std::operator<<(std::error_code)
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_code/operator_ltlt
---


# operator<<small|(std::error_code)

ddcl|header=system_error|since=c++11|
template< class CharT, class Traits >
std::basic_ostream<CharT, Traits>&
operator<<( basic_ostream<CharT, Traits>& os, const error_code& ec );
Performs stream output operation on error code `ec`.
Equivalent to `os << ec.category().name() << ':' << ec.value()`.

## Parameters


### Parameters

- `os` - output stream to insert data to
- `ec` - error code

## Return value

`os`

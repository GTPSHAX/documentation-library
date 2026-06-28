---
title: std::is_error_code_enum<std::future_errc>
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/future_errc/is_error_code_enum
---


# is_error_code_enumdsc small|<std::future_errc>


```cpp
dcl | since=c++11 |
template<>
struct is_error_code_enum<std::future_errc> : std::true_type;
```

Specifies that `std::future_errc` is an error code enum. This enables `std::error_code` automatic conversions.

## See also


---
title: std::error_category::equivalent
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_category/equivalent
---


```cpp
dcl | since=c++11 | num=1 | 1=
virtual bool equivalent( int code,
const std::error_condition& condition ) const noexcept;
dcl | since=c++11 | num=2 | 1=
virtual bool equivalent( const std::error_code& code,
int condition ) const noexcept;
```

Checks whether error code is equivalent to an error condition for the error category represented by `*this`.
1. Equivalent to `1=default_error_condition(code) == condition`.
2. Equivalent to `1=*this == code.category() && code.value() == condition`.

## Parameters


### Parameters


## Return value

`true` if the error code is equivalent to the given error condition for the error category represented by `*this`, `false` otherwise.
de:cpp/error/error category/equivalent
es:cpp/error/error category/equivalent
fr:cpp/error/error category/equivalent
it:cpp/error/error category/equivalent
ja:cpp/error/error category/equivalent
pt:cpp/error/error category/equivalent
ru:cpp/error/error category/equivalent
zh:cpp/error/error category/equivalent

---
title: std::regex_error::regex_error
type: Regular expressions
source: https://en.cppreference.com/w/cpp/regex/regex_error/regex_error
---


```cpp
**Header:** `<`regex`>`
dcl|num=1|since=c++11|
regex_error( std::regex_constants::error_type ecode );
dcl|num=2|since=c++11|
regex_error( const regex_error& other );
```

1. Constructs a `regex_error` with a given `ecode` of type `std::regex_constants::error_type`.
2. Copy constructor. Initializes the contents with those of `other`. If `*this` and `other` both have dynamic type `std::regex_error` then `1=std::strcmp(what(), other.what()) == 0`.

## Parameters


### Parameters

- `ecode` - error code indicating the error raised in regular expression parsing
- `other` - another `regex_error` object to copy

## See also


| cpp/regex/dsc error_type | (see dedicated page) |


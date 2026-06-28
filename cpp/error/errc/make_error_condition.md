---
title: std::make_error_condition(std::errc)
type: Utilities
source: https://en.cppreference.com/w/cpp/error/errc/make_error_condition
---


# make_error_conditionsmall|(std::errc)


```cpp
**Header:** `<`system_error`>`
dcl|since=c++11|
std::error_condition make_error_condition( std::errc e ) noexcept;
```

Creates an error condition for an `errc` value `e`. Sets the error value to `int(e)` and error category to `std::generic_category`.

## Parameters


### Parameters

- `e` - standard error value

## Return value

Error condition for `e`.

## Example


### Example


**Output:**
```
Invalid argument
```


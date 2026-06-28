---
title: std::operators (std::error_code)
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_code/operator_cmp
---


# 1=operator==,!=,<,<=>small|(std::error_code)


```cpp
**Header:** `<`system_error`>`
dcl|num=1|since=c++11|1=
bool operator==( const std::error_code& lhs,
const std::error_code& rhs ) noexcept;
dcl|num=2|since=c++11|until=c++20|1=
bool operator!=( const std::error_code& lhs,
const std::error_code& rhs ) noexcept;
dcl|num=3|since=c++11|until=c++20|1=
bool operator<( const std::error_code& lhs,
const std::error_code& rhs ) noexcept;
dcl|num=4|since=c++20|1=
std::strong_ordering operator<=>( const std::error_code& lhs,
const std::error_code& rhs ) noexcept;
```

Compares two error code objects.
1. Compares `lhs` and `rhs` for equality.
2. Compares `lhs` and `rhs` for equality.
3. Checks whether `lhs` is less than `rhs`.
4. Obtains three-way comparison result of `lhs` and `rhs`.
rrev|since=c++20|

## Parameters


### Parameters

- `lhs, rhs` - error codes to compare

## Return value

1. `true` if the error category and error value compare equal.
2. `true` if the error category or error value compare are not equal.
3. `true` if `lhs.category() < rhs.category()`. Otherwise, `true` if `1=lhs.category() == rhs.category() && lhs.value() < rhs.value()`. Otherwise, `false`.
4. `1=lhs.category() <=> rhs.category()` if it is not `std::strong_ordering::equal`. Otherwise, `1=lhs.value() <=> rhs.value()`.

## See also


| cpp/error/error_code/dsc category | (see dedicated page) |
| cpp/error/error_code/dsc value | (see dedicated page) |
| cpp/error/error_condition/dsc operator_cmp | (see dedicated page) |


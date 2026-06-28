---
title: operators (std::error_condition)
type: Utilities
source: https://en.cppreference.com/w/cpp/error/error_condition/operator_cmp
---


# 1=operator==,!=,<,<=>small|(std::error_condition)


```cpp
**Header:** `<`system_error`>`
dcl|num=1|since=c++11|1=
bool operator==( const std::error_condition& lhs,
const std::error_condition& rhs ) noexcept;
dcl|num=2|since=c++11|until=c++20|1=
bool operator!=( const std::error_condition& lhs,
const std::error_condition& rhs ) noexcept;
dcl|num=3|since=c++11|until=c++20|
bool operator<( const std::error_condition& lhs,
const std::error_condition& rhs ) noexcept;
dcl|num=4|since=c++20|1=
std::strong_ordering operator<=>( const std::error_condition& lhs,
const std::error_condition& rhs ) noexcept;
dcl|num=5|since=c++11|1=
bool operator==( const std::error_code& code,
const std::error_condition& cond ) noexcept;
dcl|num=5|since=c++11|until=c++20|1=
bool operator==( const std::error_condition& cond,
const std::error_code& code ) noexcept;
dcl|num=6|since=c++11|until=c++20|1=
bool operator!=( const std::error_code& code,
const std::error_condition& cond ) noexcept;
dcl|num=6|since=c++11|until=c++20|1=
bool operator!=( const std::error_condition& cond,
const std::error_code& code ) noexcept;
```

Compares two error conditions.
1. Checks whether `lhs` and `rhs` are equal.
2. Checks whether `lhs` and `rhs` are not equal.
3. Checks whether `lhs` is ''less than'' `rhs`.
4. Obtains three-way comparison result of `lhs` and `rhs`.
5. Checks whether `code` is a semantic match for `cond`.
6. Checks whether `code` is not a semantic match for `cond`.
rrev|since=c++20|1=

## Parameters


### Parameters

- `lhs, rhs, cond` - error conditions to compare
- `code` - the error code to compare

## Return value

1. `true` if the error category and error value compare equal.
2. `true` if the error category or error value compare are not equal.
3. `true` if `lhs.category() < rhs.category()`. Otherwise, `true` if `1=lhs.category() == rhs.category() && lhs.value() < rhs.value()`. Otherwise, `false`.
4. `1=lhs.category() <=> rhs.category()` if it is not `std::strong_ordering::equal`. Otherwise, `1=lhs.value() <=> rhs.value()`.
5. `true` if either `code.category().equivalent(code.value(), cond)` or `cond.category().equivalent(code, cond.value())`.
6. `true` if neither `code.category().equivalent(code.value(), cond)` nor `cond.category().equivalent(code, cond.value())`.

## See also


| cpp/error/error_category/dsc equivalent | (see dedicated page) |
| cpp/error/error_code/dsc operator_cmp | (see dedicated page) |


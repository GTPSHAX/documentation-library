---
title: std::basic_string_view::operator[]
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/operator_at
---

ddcl|since=c++17|
constexpr const_reference operator[]( size_type pos ) const;
Returns a const reference to the character at specified location `pos`.

## Parameters


### Parameters

- `pos` - position of the character to return

## Return value


## Exceptions

Does not throw.

## Complexity

Constant.

## Notes

Unlike `std::basic_string::operator[]`, `std::basic_string_view::operator[](size())` does not return a reference to `CharT()`.

## Example


### Example


**Output:**
```
e
y
```


## See also


| cpp/string/basic_string_view/dsc at | (see dedicated page) |
| cpp/string/basic_string/dsc {{SUBPAGENAMEE | (see dedicated page) |


---
title: std::basic_string_view::length
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/size
---


```cpp
dcl|since=c++17|
constexpr size_type size() const noexcept;
dcl|since=c++17|
constexpr size_type length() const noexcept;
```

Returns the number of `CharT` elements in the view, i.e. `std::distance(begin(), end())`.

## Parameters

(none)

## Return value

The number of `CharT` elements in the view.

## Complexity

Constant.

## Example


## See also


| cpp/string/basic_string_view/dsc empty  | (see dedicated page) |
| cpp/string/basic_string_view/dsc max_size  | (see dedicated page) |
| cpp/string/basic_string/dsc {{SUBPAGENAMEE | (see dedicated page) |


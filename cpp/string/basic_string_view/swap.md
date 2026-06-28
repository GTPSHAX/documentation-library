---
title: std::basic_string_view::swap
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/swap
---


```cpp
dcl|since=c++17|
constexpr void swap( basic_string_view& v ) noexcept;
```

Exchanges the view with that of `v`.

## Parameters


### Parameters

- `v` - view to swap with

## Return value

(none)

## Complexity

Constant.

## Example


### Example


**Output:**
```
Before swap:
a = AAA
b = BBBB

After swap:
a = BBBB
b = AAA
```


## See also


| cpp/algorithm/dsc swap | (see dedicated page) |
| cpp/algorithm/dsc swap_ranges | (see dedicated page) |
| cpp/string/basic_string/dsc {{SUBPAGENAMEE | (see dedicated page) |


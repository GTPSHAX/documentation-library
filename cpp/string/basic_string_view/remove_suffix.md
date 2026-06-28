---
title: std::basic_string_view::remove_suffix
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/remove_suffix
---

ddcl|since=c++17|
constexpr void remove_suffix( size_type n );
Moves the end of the view back by `n` characters.

## Parameters


### Parameters

- `n` - number of characters to remove from the end of the view

## Complexity

Constant.

## Example


### Example


**Output:**
```
Array: 'abcd', size=7
View : 'abcd', size=4
```


## See also


| cpp/string/basic_string_view/dsc remove_prefix | (see dedicated page) |


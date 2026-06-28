---
title: std::basic_string_view::crbegin
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/rbegin
---


```cpp
dcl|since=c++17|
constexpr const_reverse_iterator rbegin() const noexcept;
dcl|since=c++17|
constexpr const_reverse_iterator crbegin() const noexcept;
```

Returns a reverse iterator to the first character of the reversed view. It corresponds to the last character of the non-reversed view.

## Parameters

(none)

## Return value

`const_reverse_iterator` to the first character.

## Complexity

Constant.

## Example


### Example


**Output:**
```
fed
fed
```


## See also


| cpp/string/basic_string_view/dsc rend | (see dedicated page) |
| cpp/string/basic_string/dsc {{SUBPAGENAMEE | (see dedicated page) |


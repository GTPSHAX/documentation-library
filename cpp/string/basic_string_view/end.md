---
title: std::basic_string_view::cend
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/end
---


```cpp
dcl|since=c++17|
constexpr const_iterator end() const noexcept;
dcl|since=c++17|
constexpr const_iterator cend() const noexcept;
```

Returns an iterator to the character following the last character of the view. This character acts as a placeholder, attempting to access it results in undefined behavior.

## Parameters

(none)

## Return value

`const_iterator` to the character following the last character.

## Complexity

Constant.

## Example


## See also


| cpp/string/basic_string_view/dsc begin | (see dedicated page) |
| cpp/string/basic_string/dsc {{SUBPAGENAMEE | (see dedicated page) |


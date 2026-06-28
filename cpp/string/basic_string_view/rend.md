---
title: std::basic_string_view::rend
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/rend
---


```cpp
dcl|since=c++17|
constexpr const_reverse_iterator rend() const noexcept;
dcl|since=c++17|
constexpr const_reverse_iterator crend() const noexcept;
```

Returns a reverse iterator to the character following the last character of the reversed view. It corresponds to the character preceding the first character of the non-reversed view. This character acts as a placeholder, attempting to access it results in undefined behavior.

## Parameters

(none)

## Return value

`const_reverse_iterator` to the character following the last character.

## Complexity

Constant.

## Example


### Example


**Output:**
```
fedcba
fedcba
```


## See also


| cpp/string/basic_string_view/dsc rbegin | (see dedicated page) |
| cpp/string/basic_string/dsc {{SUBPAGENAMEE | (see dedicated page) |


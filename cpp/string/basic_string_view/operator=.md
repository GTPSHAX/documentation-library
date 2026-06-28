---
title: std::basic_string_view::operator=
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string_view/operator=
---


```cpp
dcl|since=c++17|1=
constexpr basic_string_view& operator=( const basic_string_view& view ) noexcept = default;
```

Replaces the view with that of `view`.

## Parameters


### Parameters

- `view` - view to copy

## Return value

`*this`

## Complexity

Constant.

## Example


### Example


**Output:**
```
world
```


## See also


| cpp/string/basic_string_view/dsc constructor | (see dedicated page) |
| cpp/string/basic_string/dsc operator{{= | (see dedicated page) |


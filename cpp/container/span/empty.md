---
title: std::span::empty
type: Containers
source: https://en.cppreference.com/w/cpp/container/span/empty
---

ddcl|since=c++20|
constexpr bool empty() const noexcept;
Checks if the span is empty. Equivalent to `1=return size() == 0;`.

## Return value

`true` if the span is empty; `false` otherwise.

## Example


### Example


**Output:**
```
"ABCDEF"
"BCDEF"
"CDEF"
"DEF"
"EF"
"F"
""
```


## See also


| cpp/container/span/dsc size | (see dedicated page) |


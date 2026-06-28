---
title: std::span::operator[]
type: Containers
source: https://en.cppreference.com/w/cpp/container/span/operator_at
---

ddcl|since=c++20|
constexpr reference operator[]( size_type idx ) const;
Returns a reference to the `idx` element of the sequence.

## Parameters


### Parameters

- `idx` - the index of the element to access

## Return value

`data()[idx]`

## Exceptions

Throws nothing.

## Example


### Example


**Output:**
```
1 2 3 4 5
5 4 3 2 1
```


## See also


| cpp/container/dsc at|span | (see dedicated page) |
| cpp/container/dsc data|span | (see dedicated page) |
| cpp/container/dsc size|span | (see dedicated page) |
| cpp/container/span/dsc as_bytes | (see dedicated page) |


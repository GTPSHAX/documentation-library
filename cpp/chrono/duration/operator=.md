---
title: std::chrono::duration::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration/operator=
---


```cpp
dcl|since=c++11|1=
duration& operator( const duration &other )  default;
```

Assigns the contents of one `duration` to another.

## Parameters


### Parameters

- `other` - `duration` to copy from

## Example


### Example


**Output:**
```
hours: 2
seconds: 7200
hours: 1
seconds: 7158
hours: 1.98833
```


## See also


| cpp/chrono/duration/dsc constructor | (see dedicated page) |


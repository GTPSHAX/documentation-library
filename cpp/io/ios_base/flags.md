---
title: std::ios_base::flags
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ios_base/flags
---


```cpp
dcl|num=1|
fmtflags flags() const;
dcl|num=2|
fmtflags flags( fmtflags flags );
```

Manages format flags.
1. returns current formatting setting
2. replaces current settings with given ones.

## Parameters


### Parameters

- `flags` - new formatting setting. It can be a combination of formatting flags constants.

#### Formatting flags


## Return value

the formatting flags before the call to the function

## Example


## See also


| cpp/io/ios_base/dsc setf | (see dedicated page) |
| cpp/io/ios_base/dsc unsetf | (see dedicated page) |


---
title: std::pmr::unsynchronized_pool_resource::options
type: Dynamic memory management
source: https://en.cppreference.com/w/cpp/memory/unsynchronized_pool_resource/options
---


```cpp
dcl|since=c++17 | 1=
std::pmr::pool_options options() const;
```

Returns the options that controls the pooling behavior of this resource.
The values in the returned struct may differ from those supplied to the constructor in the following ways:
* Values of zero will be replaced with implementation-specified defaults;
* Sizes may be rounded to an unspecified granularity.

## See also


| cpp/memory/unsynchronized_pool_resource/dsc constructor | (see dedicated page) |


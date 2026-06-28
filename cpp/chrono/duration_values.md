---
title: std::chrono::duration_values
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration_values
---


```cpp
**Header:** `<`chrono`>`
dcl|since=c++11|1=
template< class Rep >
struct duration_values;
```

The `std::chrono::duration_values` type defines three common durations:
* `std::chrono::duration_values::zero`
* `std::chrono::duration_values::min`
* `std::chrono::duration_values::max`
The zero, min, and max static member functions in `std::chrono::duration` forward their work to these functions.
This type can be specialized if the representation `Rep` requires a specific implementation to return these duration objects.

## Member functions


| cpp/chrono/duration_values/dsc zero | (see dedicated page) |
| cpp/chrono/duration_values/dsc min | (see dedicated page) |
| cpp/chrono/duration_values/dsc max | (see dedicated page) |


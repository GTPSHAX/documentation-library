---
title: std::chrono::system_clock::to_time_t
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/system_clock/to_time_t
---


```cpp
dcl|since=c++11|
static std::time_t to_time_t( const time_point& t ) noexcept;
```

Converts `t` to a `std::time_t` type.
If `std::time_t` has lower precision, it is implementation-defined whether the value is rounded or truncated.

## Parameters


### Parameters

- `t` - system clock time point to convert

## Return value

A `std::time_t` value representing `t`.

## Example


### Example

```cpp
#include <chrono>
#include <ctime>
#include <iostream>
#include <thread>
using namespace std::chrono_literals;

int main()
{
    // The old way
    std::time_t oldt = std::time({});

    std::this_thread::sleep_for(2700ms);

    // The new way
    auto const now = std::chrono::system_clock::now();
    std::time_t newt = std::chrono::system_clock::to_time_t(now);

    std::cout << "newt - oldt == " << newt - oldt << " s\n";
}
```


**Output:**
```
newt - oldt == 3 s
```


## See also


| cpp/chrono/system_clock/dsc from_time_t | (see dedicated page) |


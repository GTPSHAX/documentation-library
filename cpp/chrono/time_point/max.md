---
title: std::chrono::time_point::max
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_point/max
---


```cpp
dcl rev multi|until1=c++20|dcl1=
static constexpr time_point max();
|dcl2=
static constexpr time_point max() noexcept;
```

Returns a `time_point` with the largest possible duration, i.e. `time_point(duration::max())`.

## Parameters

(none)

## Return value

The largest possible `time_point`.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
#include <vector>

int main() 
{
    std::chrono::time_point<std::chrono::system_clock> now =
        std::chrono::system_clock::now();
    std::vector<std::chrono::time_point<std::chrono::system_clock>> times
    {
        now - std::chrono::hours(24),
        now - std::chrono::hours(48),
        now + std::chrono::hours(24)
    };  

    std::chrono::time_point<std::chrono::system_clock> earliest =
        std::chrono::time_point<std::chrono::system_clock>::max();

    std::cout << "all times:\n";
    for (const auto& time : times)
    {
        std::time_t t = std::chrono::system_clock::to_time_t(time);
        std::cout << std::ctime(&t);

        if (time < earliest)
            earliest = time;
    }

    std::time_t t = std::chrono::system_clock::to_time_t(earliest);
    std::cout << "earliest:\n" << std::ctime(&t);
}
```


**Output:**
```
all times:
Sun Oct  7 19:06:48 2012
Sat Oct  6 19:06:48 2012
Tue Oct  9 19:06:48 2012
earliest:
Sat Oct  6 19:06:48 2012
```


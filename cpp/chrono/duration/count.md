---
title: std::chrono::duration::count
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration/count
---

ddcl|since=c++11|
constexpr rep count() const;
Returns the number of ticks for this duration.

## Parameters

(none)

## Return value

The number of ticks for this duration.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::chrono::milliseconds ms{3}; // 3 milliseconds
    // 6000 microseconds constructed from 3 milliseconds
    std::chrono::microseconds us = 2 * ms;
    // 30Hz clock using fractional ticks
    std::chrono::duration<double, std::ratio<1, 30>> hz30(3.5);

    std::cout << "3 ms duration has " << ms.count() << " ticks\n"
              << "6000 us duration has " << us.count() << " ticks\n"
              << "3.5 30Hz duration has " << hz30.count() << " ticks\n";       
}
```


**Output:**
```
3 ms duration has 3 ticks
6000 us duration has 6000 ticks
3.5 30Hz duration has 3.5 ticks
```


## See also


| cpp/chrono/duration/dsc duration_cast | (see dedicated page) |


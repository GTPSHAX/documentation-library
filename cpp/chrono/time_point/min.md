---
title: std::chrono::time_point::min
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_point/min
---


```cpp
dcl rev multi|until1=c++20|dcl1=
static constexpr time_point min();
|dcl2=
static constexpr time_point min() noexcept;
```

Returns a `time_point` with the smallest possible duration, i.e. `time_point(duration::min())`.

## Parameters

(none)

## Return value

The smallest possible `time_point`.

## Example


### Example

```cpp
#include <chrono>
#include <iomanip>
#include <iostream>
#include <ratio>
#include <string>

constexpr auto steady_min = std::chrono::steady_clock::time_point::min();

void animate_frame_at_time_offset(double game_time)
{
    std::cout << std::string(static_cast<int>(game_time) % 10 + 1, '*') << '\n';
}

int main()
{
    auto last_frame = steady_min;
    std::chrono::duration<double, std::micro> game_time{0.0};

    for (int n = 0; n < 5; ++n)
    {
        const auto current_frame = std::chrono::steady_clock::now();
        // initialize timer if first frame ever:
        if (last_frame == steady_min)
            last_frame = current_frame;
        game_time += current_frame - last_frame;
        std::cout << "Drawing frame at " << std::setprecision(10)
                  << std::setw(8) << game_time.count() << " μs ";
        animate_frame_at_time_offset(game_time.count());
    }
}
```


**Output:**
```
Drawing frame at        0 μs *
Drawing frame at  134.499 μs *****
Drawing frame at  274.337 μs *****
Drawing frame at  416.571 μs *******
Drawing frame at  561.124 μs **
```


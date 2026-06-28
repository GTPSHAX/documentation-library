---
title: std::chrono::year::year
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/year/year
---


```cpp
dcl|num=1|since=c++20|1=
year() = default;
dcl|num=2|since=c++20|
constexpr explicit year( int y ) noexcept;
```

Constructs a `year` object.
1. Default constructor leaves the year value uninitialized.
2. If `y` is in the range , constructs a `year` object holding the year value `y`. Otherwise the value held is unspecified.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    using namespace std::chrono;

    constexpr int leap_years = []
    {
        int count{};
        for (int i{year::min()}; i <= int{year::max()}; ++i)
            if (year{i}.is_leap()) // uses constructor (2)
                ++count;
        return count;
    } ();

    static_assert(15891 == leap_years);

    std::cout << "There are " << leap_years << " leap years in the range ["
              << int(year::min()) << ", " << int(year::max()) << "].\n";
}
```


**Output:**
```
There are 15891 leap years in the range [-32767, 32767].
```


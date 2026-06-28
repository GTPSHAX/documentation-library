---
title: std::chrono::make24
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/hour_fun
---


```cpp
**Header:** `<`chrono`>`
dcl|num=1|since=c++20|
constexpr bool is_am( const std::chrono::hours& h ) noexcept;
dcl|num=2|since=c++20|
constexpr bool is_pm( const std::chrono::hours& h ) noexcept;
dcl|num=3|since=c++20|
constexpr std::chrono::hours make12( const std::chrono::hours& h ) noexcept;
dcl|num=4|since=c++20|
constexpr std::chrono::hours make24( const std::chrono::hours& h,
bool is_pm ) noexcept;
```

These functions aid in translating between a 12-hour format time of day, and a 24-hour format time of day.
1. Detects whether the 24-hour format time is a.m. (''ante meridiem'', before midday).
2. Detects whether the 24-hour format time is p.m. (''post meridiem'', after midday).
3. Returns the 12-hour equivalent of a 24-hour format time.
4. Returns the 24-hour equivalent of a 12-hour format time `h`, where `is_pm` determines whether the time is p.m.

## Parameters


### Parameters

- `h` - 12-hour or 24-hour format time to detect
- `is_pm` - whether the 12-hour format time is p.m.

## Return value

1. `1=0h <= h && h <= 11h`
2. `1=12h <= h && h <= 23h`
3. If `h` is in range , returns the 12-hour equivalent in range . Otherwise, the return value is unspecified.
4. If `h` is in range , returns the 24-hour equivalent in range  if `is_pm` is `false`, or in range  otherwise. Otherwise, the return value is unspecified.

## Example


### Example

```cpp
#include <chrono>
#include <iomanip>
#include <iostream>
#include <utility>

int main()
{
    using namespace std::chrono;

    static_assert(
        is_am(10h) &&  is_am(11h) && !is_am(12h) && !is_am(23h) &&
       !is_pm(10h) && !is_pm(11h) &&  is_pm(12h) &&  is_pm(23h)
    );

    std::cout << "make12():\n";

    for (const hours hh : {0h, 1h, 11h, 12h, 13h, 23h})
    {
        const hours am{make12(hh)};
        std::cout << std::setw(2) << hh.count() << "h == "
                  << std::setw(2) << am.count() << (is_am(hh) ? "h a.m.\n" : "h p.m.\n");
    }

    std::cout << "\nmake24():\n";

    using p = std::pair<hours, bool>;

    for (const auto& [hh, pm] : {p{1h, 0}, p{12h, 0}, p{1h, 1}, p{12h, 1}<!---->})
    {
        std::cout << std::setw(2) << hh.count()
                  << (pm ? "h p.m." : "h a.m.")
                  << " == " << std::setw(2)
                  << make24(hh, pm).count() << "h\n";
    }
}
```


**Output:**
```
make12():
 0h == 12h a.m.
 1h ==  1h a.m.
11h == 11h a.m.
12h == 12h p.m.
13h ==  1h p.m.
23h == 11h p.m.

make24():
 1h a.m. ==  1h
12h a.m. ==  0h
 1h p.m. == 13h
12h p.m. == 12h
```


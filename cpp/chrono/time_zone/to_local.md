---
title: std::chrono::time_zone::to_local
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/time_zone/to_local
---

ddcl|since=c++20|
template< class Duration >
auto to_local( const std::chrono::sys_time<Duration>& tp ) const
-> std::chrono::local_time<std::common_type_t<Duration, std::chrono::seconds>>;
Converts the `sys_time` `tp` to the corresponding `local_time` in this [List of tz database time zones|time zone](https://en.wikipedia.org/wiki/List of tz database time zones|time zone).

## Parameters


### Parameters

- `tp` - a time point to be converted

## Return value

The `cpp/chrono/local_t|local_time` associated with `tp` and this time zone.

## Notes

The precision of the result is at least `std::chrono::seconds`, and will be finer if the argument has finer precision.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    const auto some_zone_name{"Australia/Sydney"};
    const auto time_pt_utc{std::chrono::system_clock::now()};
    std::cout << "Current time UTC is:\t\t " << time_pt_utc << '\n';

    try
    {
        std::cout << "Current time local is:\t\t "
                  << std::chrono::current_zone()-> // may throw
                      to_local(time_pt_utc) << '\n'
                  << "Current time " << some_zone_name << " is:\t "
                  << std::chrono::locate_zone(some_zone_name)-> // may throw
                      to_local(time_pt_utc) << '\n';
    }
    catch(const std::runtime_error& ex)
    {
        std::cout << ex.what() << '\n';
    }
}
```


**Output:**
```
Current time UTC is:              2025-02-10 13:38:13.233872158
Current time local is:            2025-02-10 16:38:13.233872158
Current time Australia/Sydney is: 2025-02-11 00:38:13.233872158
```


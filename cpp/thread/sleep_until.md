---
title: std::this_thread::sleep_until
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/sleep_until
---

ddcl|header=thread|since=c++11|1=
template< class Clock, class Duration >
void sleep_until( const std::chrono::time_point<Clock, Duration>& sleep_time );
Blocks the execution of the current thread until specified `sleep_time` has been reached.

## Parameters


### Parameters

- `sleep_time` - time to block until

## Return value

(none)

## Exceptions

Any exception thrown by `Clock` or `Duration` (clocks and durations provided by the standard library never throw).

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
#include <thread>

auto now() { return std::chrono::steady_clock::now(); }

auto awake_time()
{
    using std::chrono::operator""ms;
    return now() + 2000ms;
}

int main()
{
    std::cout << "Hello, waiter...\n" << std::flush;
    const auto start{now()};
    std::this_thread::sleep_until(awake_time());
    std::chrono::duration<double, std::milli> elapsed{now() - start};
    std::cout << "Waited " << elapsed.count() << " ms\n";
}
```


**Output:**
```
Hello, waiter...
Waited 2000.17 ms
```


## See also


| cpp/thread/dsc sleep_for | (see dedicated page) |


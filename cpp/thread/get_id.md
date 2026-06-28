---
title: std::this_thread::get_id
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/get_id
---

ddcl|header=thread|since=c++11|1=
std::thread::id get_id() noexcept;
Returns the ''id'' of the current thread.

## Parameters

(none)

## Return value

''id'' of the current thread.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
#include <syncstream>
#include <thread>
using namespace std::chrono_literals;

void foo()
{
    std::thread::id this_id = std::this_thread::get_id();

    std::osyncstream(std::cout) << "thread " << this_id << " sleeping...\n";

    std::this_thread::sleep_for(500ms);
}

int main()
{
    std::jthread t1{foo};
    std::jthread t2{foo};
}
```


**Output:**
```
thread 140113018054400 sleeping...
thread 140113009661696 sleeping...
```


## See also


| cpp/thread/thread/dsc get_id|thread | (see dedicated page) |


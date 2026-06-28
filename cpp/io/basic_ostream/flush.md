---
title: std::basic_ostream::flush
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ostream/flush
---

ddcl|
basic_ostream& flush();
Writes uncommitted changes to the underlying output sequence. Behaves as an *UnformattedOutputFunction*.
If `rdbuf()` is a null pointer, the sentry object is not constructed.
Otherwise, after constructing and checking the sentry object, calls `rdbuf()->pubsync()`. If the call returns `-1`, calls `setstate(badbit)`.

## Return value

`*this`

## Exceptions

May throw `std::ios_base::failure` if `1=(exceptions() & badbit) != 0`.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
#include <thread>

using namespace std::chrono_literals;

void f()
{
    std::cout << "Output from thread... ";
    for (int i{1}; i != 10; ++i)
    {
        std::this_thread::sleep_for(250ms);
        std::cout << i << ' ';

        // output three numbers at once;
        // the effect is observable only in real-time
        if (0 == (i % 3))
            std::cout.flush();
    }
    std::cout << std::endl; // flushes as well
}

int main()
{
    std::thread tr{f};
    std::this_thread::sleep_for(150ms);
    std::clog << "Output from main\n";
    tr.join();
}
```


**Output:**
```
Output from main
Output from thread... 1 2 3 4 5 6 7 8 9
```


## Defect reports


## See also


| cpp/io/basic_streambuf/dsc pubsync | (see dedicated page) |
| cpp/io/basic_streambuf/dsc sync | (see dedicated page) |
| cpp/io/manip/dsc flush | (see dedicated page) |
| cpp/io/manip/dsc endl | (see dedicated page) |
| cpp/io/basic_istream/dsc sync | (see dedicated page) |


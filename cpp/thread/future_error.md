---
title: std::future_error
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/future_error
---


```cpp
**Header:** `<`future`>`
dcl|since=c++11|
class future_error;
```

The class `std::future_error` defines an exception object that is thrown on failure by the functions in the thread library that deal with asynchronous execution and shared states (`std::future`, `std::promise`, etc). Similar to `std::system_error`, this exception carries an error code compatible with `std::error_code`.

## Member functions


| cpp/thread/future_error/dsc constructor | (see dedicated page) |
| cpp/thread/future_error/dsc operator{{= | (see dedicated page) |
| cpp/thread/future_error/dsc code | (see dedicated page) |
| cpp/thread/future_error/dsc what | (see dedicated page) |


## Example


### Example

```cpp
#include <future>
#include <iostream>

int main()
{
    std::future<int> empty;
    try
    {
        int n = empty.get(); // The behavior is undefined, but
                             // some implementations throw std::future_error
    }
    catch (const std::future_error& e)
    {
        std::cout << "Caught a future_error with code \"" << e.code()
                  << "\"\nMessage: \"" << e.what() << "\"\n";
    }
}
```


**Output:**
```
Caught a future_error with code "future:3"
Message: "No associated state"
```


## See also


| cpp/thread/dsc future_errc | (see dedicated page) |


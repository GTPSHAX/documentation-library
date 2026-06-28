---
title: std::shared_future
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_future
---


```cpp
**Header:** `<`future`>`
dcl|num=1|since=c++11|
template< class T > class shared_future;
dcl|num=2|since=c++11|
template< class T > class shared_future<T&>;
dcl|num=3|since=c++11|
template<> class shared_future<void>;
```

The class template `std::shared_future` provides a mechanism to access the result of asynchronous operations, similar to `std::future`, except that multiple threads are allowed to wait for the same shared state. Unlike `std::future`, which is only movable (so only one instance can refer to any particular asynchronous result), `std::shared_future` is copyable and multiple shared future objects may refer to the same shared state.
Access to the same shared state from multiple threads is safe if each thread does it through its own copy of a `shared_future` object.

## Member functions


| cpp/thread/future/dsc constructor|shared_future | (see dedicated page) |

#### Getting the result

| cpp/thread/future/dsc get|shared_future | (see dedicated page) |

#### State

| cpp/thread/future/dsc valid|shared_future | (see dedicated page) |
| cpp/thread/future/dsc wait|shared_future | (see dedicated page) |
| cpp/thread/future/dsc wait_for|shared_future | (see dedicated page) |
| cpp/thread/future/dsc wait_until|shared_future | (see dedicated page) |


## Example


### Example

```cpp
#include <chrono>
#include <future>
#include <iostream>

int main()
{   
    std::promise<void> ready_promise, t1_ready_promise, t2_ready_promise;
    std::shared_future<void> ready_future(ready_promise.get_future());

    std::chrono::time_point<std::chrono::high_resolution_clock> start;

    auto fun1 = [&, ready_future]() -> std::chrono::duration<double, std::milli> 
    {
        t1_ready_promise.set_value();
        ready_future.wait(); // waits for the signal from main()
        return std::chrono::high_resolution_clock::now() - start;
    };


    auto fun2 = [&, ready_future]() -> std::chrono::duration<double, std::milli> 
    {
        t2_ready_promise.set_value();
        ready_future.wait(); // waits for the signal from main()
        return std::chrono::high_resolution_clock::now() - start;
    };

    auto fut1 = t1_ready_promise.get_future();
    auto fut2 = t2_ready_promise.get_future();

    auto result1 = std::async(std::launch::async, fun1);
    auto result2 = std::async(std::launch::async, fun2);

    // wait for the threads to become ready
    fut1.wait();
    fut2.wait();

    // the threads are ready, start the clock
    start = std::chrono::high_resolution_clock::now();

    // signal the threads to go
    ready_promise.set_value();

    std::cout << "Thread 1 received the signal "
              << result1.get().count() << " ms after start\n"
              << "Thread 2 received the signal "
              << result2.get().count() << " ms after start\n";
}
```


**Output:**
```
Thread 1 received the signal 0.072 ms after start
Thread 2 received the signal 0.041 ms after start
```


## See also


| cpp/thread/dsc async | (see dedicated page) |
| cpp/thread/dsc future | (see dedicated page) |


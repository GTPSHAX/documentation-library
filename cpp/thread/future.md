---
title: std::future
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/future
---


```cpp
**Header:** `<`future`>`
dcl|num=1|since=c++11|
template< class T > class future;
dcl|num=2|since=c++11|
template< class T > class future<T&>;
dcl|num=3|since=c++11|
template<> class future<void>;
```

The class template `std::future` provides a mechanism to access the result of asynchronous operations:
* An asynchronous operation (performed via `std::async`, `std::packaged_task`, or `std::promise`) can provide a `std::future` object to the creator of that asynchronous operation.
* The creator of the asynchronous operation can then use a variety of methods to query, wait for, or extract a value from the `std::future`. These methods may block if the asynchronous operation has not yet provided a value.
* When the asynchronous operation is ready to send a result to the creator, it can do so by modifying ''shared state'' (e.g. `std::promise::set_value`) that is linked to the creator's `std::future`.
Note that a `std::future` is a unique reference to the result in a shared state, i.e. the result is not shared with any other asynchronous return objects. Use `std::shared_future` for non-unique access to the result.

## Member functions


| cpp/thread/future/dsc constructor|future | (see dedicated page) |
| cpp/thread/future/dsc destructor | (see dedicated page) |
| cpp/thread/future/dsc operator{{= | (see dedicated page) |
| cpp/thread/future/dsc share | (see dedicated page) |

#### Getting the result

| cpp/thread/future/dsc get|future | (see dedicated page) |

#### State

| cpp/thread/future/dsc valid|future | (see dedicated page) |
| cpp/thread/future/dsc wait|future | (see dedicated page) |
| cpp/thread/future/dsc wait_for|future | (see dedicated page) |
| cpp/thread/future/dsc wait_until|future | (see dedicated page) |


## Examples


### Example

```cpp
#include <future>
#include <iostream>
#include <thread>

int main()
{
    // future from a packaged_task
    std::packaged_task<int()> task([]{ return 7; }); // wrap the function
    std::future<int> f1 = task.get_future(); // get a future
    std::thread t(std::move(task)); // launch on a thread

    // future from an async()
    std::future<int> f2 = std::async(std::launch::async, []{ return 8; });

    // future from a promise
    std::promise<int> p;
    std::future<int> f3 = p.get_future();
    std::thread([&p]{ p.set_value_at_thread_exit(9); }).detach();

    std::cout << "Waiting..." << std::flush;
    f1.wait();
    f2.wait();
    f3.wait();
    std::cout << "Done!\nResults are: "
              << f1.get() << ' ' << f2.get() << ' ' << f3.get() << '\n';
    t.join();
}
```


**Output:**
```
Waiting...Done!
Results are: 7 8 9
```


### Example with exceptions


### Example

```cpp
#include <future>
#include <iostream>
#include <thread>

int main()
{
    std::promise<int> p;
    std::future<int> f = p.get_future();

    std::thread t([&p]
    {
        try
        {
            // code that may throw
            throw std::runtime_error("Example");
        }
        catch (...)
        {
            try
            {
                // store anything thrown in the promise
                p.set_exception(std::current_exception());
            }
            catch (...) {} // set_exception() may throw too
        }
    });

    try
    {
        std::cout << f.get();
    }
    catch (const std::exception& e)
    {
        std::cout << "Exception from the thread: " << e.what() << '\n';
    }
    t.join();
}
```


**Output:**
```
Exception from the thread: Example
```


## See also


| cpp/thread/dsc async | (see dedicated page) |
| cpp/thread/dsc shared_future | (see dedicated page) |


---
title: std::atomic_flag
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_flag
---


```cpp
**Header:** `<`atomic`>`
dcl|since=c++11|1=
struct atomic_flag;
```

`std::atomic_flag` is an atomic boolean type. Unlike all specializations of `std::atomic`, it is guaranteed to be lock-free. Unlike `std::atomic<bool>`, `std::atomic_flag` does not provide load or store operations.

## Member functions


| cpp/atomic/atomic_flag/dsc clear | (see dedicated page) |
| cpp/atomic/atomic_flag/dsc test_and_set | (see dedicated page) |
| cpp/atomic/atomic_flag/dsc test | (see dedicated page) |
| cpp/atomic/atomic/dsc wait|atomic_flag | (see dedicated page) |
| cpp/atomic/atomic/dsc notify_one|atomic_flag | (see dedicated page) |
| cpp/atomic/atomic/dsc notify_all|atomic_flag | (see dedicated page) |


## Example


### Example

```cpp
#include <atomic>
#include <iostream>
#include <mutex>
#include <thread>
#include <vector>

class mutex
{
    std::atomic_flag m_{};

  public:
    void lock() noexcept
    {
        while (m_.test_and_set(std::memory_order_acquire))
#if defined(__cpp_lib_atomic_wait) && __cpp_lib_atomic_wait >= 201907L
            // Since C++20, locks can be acquired only after notification in the unlock,
            // avoiding any unnecessary spinning.
            // Note that even though wait guarantees it returns only after the value has
            // changed, the lock is acquired after the next condition check.
            m_.wait(true, std::memory_order_relaxed)
#endif
                ;
    }
    bool try_lock() noexcept
    {
        return !m_.test_and_set(std::memory_order_acquire);
    }
    void unlock() noexcept
    {
        m_.clear(std::memory_order_release);
#if defined(__cpp_lib_atomic_wait) && __cpp_lib_atomic_wait >= 201907L
        m_.notify_one();
#endif
    }
};

static mutex m;

static int out{};

void f(std::size_t n)
{
    for (std::size_t cnt{}; cnt < 40; ++cnt)
    {
        std::lock_guard lock{m};
        std::cout << n << ((++out % 40) == 0 ? '\n' : ' ');
    }
}

int main()
{
    std::vector<std::thread> v;
    for (std::size_t n{}; n < 10; ++n)
        v.emplace_back(f, n);
    for (auto &t : v)
        t.join();
}
```


**Output:**
```
0 1 1 2 0 1 3 2 3 2 0 1 2 3 2 3 0 1 3 2 0 1 2 3 2 3 0 3 2 3 2 3 2 3 1 2 3 0 1 3
2 3 2 0 1 2 3 0 1 2 3 2 0 1 2 3 0 1 2 3 2 3 2 3 2 0 1 2 3 2 3 0 1 3 2 3 0 2 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 3 2 0 2 3 2 3 2 3 2 3 2 3 0 3
2 3 0 3 0 3 2 3 0 3 2 3 2 3 0 2 3 0 3 2 0 2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
```


## See also


| cpp/atomic/dsc atomic_flag_test_and_set | (see dedicated page) |
| cpp/atomic/dsc atomic_flag_clear | (see dedicated page) |
| cpp/atomic/dsc atomic_flag_wait | (see dedicated page) |
| cpp/atomic/dsc atomic_flag_notify_one | (see dedicated page) |
| cpp/atomic/dsc atomic_flag_notify_all | (see dedicated page) |
| cpp/atomic/dsc ATOMIC_FLAG_INIT | (see dedicated page) |


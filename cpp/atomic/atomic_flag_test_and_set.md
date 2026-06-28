---
title: std::atomic_flag_test_and_set_explicit
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_flag_test_and_set
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++11|
bool atomic_flag_test_and_set( volatile std::atomic_flag* obj ) noexcept;
dcl|num=2|since=c++11|
bool atomic_flag_test_and_set( std::atomic_flag* obj ) noexcept;
dcl|num=3|since=c++11|
bool atomic_flag_test_and_set_explicit( volatile std::atomic_flag* obj,
std::memory_order order ) noexcept;
dcl|num=4|since=c++11|
bool atomic_flag_test_and_set_explicit( std::atomic_flag* obj,
std::memory_order order ) noexcept;
```

Atomically changes the state of a `std::atomic_flag` pointed to by `obj` to set (`true`) and returns the value it held before. This operation is a read-modify-write operation. Memory is affected by the specified memory synchronization order.
@1,2@ The memory synchronization order is `std::memory_order_seq_cst`.
@3,4@ The memory synchronization order is `order`.

## Parameters


### Parameters

- `obj` - pointer to `std::atomic_flag` to access
- `order` - the memory synchronization order

## Return value

The value previously held by the flag pointed to by `obj`.

## Notes

`std::atomic_flag_test_and_set` and `std::atomic_flag_test_and_set_explicit` can be implemented as `obj->test_and_set()` and `obj->test_and_set(order)` respectively.

## Example


### Example

```cpp
#include <atomic>
#include <iostream>
#include <thread>
#include <vector>

std::atomic_flag lock = ATOMIC_FLAG_INIT;

void f(int n)
{
    for (int cnt = 0; cnt < 100; ++cnt)
    {
        while (std::atomic_flag_test_and_set_explicit(&lock, std::memory_order_acquire))
            ; // spin until the lock is acquired
        std::cout << "Output from thread " << n << '\n';
        std::atomic_flag_clear_explicit(&lock, std::memory_order_release);
    }
}

int main()
{
    std::vector<std::thread> v;
    for (int n = 0; n < 10; ++n)
        v.emplace_back(f, n);
    for (auto& t : v)
        t.join();
}
```


**Output:**
```
Output from thread 2
Output from thread 6
Output from thread 7
...<exactly 1000 lines>...
```


## See also


| cpp/atomic/dsc atomic_flag | (see dedicated page) |
| cpp/atomic/dsc atomic_flag_clear | (see dedicated page) |
| cpp/atomic/dsc memory_order | (see dedicated page) |


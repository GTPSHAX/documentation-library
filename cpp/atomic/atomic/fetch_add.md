---
title: std::atomic::fetch_add
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic/fetch_add
---


```cpp
dcl|num=1|since=c++11|1=
T fetch_add( T arg, std::memory_order order =
std::memory_order_seq_cst ) noexcept;
dcl|num=2|since=c++11|1=
T fetch_add( T arg, std::memory_order order =
std::memory_order_seq_cst ) volatile noexcept;
dcl|num=3|since=c++11|1=
T* fetch_add( std::ptrdiff_t arg,
std::memory_order order =
std::memory_order_seq_cst ) noexcept;
dcl|num=4|since=c++11|1=
T* fetch_add( std::ptrdiff_t arg,
std::memory_order order =
std::memory_order_seq_cst ) volatile noexcept;
```

Atomically replaces the current value with the result of arithmetic addition of the value and `arg`. That is, it performs atomic post-increment. The operation is a read-modify-write operation. Memory is affected according to the value of `order`.
@1,2@ For signed integral types, arithmetic is defined to use two’s complement representation. There are no undefined results.
rrev|since=c++20|
For floating-point types, the floating-point environment in effect may be different from the calling thread's floating-point environment. The operation need not conform to the corresponding `std::numeric_limits` traits but is encouraged to do so. If the result is not a representable value for its type, the result is unspecified but the operation otherwise has no undefined behavior.
@3,4@ The result may be an undefined address, but the operation otherwise has no undefined behavior.
@@ If `T` is not a complete object type, the program is ill-formed.
rrev|since=c++20|
It is deprecated if `std::atomic<T>::is_always_lock_free` is `false` and overload  or  participates in overload resolution.

## Parameters


### Parameters

- `arg` - the other argument of arithmetic addition
- `order` - memory order constraints to enforce

## Return value

The value immediately preceding the effects of this function in the  of `*this`.

## Example


### Example

```cpp
#include <array>
#include <atomic>
#include <iostream>
#include <thread>

std::atomic<long long> data{10};
std::array<long long, 5> return_values{};

void do_work(int thread_num)
{
    long long val = data.fetch_add(1, std::memory_order_relaxed);
    return_values[thread_num] = val;
}

int main()
{
    {
        std::jthread th0{do_work, 0};
        std::jthread th1{do_work, 1};
        std::jthread th2{do_work, 2};
        std::jthread th3{do_work, 3};
        std::jthread th4{do_work, 4};
    }

    std::cout << "Result : " << data << '\n';

    for (long long val : return_values)
        std::cout << "Seen return value : " << val << std::endl;
}
```


**Output:**
```
Result : 15
Seen return value : 11
Seen return value : 10
Seen return value : 14
Seen return value : 12
Seen return value : 13
```


## Defect reports


## See also


| cpp/atomic/dsc atomic_fetch_add | (see dedicated page) |
| cpp/atomic/atomic/dsc operator arith | (see dedicated page) |


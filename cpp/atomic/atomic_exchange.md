---
title: std::atomic_exchange_explicit
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_exchange
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++11|
template< class T >
T atomic_exchange( std::atomic<T>* obj,
typename std::atomic<T>::value_type desired ) noexcept;
dcl|num=2|since=c++11|
template< class T >
T atomic_exchange( volatile std::atomic<T>* obj,
typename std::atomic<T>::value_type desired ) noexcept;
dcl|num=3|since=c++11|
template< class T >
T atomic_exchange_explicit( std::atomic<T>* obj,
typename std::atomic<T>::value_type desired,
std::memory_order order ) noexcept;
dcl|num=4|since=c++11|
template< class T >
T atomic_exchange_explicit( volatile std::atomic<T>* obj,
typename std::atomic<T>::value_type desired,
std::memory_order order ) noexcept;
```

@1,2@ Atomically replaces the value pointed to by `obj` with the value of `desired` and returns the value `obj` held previously, as if by `obj->exchange(desired)`.
@3,4@ Atomically replaces the value pointed to by `obj` with the value of `desired` and returns the value `obj` held previously, as if by `obj->exchange(desired, order)`.

## Parameters


### Parameters

- `obj` - pointer to the atomic object to modify
- `desired` - the value to store in the atomic object
- `order` - the memory synchronization ordering

## Return value

The value held previously by the atomic object pointed to by `obj`.

## Example


### Example

```cpp
#include <atomic>
#include <iostream>
#include <thread>
#include <vector>

std::atomic<bool> lock(false); // holds true when locked
                               // holds false when unlocked

int new_line{1}; // the access is synchronized via atomic lock variable

void f(int n)
{
    for (int cnt = 0; cnt < 100; ++cnt)
    {
        while (std::atomic_exchange_explicit(&lock, true, std::memory_order_acquire))
            ; // spin until acquired
        std::cout << n << (new_line++ % 80 ? "" : "\n");
        std::atomic_store_explicit(&lock, false, std::memory_order_release);
    }
}

int main()
{
    std::vector<std::thread> v;
    for (int n = 0; n < 8; ++n)
        v.emplace_back(f, n);
    for (auto& t : v)
        t.join();
}
```


**Output:**
```
02222222222222222222222002222222222222222222222222222222222222222222222222222222
22222222200022222222202222211111111111110000011111111100000000000000110001111111
00011111000001111110000011111100000111000000001111111111111110000010000001001111
11011111111011111011000000000000111100000000000001111000011133333333333333333333
33333333333333333333333333333333333333333333333333333333333333333333333333333333
44444444444444444444444444444444444444444444444444444444444444444444444444444444
44444444444444444444555555555555555555555555555555555555555555555555555555555555
55555555555555555555555555555555555555556666666666666666666666666666666666666666
66666666666666666666666666666666666666666666666666666666666677777777777777777777
77777777777777777777777777777777777777777777777777777777777777777777777777777777
```


## Defect reports


## See also


| cpp/atomic/atomic/dsc exchange|mem=std::atomic<T> | (see dedicated page) |
| cpp/atomic/dsc atomic_compare_exchange | (see dedicated page) |
| cpp/memory/shared_ptr/atomic|notes=mark life|deprecated=c++20|removed=c++26|br=yes|title=std::atomic_exchange(std::shared_ptr) | |
| <br>std::atomic_exchange_explicit(std::shared_ptr)|specializes atomic operations for `std::shared_ptr` | |


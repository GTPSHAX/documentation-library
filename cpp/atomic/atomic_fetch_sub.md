---
title: std::atomic_fetch_sub_explicit
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_fetch_sub
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++11|
template< class T >
T atomic_fetch_sub( std::atomic<T>* obj,
typename std::atomic<T>::difference_type arg ) noexcept;
dcl|num=2|since=c++11|
template< class T >
T atomic_fetch_sub( volatile std::atomic<T>* obj,
typename std::atomic<T>::difference_type arg ) noexcept;
dcl|num=3|since=c++11|
template< class T >
T atomic_fetch_sub_explicit( std::atomic<T>* obj,
typename std::atomic<T>::difference_type arg,
std::memory_order order ) noexcept;
dcl|num=4|since=c++11|
template< class T >
T atomic_fetch_sub_explicit( volatile std::atomic<T>* obj,
typename std::atomic<T>::difference_type arg,
std::memory_order order ) noexcept;
```

Performs atomic subtraction. Atomically subtracts `arg` from the value pointed to by `obj` and returns the value `obj` held previously. The operation is performed as if the following was executed:
@1,2@ `obj->fetch_sub(arg)`
@3,4@ `obj->fetch_sub(arg, order)`
If `std::atomic<T>` has no `fetch_sub` member (this member is only provided for `integral`<sup>(since C++20)</sup> , `floating-point` and `pointer` types except `bool`), the program is ill-formed.

## Parameters


### Parameters

- `obj` - pointer to the atomic object to modify
- `arg` - the value to subtract from the value stored in the atomic object
- `order` - the memory synchronization ordering

## Return value

The value immediately preceding the effects of this function in the  of `*obj`.

## Example


### Example

```cpp
#include <atomic>
#include <iostream>
#include <numeric>
#include <string>
#include <thread>
#include <vector>

const int N = 50;
std::atomic<int> cnt;
std::vector<int> data(N);

void reader(int id) 
{
    for (;;)
    {
        int idx = atomic_fetch_sub_explicit(&cnt, 1, std::memory_order_relaxed);
        if (idx >= 0)
            std::cout << "reader " << std::to_string(id) << " processed item "
                      << std::to_string(data[idx]) << '\n';
        else
        {
            std::cout << "reader " << std::to_string(id) << " done\n";
            break;
        }
    }
}

int main()
{
    std::iota(data.begin(), data.end(), 1);
    cnt = data.size() - 1;

    std::vector<std::thread> v;
    for (int n = 0; n < 5; ++n)
        v.emplace_back(reader, n);
    for (auto& t : v)
        t.join();
}
```


**Output:**
```
reader 2 processed item 50
reader 1 processed item 44
reader 4 processed item 46
<....>
reader 0 done
reader 4 done
reader 3 done
```


## Defect reports


## See also


| cpp/atomic/atomic/dsc fetch_sub|mem=std::atomic<T> | (see dedicated page) |
| cpp/atomic/dsc atomic_fetch_add | (see dedicated page) |


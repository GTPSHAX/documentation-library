---
title: operators (std::thread::id)
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/thread/id/operator_cmp
---


# 1=operator==,!=,<,<=,>,>=,<=>small|(std::thread::id)


```cpp
**Header:** `<`thread`>`
dcl|num=1|since=c++11|1=
bool operator==( std::thread::id lhs, std::thread::id rhs ) noexcept;
dcl|num=2|since=c++11|until=c++20|1=
bool operator!=( std::thread::id lhs, std::thread::id rhs ) noexcept;
dcl|num=3|since=c++11|until=c++20|1=
bool operator< ( std::thread::id lhs, std::thread::id rhs ) noexcept;
dcl|num=4|since=c++11|until=c++20|1=
bool operator<=( std::thread::id lhs, std::thread::id rhs ) noexcept;
dcl|num=5|since=c++11|until=c++20|1=
bool operator> ( std::thread::id lhs, std::thread::id rhs ) noexcept;
dcl|num=6|since=c++11|until=c++20|1=
bool operator>=( std::thread::id lhs, std::thread::id rhs ) noexcept;
dcl|num=7|since=c++20|1=
std::strong_ordering operator<=>( std::thread::id lhs,
std::thread::id rhs ) noexcept;
```

Compares two thread identifiers.
@1,2@ Checks whether `lhs` and `rhs` represent either the same thread, or no thread.
@3-7@ Compares `lhs` and `rhs` in an unspecified total ordering.
rrev|since=c++20|

## Parameters


### Parameters

- `lhs, rhs` - thread identifiers to compare

## Return value

@1-6@ `true` if the corresponding relation holds, `false` otherwise.
7. `std::strong_ordering::less` if `lhs` is less than `rhs` in the total ordering; otherwise `std::strong_ordering::greater` if `rhs` is less than `lhs` in the total ordering; otherwise `std::strong_ordering::equal`.

## Complexity

Constant.

## Example


### Example

```cpp
#include <cassert>
#include <chrono>
#include <iostream>
#include <thread>


int main()
{
    auto work = [] { std::this_thread::sleep_for(std::chrono::seconds(1)); };
    std::thread t1(work);
    std::thread t2(work);

    assert(t1.get_id() == t1.get_id() and
           t2.get_id() == t2.get_id() and
           t1.get_id() != t2.get_id());

    if (const auto cmp = t1.get_id() <=> t2.get_id(); cmp < 0)
        std::cout << "id1 < id2\n";
    else
        std::cout << "id1 > id2\n";

    std::cout << "id1: " << t1.get_id() << "\n"
                 "id2: " << t2.get_id() << '\n';

    t1.join();
    t2.join();
}
```


**Output:**
```
id1 > id2
id1: 139741717640896
id2: 139741709248192
```


## See also


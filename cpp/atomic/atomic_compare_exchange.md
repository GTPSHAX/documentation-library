---
title: std::atomic_compare_exchange_weak_explicit
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_compare_exchange
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++11|
template< class T >
bool atomic_compare_exchange_weak
( std::atomic<T>* obj, typename std::atomic<T>::value_type* expected,
typename std::atomic<T>::value_type desired ) noexcept;
dcl|num=2|since=c++11|
template< class T >
bool atomic_compare_exchange_weak
( volatile std::atomic<T>* obj,
typename std::atomic<T>::value_type* expected,
typename std::atomic<T>::value_type desired ) noexcept;
dcl|num=3|since=c++11|
template< class T >
bool atomic_compare_exchange_strong
( std::atomic<T>* obj, typename std::atomic<T>::value_type* expected,
typename std::atomic<T>::value_type desired ) noexcept;
dcl|num=4|since=c++11|
template< class T >
bool atomic_compare_exchange_strong
( volatile std::atomic<T>* obj,
typename std::atomic<T>::value_type* expected,
typename std::atomic<T>::value_type desired ) noexcept;
dcl|num=5|since=c++11|
template< class T >
bool atomic_compare_exchange_weak_explicit
( std::atomic<T>* obj, typename std::atomic<T>::value_type* expected,
typename std::atomic<T>::value_type desired,
std::memory_order success, std::memory_order failure ) noexcept;
dcl|num=6|since=c++11|
template< class T >
bool atomic_compare_exchange_weak_explicit
( volatile std::atomic<T>* obj,
typename std::atomic<T>::value_type* expected,
typename std::atomic<T>::value_type desired,
std::memory_order success, std::memory_order failure ) noexcept;
dcl|num=7|since=c++11|
template< class T >
bool atomic_compare_exchange_strong_explicit
( std::atomic<T>* obj, typename std::atomic<T>::value_type* expected,
typename std::atomic<T>::value_type desired,
std::memory_order success, std::memory_order failure ) noexcept;
dcl|num=8|since=c++11|
template< class T >
bool atomic_compare_exchange_strong_explicit
( volatile std::atomic<T>* obj,
typename std::atomic<T>::value_type* expected,
typename std::atomic<T>::value_type desired,
std::memory_order success, std::memory_order failure ) noexcept;
```

Atomically compares the <sup>(until C++20)</sup> object representation<sup>(since C++20)</sup> value representation of the object pointed to by `obj` with that of the object pointed to by `expected`, and if those are bitwise-equal, replaces the former with `desired` (performs read-modify-write operation). Otherwise, loads the actual value pointed to by `obj` into `*expected` (performs load operation).


| rowspan=2 | Overloads |
| colspan=2 | Memory model for |
| - |
| read&#8209;modify&#8209;writeoperation |
| load operation |
| - |
| v | 1-4 |
| c | std::memory_order_seq_cst |
| c | std::memory_order_seq_cst |
| - |
| v | 5-8 |
| c | success |
| c | failure |

These functions are defined in terms of member functions of `std::atomic`:
@1,2@ `obj->compare_exchange_weak(*expected, desired)`
@3,4@ `obj->compare_exchange_strong(*expected, desired)`
@5,6@ `obj->compare_exchange_weak(*expected, desired, success, failure)`
@7,8@ `obj->compare_exchange_strong(*expected, desired, success, failure)`
If `failure`<sup>(until C++17)</sup>  is stronger than `success` or is one of `std::memory_order_release` and `std::memory_order_acq_rel`, the behavior is undefined.

## Parameters


### Parameters

- `obj` - pointer to the atomic object to test and modify
- `expected` - pointer to the value expected to be found in the atomic object
- `desired` - the value to store in the atomic object if it is as expected
- `success` - the memory synchronization ordering for the read-modify-write operation if the comparison succeeds
- `failure` - the memory synchronization ordering for the load operation if the comparison fails

## Return value

The result of the comparison: `true` if `*obj` was equal to `*expected`, `false` otherwise.

## Notes

`std::atomic_compare_exchange_weak` and `std::atomic_compare_exchange_weak_explicit` (the weak versions) are allowed to fail spuriously, that is, act as if `1=*obj != *expected` even if they are equal. When a compare-and-exchange is in a loop, they will yield better performance on some platforms.
When a weak compare-and-exchange would require a loop and a strong one would not, the strong one is preferable unless the object representation of `T` may include <sup>(until C++20)</sup> padding bits, trap bits, or offers multiple object representations for the same value (e.g. floating-point NaN). In those cases, weak compare-and-exchange typically works because it quickly converges on some stable object representation.
For a union with bits that participate in the value representations of some members but not the others, compare-and-exchange might always fail because such padding bits have indeterminate values when they do not participate in the value representation of the active member.
rrev|since=c++20|1=
Padding bits that never participate in an object's value representation are ignored.

## Example


### Example

```cpp
#include <atomic>

template<class T>
struct node
{
    T data;
    node* next;
    node(const T& data) : data(data), next(nullptr) {}
};

template<class T>
class stack
{
    std::atomic<node<T>*> head;
public:
    void push(const T& data)
    {
        node<T>* new_node = new node<T>(data);

        // put the current value of head into new_node->next
        new_node->next = head.load(std::memory_order_relaxed);

        // now make new_node the new head, but if the head
        // is no longer what's stored in new_node->next
        // (some other thread must have inserted a node just now)
        // then put that new head into new_node->next and try again
        while (!std::atomic_compare_exchange_weak_explicit(
                   &head, &new_node->next, new_node,
                   std::memory_order_release, std::memory_order_relaxed))
            ; // the body of the loop is empty
// note: the above loop is not thread-safe in at least
// GCC prior to 4.8.3 (bug 60272), clang prior to 2014-05-05 (bug 18899)
// MSVC prior to 2014-03-17 (bug 819819). See member function version for workaround
    }
};

int main()
{
    stack<int> s;
    s.push(1);
    s.push(2);
    s.push(3);
}
```


## Defect reports


## See also


| cpp/atomic/atomic/dsc compare_exchange | (see dedicated page) |
| cpp/atomic/dsc atomic_exchange | (see dedicated page) |
| cpp/memory/shared_ptr/atomic|notes=mark life|deprecated=c++20|removed=c++26|br=yes|title=std::atomic_compare_exchange_weak(std::shared_ptr) | |
| <br>std::atomic_compare_exchange_strong(std::shared_ptr)|specializes atomic operations for std::shared_ptr | |


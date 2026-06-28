---
title: std::atomic::compare_exchange_weak
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic/compare_exchange
---


```cpp
dcl|num=1|since=c++11|
bool compare_exchange_weak( T& expected, T desired,
std::memory_order success,
std::memory_order failure ) noexcept;
dcl|num=2|since=c++11|
bool compare_exchange_weak( T& expected, T desired,
std::memory_order success,
std::memory_order failure ) volatile noexcept;
dcl|num=3|since=c++11|1=
bool compare_exchange_weak( T& expected, T desired,
std::memory_order order =
std::memory_order_seq_cst ) noexcept;
dcl|num=4|since=c++11|1=
bool compare_exchange_weak( T& expected, T desired,
std::memory_order order =
std::memory_order_seq_cst ) volatile noexcept;
dcl|num=5|since=c++11|
bool compare_exchange_strong( T& expected, T desired,
std::memory_order success,
std::memory_order failure ) noexcept;
dcl|num=6|since=c++11|
bool compare_exchange_strong( T& expected, T desired,
std::memory_order success,
std::memory_order failure ) volatile noexcept;
dcl|num=7|since=c++11|1=
bool compare_exchange_strong( T& expected, T desired,
std::memory_order order =
std::memory_order_seq_cst ) noexcept;
dcl|num=8|since=c++11|1=
bool compare_exchange_strong
( T& expected, T desired,
std::memory_order order = std::memory_order_seq_cst ) volatile noexcept;
```

Atomically compares the <sup>(until C++20)</sup> object representation<sup>(since C++20)</sup> value representation of `*this` with that of `expected`. If those are bitwise-equal, replaces the former with `desired` (performs read-modify-write operation). Otherwise, loads the actual value stored in `*this` into `expected` (performs load operation).


| rowspan=2 | Overloads |
| colspan=2 | Memory model for |
| - |
| read&#8209;modify&#8209;writeoperation |
| load operation |
| - |
| v | 1,2,5,6 |
| c | success |
| c | failure |
| - |
| v | 3,4,7,8 |
| c | order |
|  |

If `failure`<sup>(until C++17)</sup>  is stronger than `success` or is one of `std::memory_order_release` and `std::memory_order_acq_rel`, the behavior is undefined.
rrev|since=c++20|
It is deprecated if `std::atomic<T>::is_always_lock_free` is `false` and any `volatile` overload participates in overload resolution.

## Parameters


### Parameters

- `expected` - reference to the value expected to be found in the atomic object
- `desired` - the value to store in the atomic object if it is as expected
- `success` - the memory synchronization ordering for the read-modify-write operation if the comparison succeeds
- `failure` - the memory synchronization ordering for the load operation if the comparison fails
- `order` - the memory synchronization ordering for both operations

## Return value

`true` if the underlying atomic value was successfully changed, `false` otherwise.

## Notes

The comparison and copying are bitwise (similar to `std::memcmp` and `std::memcpy`); no constructor, assignment operator, or comparison operator are used.
`compare_exchange_weak` is allowed to fail spuriously, that is, acts as if `1=*this != expected` even if they are equal. When a compare-and-exchange is in a loop, `compare_exchange_weak` will yield better performance on some platforms.
When `compare_exchange_weak` would require a loop and `compare_exchange_strong` would not, `compare_exchange_strong` is preferable unless the object representation of `T` may include <sup>(until C++20)</sup> padding bits, trap bits, or offers multiple object representations for the same value (e.g. floating-point NaN). In those cases, `compare_exchange_weak` typically works because it quickly converges on some stable object representation.
For a union with bits that participate in the value representations of some members but not the others, compare-and-exchange might always fail because such padding bits have indeterminate values when they do not participate in the value representation of the active member.
rrev|since=c++20|1=
Padding bits that never participate in an object's value representation are ignored.

## Example


### Example

```cpp
#include <atomic>

template<typename T>
struct node
{
    T data;
    node* next;
    node(const T& data) : data(data), next(nullptr) {}
};

template<typename T>
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
        while (!head.compare_exchange_weak(new_node->next, new_node,
                                           std::memory_order_release,
                                           std::memory_order_relaxed))
            ; // the body of the loop is empty

// Note: the above use is not thread-safe in at least 
// GCC prior to 4.8.3 (bug 60272), clang prior to 2014-05-05 (bug 18899)
// MSVC prior to 2014-03-17 (bug 819819). The following is a workaround:
//      node<T>* old_head = head.load(std::memory_order_relaxed);
//      do
//      {
//          new_node->next = old_head;
//      }
//      while (!head.compare_exchange_weak(old_head, new_node,
//                                         std::memory_order_release,
//                                         std::memory_order_relaxed));
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


### Example

```cpp
#include <atomic>
#include <iostream>

std::atomic<int> ai;

int tst_val = 4;
int new_val = 5;
bool exchanged = false;

void valsout()
{
    std::cout << "ai = " << ai
	      << "  tst_val = " << tst_val
	      << "  new_val = " << new_val
	      << "  exchanged = " << std::boolalpha << exchanged
	      << '\n';
}

int main()
{
    ai = 3;
    valsout();

    // tst_val != ai   ==>  tst_val is modified
    exchanged = ai.compare_exchange_strong(tst_val, new_val);
    valsout();

    // tst_val == ai   ==>  ai is modified
    exchanged = ai.compare_exchange_strong(tst_val, new_val);
    valsout();
}
```


**Output:**
```
ai = 3  tst_val = 4  new_val = 5  exchanged = false
ai = 3  tst_val = 3  new_val = 5  exchanged = false
ai = 5  tst_val = 3  new_val = 5  exchanged = true
```


## See also


| cpp/atomic/dsc atomic_compare_exchange | (see dedicated page) |


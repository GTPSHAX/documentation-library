---
title: std::memory_order
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/memory_order
---


```cpp
**Header:** `<`atomic`>`
dcl rev multi
|since1=c++11|dcl1=
enum memory_order
{
memory_order_relaxed,
memory_order_consume,
memory_order_acquire,
memory_order_release,
memory_order_acq_rel,
memory_order_seq_cst
};
|since2=c++20|dcl2=
enum class memory_order : /* unspecified */
{
relaxed, consume, acquire, release, acq_rel, seq_cst
};
inline constexpr memory_order memory_order_relaxed = memory_order::relaxed;
inline constexpr memory_order memory_order_consume = memory_order::consume;
inline constexpr memory_order memory_order_acquire = memory_order::acquire;
inline constexpr memory_order memory_order_release = memory_order::release;
inline constexpr memory_order memory_order_acq_rel = memory_order::acq_rel;
inline constexpr memory_order memory_order_seq_cst = memory_order::seq_cst;
```


## Constants


| Item | Description |
|------|-------------|
| atomic | |
| **Name** | Meaning |


## Formal description

Inter-thread synchronization and memory ordering determine how ''evaluations'' and ''side effects'' of expressions are ordered between different threads of execution. They are defined in the following terms:

### Sequenced-before

Within the same thread, evaluation A may be ''sequenced-before'' evaluation B, as described in evaluation order.
rrev|until=c++26|

### Carries dependency

Within the same thread, evaluation A that is ''sequenced-before'' evaluation B may also carry a dependency into B (that is, B depends on A), if any of the following is true:
1. The value of A is used as an operand of B, '''except'''
:@a@ if B is a call to `std::kill_dependency`,
:@b@ if A is the left operand of the built-in `&&`, `, `?:`, or `,` operators.
2. A writes to a scalar object M, B reads from M.
3. A carries dependency into another evaluation X, and X carries dependency into B.

### Modification order

All modifications to any particular atomic variable occur in a total order that is specific to this one atomic variable.
The following four requirements are guaranteed for all atomic operations:
1. '''Write-write coherence''': If evaluation A that modifies some atomic M (a write) ''happens-before'' evaluation B that modifies M, then A appears earlier than B in the ''modification order'' of M.
2. '''Read-read coherence''': if a value computation A of some atomic M (a read) ''happens-before'' a value computation B on M, and if the value of A comes from a write X on M, then the value of B is either the value stored by X, or the value stored by a side effect Y on M that appears later than X in the ''modification order'' of M.
3. '''Read-write coherence''': if a value computation A of some atomic M (a read) ''happens-before'' an operation B on M (a write), then the value of A comes from a side-effect (a write) X that appears earlier than B in the ''modification order'' of M.
4. '''Write-read coherence''': if a side effect (a write) X on an atomic object M ''happens-before'' a value computation (a read) B of M, then the evaluation B shall take its value from X or from a side effect Y that follows X in the modification order of M.

### Release sequence

After a ''release operation'' A is performed on an atomic object M, the longest continuous subsequence of the modification order of M that consists of:
rrev|until=c++20|
1. Writes performed by the same thread that performed A.
2. Atomic read-modify-write operations made to M by any thread.
Is known as ''release sequence headed by A''.

### Synchronizes with

If an atomic store in thread A is a ''release operation'', an atomic load in thread B from the same variable is an ''acquire operation'', and the load in thread B reads a value written by the store in thread A, then the store in thread A ''synchronizes-with'' the load in thread B.
Also, some library calls may be defined to ''synchronize-with'' other library calls on other threads.
rrev|until=c++26|

### Dependency-ordered before

Between threads, evaluation A is ''dependency-ordered before'' evaluation B if any of the following is true:
1. A performs a ''release operation'' on some atomic M, and, in a different thread, B performs a ''consume operation'' on the same atomic M, and B reads a value written <sup>(until C++20)</sup> by any part of the release sequence headed by A.
2. A is dependency-ordered before X and X carries a dependency into B.

### Inter-thread happens-before

Between threads, evaluation A ''inter-thread happens before'' evaluation B if any of the following is true:
1. A ''synchronizes-with'' B.
2. A is ''dependency-ordered before'' B.
3. A ''synchronizes-with'' some evaluation X, and X is ''sequenced-before'' B.
4. A is ''sequenced-before'' some evaluation X, and X ''inter-thread happens-before'' B.
5. A ''inter-thread happens-before'' some evaluation X, and X ''inter-thread happens-before'' B.
rev|until=c++26|

### Happens-before

Regardless of threads, evaluation A ''happens-before'' evaluation B if any of the following is true:
1. A is ''sequenced-before'' B.
2. A ''inter-thread happens before'' B.
The implementation is required to ensure that the ''happens-before'' relation is acyclic, by introducing additional synchronization if necessary (it can only be necessary if a consume operation is involved, see [https://www.cl.cam.ac.uk/~pes20/cpp/popl085ap-sewell.pdf Batty et al]).
If one evaluation modifies a memory location, and the other reads or modifies the same memory location, and if at least one of the evaluations is not an atomic operation, the behavior of the program is undefined (the program has a data race) unless there exists a ''happens-before'' relationship between these two evaluations.
rrev|since=c++20|

### Simply happens-before

Regardless of threads, evaluation A ''simply happens-before'' evaluation B if any of the following is true:
1. A is ''sequenced-before'' B.
2. A ''synchronizes-with'' B.
3. A ''simply happens-before'' X, and X ''simply happens-before'' B.
Note: without consume operations, ''simply happens-before'' and ''happens-before'' relations are the same.
rev|since=c++26|

### Happens-before

Regardless of threads, evaluation A ''happens-before'' evaluation B if any of the following is true:
1. A is ''sequenced-before'' B.
2. A ''synchronizes-with'' B.
3. A ''happens-before'' X, and X ''happens-before'' B.

### Strongly happens-before

Regardless of threads, evaluation A ''strongly happens-before'' evaluation B if any of the following is true:
rrev multi|until1=c++20
|rev1=
1. A is ''sequenced-before'' B.
2. A ''synchronizes-with'' B.
3. A ''strongly happens-before'' X, and X ''strongly happens-before'' B.
|rev2=
1. A is ''sequenced-before'' B.
2. A ''synchronizes with'' B, and both A and B are sequentially consistent atomic operations.
3. A is ''sequenced-before'' X, X ''<sup>(until C++26)</sup> simply happens-before'' Y, and Y is ''sequenced-before'' B.
4. A ''strongly happens-before'' X, and X ''strongly happens-before'' B.
Note: informally, if A ''strongly happens-before'' B, then A appears to be evaluated before B in all contexts.
rrev|until=c++26|
Note: ''strongly happens-before'' excludes consume operations.

### Visible side-effects

The side-effect A on a scalar M (a write) is ''visible'' with respect to value computation B on M (a read) if both of the following are true:
1. A ''happens-before'' B.
2. There is no other side effect X to M where A ''happens-before'' X and X ''happens-before'' B.
If side-effect A is visible with respect to the value computation B, then the longest contiguous subset of the side-effects to M, in ''modification order'', where B does not ''happen-before'' it is known as the ''visible sequence of side-effects'' (the value of M, determined by B, will be the value stored by one of these side effects).
The standard requires that implementations ensure that atomic store operations are visible to other atomic load operations within a reasonable amount of time (but does not specify a “reasonable time” requirement).
Note: inter-thread synchronization boils down to preventing data races (by establishing happens-before relationships) and defining which side effects become visible under what conditions. Data visibility is strongly related to CPU caching.

### Consume operation

Atomic load with `memory_order_consume` or stronger is a consume operation. Note that `std::atomic_thread_fence` imposes stronger synchronization requirements than a consume operation.

### Acquire operation

Atomic load with `memory_order_acquire` or stronger is an acquire operation. The `lock()` operation on a *Mutex* is also an acquire operation. Note that `std::atomic_thread_fence` imposes stronger synchronization requirements than an acquire operation.

### Release operation

Atomic store with `memory_order_release` or stronger is a release operation. The `unlock()` operation on a *Mutex* is also a release operation. Note that `std::atomic_thread_fence` imposes stronger synchronization requirements than a release operation.

## Explanation


### Relaxed ordering


### Example

```cpp
#include <atomic>
#include <iostream>
#include <thread>
#include <vector>

std::atomic<int> cnt = {0};

void f()
{
    for (int n = 0; n < 1000; ++n)
        cnt.fetch_add(1, std::memory_order_relaxed);
}

int main()
{
    std::vector<std::thread> v;
    for (int n = 0; n < 10; ++n)
        v.emplace_back(f);
    for (auto& t : v)
        t.join();
    std::cout << "Final counter value is " << cnt << '\n';
}
```


**Output:**
```
Final counter value is 10000
```


### Release-Acquire ordering


### Example

```cpp
#include <atomic>
#include <cassert>
#include <string>
#include <thread>

std::atomic<std::string*> ptr;
int data;

void producer()
{
    std::string* p = new std::string("Hello");
    data = 42;
    ptr.store(p, std::memory_order_release);
}

void consumer()
{
    std::string* p2;
    while (!(p2 = ptr.load(std::memory_order_acquire)))
        ;
    assert(*p2 == "Hello"); // never fires
    assert(data == 42); // never fires
}

int main()
{
    std::thread t1(producer);
    std::thread t2(consumer);
    t1.join(); t2.join();
}
```


### Example

```cpp
#include <atomic>
#include <cassert>
#include <thread>
#include <vector>

std::vector<int> data;
std::atomic<int> flag = {0};

void thread_1()
{
    data.push_back(42);
    flag.store(1, std::memory_order_release);
}

void thread_2()
{
    int expected = 1;
    // memory_order_relaxed is okay because this is an RMW,
    // and RMWs (with any ordering) following a release form a release sequence
    while (!flag.compare_exchange_strong(expected, 2, std::memory_order_relaxed))
    {
        expected = 1;
    }
}

void thread_3()
{
    while (flag.load(std::memory_order_acquire) < 2)
        ;
    // if we read the value 2 from the atomic flag, we see 42 in the vector
    assert(data.at(0) == 42); // will never fire
}

int main()
{
    std::thread a(thread_1);
    std::thread b(thread_2);
    std::thread c(thread_3);
    a.join(); b.join(); c.join();
}
```


### Release-Consume ordering

rrev|until=c++26|
rev|since=c++17|until=c++26|
The specification of release-consume ordering is being revised, and the use of `memory_order_consume` is temporarily discouraged.
rev|since=c++26|
Release-consume ordering has the same effect as release-acquire ordering and is deprecated.

### Example

```cpp
#include <atomic>
#include <cassert>
#include <string>
#include <thread>

std::atomic<std::string*> ptr;
int data;

void producer()
{
    std::string* p = new std::string("Hello");
    data = 42;
    ptr.store(p, std::memory_order_release);
}

void consumer()
{
    std::string* p2;
    while (!(p2 = ptr.load(std::memory_order_consume)))
        ;
    assert(*p2 == "Hello"); // never fires: *p2 carries dependency from ptr
    assert(data == 42); // may or may not fire: data does not carry dependency from ptr
}

int main()
{
    std::thread t1(producer);
    std::thread t2(consumer);
    t1.join(); t2.join();
}
```


### Sequentially-consistent ordering


### Example

```cpp
#include <atomic>
#include <cassert>
#include <thread>

std::atomic<bool> x = {false};
std::atomic<bool> y = {false};
std::atomic<int> z = {0};

void write_x()
{
    x.store(true, std::memory_order_seq_cst);
}

void write_y()
{
    y.store(true, std::memory_order_seq_cst);
}

void read_x_then_y()
{
    while (!x.load(std::memory_order_seq_cst))
        ;
    if (y.load(std::memory_order_seq_cst))
        ++z;
}

void read_y_then_x()
{
    while (!y.load(std::memory_order_seq_cst))
        ;
    if (x.load(std::memory_order_seq_cst))
        ++z;
}

int main()
{
    std::thread a(write_x);
    std::thread b(write_y);
    std::thread c(read_x_then_y);
    std::thread d(read_y_then_x);
    a.join(); b.join(); c.join(); d.join();
    assert(z.load() != 0); // will never happen
}
```


## Relationship with


## See also


## External links


---
title: std::packaged_task::packaged_task
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/packaged_task/packaged_task
---


```cpp
dcl|num=1|since=c++11|
packaged_task() noexcept;
dcl|num=2|since=c++11|
template< class F >
explicit packaged_task( F&& f );
dcl|num=3|since=c++11|until=c++17|
template< class F, class Allocator >
explicit packaged_task( std::allocator_arg_t, const Allocator& a, F&& f );
dcl|num=4|since=c++11|1=
packaged_task( const packaged_task& ) = delete;
dcl|num=5|since=c++11|
packaged_task( packaged_task&& rhs ) noexcept;
```

Constructs a new `std::packaged_task` object.
1. Constructs a `std::packaged_task` object with no task and no shared state.
@2,3@ Constructs a `std::packaged_task` object with a stored task of type `std::decay<F>::type` and a shared state. The stored task is initialized with `std::forward<F>(f)`.
rev|until=c++20|
.
Let `t1`, `t2`, ..., `tN` be values of the corresponding types in `Args`, if  is not a valid expression, the program is ill-formed.
rev|since=c++20|
.
If `std::is_invocable_r_v<R, std::decay_t<F>&, Args...>` is `false`, the program is ill-formed.
:@3@ The allocator `a` is used to allocate memory necessary to store the task.
4. The copy constructor is deleted, `std::packaged_task` is move-only.
5. Constructs a `std::packaged_task` with the shared state and task formerly owned by `rhs`, leaving `rhs` with no shared state and a moved-from task.

## Parameters


### Parameters

- `f` - the callable target to execute
- `a` - the allocator to use when storing the task
- `rhs` - the `std::packaged_task` to move from

## Exceptions

2. Any exceptions thrown by copy/move constructor of `f` and possibly `std::bad_alloc` if the allocation fails.
3. Any exceptions thrown by copy/move constructor of `f` and by the allocator's `allocate` function if memory allocation fails.

## Example


### Example

```cpp
#include <future>
#include <iostream>
#include <thread>

int fib(int n)
{
    if (n < 3)
        return 1;
    else
        return fib(n - 1) + fib(n - 2);
}

int main()
{
    std::packaged_task<int(int)> fib_task(&fib); 

    std::cout << "Starting task\n";
    auto result = fib_task.get_future();
    std::thread t(std::move(fib_task), 42);

    std::cout << "Waiting for task to finish..." << std::endl;
    std::cout << result.get() << '\n';

    std::cout << "Task complete\n";
    t.join();
}
```


**Output:**
```
Starting task
Waiting for task to finish...
267914296
Task complete
```


## Defect reports


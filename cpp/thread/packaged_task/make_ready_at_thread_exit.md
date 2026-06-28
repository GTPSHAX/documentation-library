---
title: std::packaged_task::make_ready_at_thread_exit
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/packaged_task/make_ready_at_thread_exit
---

ddcl|since=c++11|
void make_ready_at_thread_exit( Args... args );
Calls the stored task as if by , where `f` is the stored task. The return value of the task or any exception thrown by it is stored in the shared state of `*this`.
The shared state is only made ready after the current thread exits and all objects of thread-local storage duration are destroyed.

## Parameters


### Parameters

- `args` - the parameters to pass on invocation of the stored task

## Return value

(none)

## Exceptions

`std::future_error` on the following error conditions:
* The stored task has already been invoked. The error category is set to `promise_already_satisfied`.
* `*this` has no shared state. The error category is set to `cpp/thread/future_errc|no_state`.

## Example


### Example

```cpp
#include <chrono>
#include <functional>
#include <future>
#include <iostream>
#include <memory>
#include <thread>
#include <utility>

struct ProgramState
{
    std::packaged_task<void()> task;
    std::future<void> future;
    std::thread worker;
};

static void worker(std::shared_ptr<ProgramState> state)
{
    state->task.make_ready_at_thread_exit(); // execute task right away

    auto status = state->future.wait_for(std::chrono::seconds(0));
    if (status == std::future_status::timeout)
        std::cout << "worker: future is not ready yet\n";
    else
        std::cout << "worker: future is ready\n";

    std::cout << "worker: exit\n";
}

static std::shared_ptr<ProgramState> create_state()
{
    auto state = std::make_shared<ProgramState>();
    state->task = std::packaged_task<void()>{[]
    {
        std::cout << "task: executed\n";
    }<!---->};
    state->future = state->task.get_future();
    state->worker = std::thread{worker, state};
    return state;
}

int main()
{
    auto state = create_state();

    state->worker.join();
    std::cout << "main: worker finished\n";

    auto status = state->future.wait_for(std::chrono::seconds(0));
    if (status == std::future_status::timeout)
        std::cout << "main: future is not ready yet\n";
    else
        std::cout << "main: future is ready\n";
}
```


**Output:**
```
task: executed
worker: future is not ready yet
worker: exit
main: worker finished
main: future is ready
```


## See also


| cpp/thread/packaged_task/dsc operator() | (see dedicated page) |


---
title: std::packaged_task::operator=
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/packaged_task/operator=
---


```cpp
dcl|num=1|since=c++11|1=
packaged_task& operator=( const packaged_task& ) = delete;
dcl|num=2|since=c++11|1=
packaged_task& operator=( packaged_task&& rhs ) noexcept;
```

1. Copy assignment operator is deleted, `std::packaged_task` is move-only.
2. Releases the shared state, if any, destroys the previously-held task, and moves the shared state and the task owned by `rhs` into `*this`. `rhs` is left without a shared state and with a moved-from task.

## Parameters


### Parameters

- `rhs` - the `std::packaged_task` to move from

## Example


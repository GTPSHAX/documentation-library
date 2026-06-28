---
title: deduction guides for std::packaged_task
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/packaged_task/deduction_guides
---


# deduction guides for tt|std::packaged_task


```cpp
**Header:** `<`future`>`
dcl|num=1|since=c++17|
template< class R, class... Args >
packaged_task( R(*)(Args...) ) -> packaged_task<R(Args...)>;
dcl|num=2|since=c++17|
template< class F >
packaged_task( F ) -> packaged_task</*see below*/>;
dcl|num=3|since=c++23|
template< class F >
packaged_task( F ) -> packaged_task</*see below*/>;
dcl|num=4|since=c++23|
template< class F >
packaged_task( F ) -> packaged_task</*see below*/>;
```

1. This deduction guide is provided for `std::packaged_task` to allow deduction from functions.
2. . The deduced type is `std::packaged_task<R(A...)>`.
3. . The deduced type is `std::packaged_task<R(A...)>`.
4. . The deduced type is `std::packaged_task<R(A...)>`.

## Notes

These deduction guides do not allow deduction from a function with ellipsis parameter, and the `...` in the types is always treated as a .

## Example


### Example

```cpp
#include <future>

int func(double) { return 0; }

int main()
{
    std::packaged_task f{func}; // deduces packaged_task<int(double)>

    int i = 5;
    std::packaged_task g = [&](double) { return i; }; // => packaged_task<int(double)>
}
```


---
title: std::function::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/function/operator=
---


```cpp
dcl|num=1|since=c++11|1=
function& operator=( const function& other );
dcl|num=2|since=c++11|1=
function& operator=( function&& other );
dcla|num=3|since=c++11|1=
function& operator=( std::nullptr_t ) noexcept;
dcla|num=4|since=c++11|1=
template< class F >
function& operator=( F&& f );
dcl|num=5|since=c++11|1=
template< class F >
function& operator=( std::reference_wrapper<F> f ) noexcept;
```

Assigns a new ''target'' to `std::function`.
1. Assigns a copy of ''target'' of `other`, as if by executing `function(other).swap(*this);`
2. Moves the ''target'' of `other` to `*this`. `other` is in a valid state with an unspecified value.
3. Drops the current ''target''. `*this` is ''empty'' after the call.
4. Sets the ''target'' of `*this` to the callable `f`, as if by executing `function(std::forward<F>(f)).swap(*this);`. This operator does not participate in overload resolution unless `f` is *Callable* for argument types `Args...` and return type `R`.
5. Sets the ''target'' of `*this` to a copy of `f`, as if by executing `function(f).swap(*this);`

## Parameters


### Parameters

- `other` - another `std::function` object to copy the target of
- `f` - a callable to initialize the ''target'' with

**Type requirements:**

- `F`

## Return value

`*this`

## Notes

Even before allocator support was removed from `std::function` in C++17, these assignment operators use the default allocator rather than the allocator of `*this` or the allocator of `other` (see ).

## Example


### Example

```cpp
#include <cassert>
#include <functional>
#include <utility>

int inc(int n) { return n + 1; }

int main()
{
    std::function<int(int)> f1;
    std::function<int(int)> f2(inc);
    assert(f1 == nullptr and f2 != nullptr);

    f1 = f2; // overload (1)
    assert(f1 != nullptr and f1(1) == 2);

    f1 = std::move(f2); // overload (2)
    assert(f1 != nullptr and f1(1) == 2);
    // f2 is in valid but unspecified state

    f1 = nullptr; // overload (3)
    assert(f1 == nullptr);

    f1 = inc; // overload (4)
    assert(f1 != nullptr and f1(1) == 2);

    f1 = [](int n) { return n + n; }; // overload (4)
    assert(f1 != nullptr and f1(2) == 4);

    std::reference_wrapper<int(int)> ref1 = std::ref(inc);
    f1 = ref1; // overload (5)
    assert(f1 != nullptr and f1(1) == 2);
}
```


## Defect reports


## See also


| cpp/utility/functional/move_only_function/dsc operator{{= | (see dedicated page) |
| cpp/utility/functional/function/dsc assign | (see dedicated page) |


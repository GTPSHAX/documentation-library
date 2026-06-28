---
title: std::async
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/async
---


```cpp
**Header:** `<`future`>`
dcl|num=1|since=c++11|
template< class F, class... Args >
std::future</* see below */> async( F&& f, Args&&... args );
dcl|num=2|since=c++11|
template< class F, class... Args >
std::future</* see below */> async( std::launch policy,
F&& f, Args&&... args );
```

The function template `std::async` runs the function `f` asynchronously (potentially in a separate thread which might be a part of a thread pool) and returns a `std::future` that will eventually hold the result of that function call.
1. Behaves as if  is called with `policy` being `std::launch::async .
2. Calls a function `f` with arguments `args` according to a specific launch policy `policy` (see below).
The return type of `std::async` is `std::future<V>`, where `V` is:
rrev multi|until1=c++17
|rev1=
cc multi
|typename std::result_of<typename std::decay<F>::type(
|                        typename std::decay<Args>::type...)>::type.
|rev2=
`std::invoke_result_t<std::decay_t<F>, std::decay_t<Args>...>`.
rrev multi|until1=c++20
|rev1=
If any of the following conditions is satisfied, the program is ill-formed:
* `F` is not *MoveConstructible*.
* Any type in `Args` is not *MoveConstructible*.
*  is not a valid expression.
|rev2=
If any of the following is `false`, the program is ill-formed:
* `std::is_constructible_v<std::decay_t<F>, F>`
* `(std::is_constructible_v<std::decay_t<Args>, Args> && ...)`
* `std::is_invocable_v<std::decay_t<F>, std::decay_t<Args>...>`
The call to `std::async` synchronizes with the call to `f`, and the completion of `f` is sequenced before making the shared state ready.

## Parameters


### Parameters

- `f` - *Callable* object to call
- `args` - parameters to pass to `f`
- `policy` - bitmask value, where individual bits control the allowed methods of execution

## Return value

`std::future` referring to the shared state created by this call to `std::async`.

## Launch policies


### Async invocation

If the ''async'' flag is set, i.e. `1=(policy & std::launch::async) != 0`, then `std::async` calls
rrev multi|until1=c++23
|rev1=
|rev2=
c multi
|std::invoke(auto(std::forward<F>(f)),
|            auto(std::forward<Args>(args))...)
as if in a new thread of execution represented by a `std::thread` object.
rrev multi|until1=c++23
|rev1=The calls of  are evaluated in the current thread.
|rev2=The values produced by `auto` are materialized in the current thread.
If the function `f` returns a value or throws an exception, it is stored in the shared state accessible through the `std::future` that `std::async` returns to the caller.

### Deferred invocation

If the ''deferred'' flag is set (i.e. `1=(policy & std::launch::deferred) != 0`), then `std::async` stores
rrev multi|until1=c++23
|rev1= and  in the shared state.
|rev2=`auto(std::forward<F>(f))` and `auto(std::forward<Args>(args))...` in the shared state.
''Lazy evaluation'' is performed:
* The first call to a non-timed wait function on the `std::future` that `std::async` returned to the caller will evaluate  in the thread that called the waiting function (which does not have to be the thread that originally called `std::async`), where
rrev multi|until1=c++23|rev1=
:* `g` is the stored value of  and
:* `xyz` is the stored copy of .
|rev2=
:* `g` is the stored value of `auto(std::forward<F>(f))` and
:* `xyz` is the stored copy of `auto(std::forward<Args>(args))...`.
* The result or exception is placed in the shared state associated with the returned `std::future` and only then it is made ready. All further accesses to the same `std::future` will return the result immediately.

### Other policies

If neither `std::launch::async` nor `std::launch::deferred`, nor any implementation-defined policy flag is set in `policy`, the behavior is undefined.

## Policy selection

If more than one flag is set, it is implementation-defined which policy is selected. For the default (both the `std::launch::async` and `std::launch::deferred` flags are set in `policy`), standard recommends (but does not require) utilizing available concurrency, and deferring any additional tasks.
If the `std::launch::async` policy is chosen,
* a call to a waiting function on an asynchronous return object that shares the shared state created by this `std::async` call blocks until the associated thread has completed, as if joined, or else time out; and
* the associated thread completion ''synchronizes-with'' the successful return from the first function that is waiting on the shared state, or with the return of the last function that releases the shared state, whichever comes first.

## Exceptions

Throws
* `std::bad_alloc`, if the memory for the internal data structures cannot be allocated, or
* `std::system_error` with error condition `std::errc::resource_unavailable_try_again`, if `1=policy == std::launch::async` and the implementation is unable to start a new thread.
** If `policy` is `std::launch::async  or has additional bits set, it will fall back to deferred invocation or the implementation-defined policies in this case.

## Notes

The implementation may extend the behavior of the first overload of `std::async` by enabling additional (implementation-defined) bits in the default launch policy.
Examples of implementation-defined launch policies are the sync policy (execute immediately, within the `std::async` call) and the task policy (similar to `std::async`, but thread-locals are not cleared)
If the `std::future` obtained from  `std::async` is not moved from or bound to a reference, the destructor of the `std::future` will block at the end of the full expression until the asynchronous operation completes, essentially making code such as the following synchronous:

```cpp
std::async(std::launch::async, []{ f(); }); // temporary's dtor waits for f()
std::async(std::launch::async, []{ g(); }); // does not start until f() completes
```

Note that the destructors of `std::future`s obtained by means other than a call to `std::async` never block.

## Example


### Example

```cpp
#include <algorithm>
#include <future>
#include <iostream>
#include <mutex>
#include <numeric>
#include <string>
#include <vector>

std::mutex m;

struct X
{
    void foo(int i, const std::string& str)
    {
        std::lock_guard<std::mutex> lk(m);
        std::cout << str << ' ' << i << '\n';
    }

    void bar(const std::string& str)
    {
        std::lock_guard<std::mutex> lk(m);
        std::cout << str << '\n';
    }

    int operator()(int i)
    {
        std::lock_guard<std::mutex> lk(m);
        std::cout << i << '\n';
        return i + 10;
    }
};

template<typename RandomIt>
int parallel_sum(RandomIt beg, RandomIt end)
{
    auto len = end - beg;
    if (len < 1000)
        return std::accumulate(beg, end, 0);

    RandomIt mid = beg + len / 2;
    auto handle = std::async(std::launch::async,
                             parallel_sum<RandomIt>, mid, end);
    int sum = parallel_sum(beg, mid);
    return sum + handle.get();
}

int main()
{
    std::vector<int> v(10000, 1);
    std::cout << "The sum is " << parallel_sum(v.begin(), v.end()) << '\n';

    X x;
    // Calls (&x)->foo(42, "Hello") with default policy:
    // may print "Hello 42" concurrently or defer execution
    auto a1 = std::async(&X::foo, &x, 42, "Hello");
    // Calls x.bar("world!") with deferred policy
    // prints "world!" when a2.get() or a2.wait() is called
    auto a2 = std::async(std::launch::deferred, &X::bar, x, "world!");
    // Calls X()(43); with async policy
    // prints "43" concurrently
    auto a3 = std::async(std::launch::async, X(), 43);
    a2.wait();                     // prints "world!"
    std::cout << a3.get() << '\n'; // prints "53"
} // if a1 is not done at this point, destructor of a1 prints "Hello 42" here
```


**Output:**
```
The sum is 10000
43
world!
53
Hello 42
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2021 | C++11 | return type incorrect and value category<br>of arguments unclear in the deferred case | corrected return type and<br>clarified that rvalues are used |
| lwg-2120 | C++11 | the behavior was unclear if no standard<br>or implementation-defined policy is set | the behavior is<br>undefined in this case |
| lwg-2186 | C++11 | it was unclear how the value returned and the<br>exception thrown from the lazy evaluation are handled | they are stored in<br>the shared state |


## See also


| cpp/thread/dsc future | (see dedicated page) |


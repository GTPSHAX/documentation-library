---
title: std::try_to_lock
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/lock_tag
---


```cpp
**Header:** `<`mutex`>`
dcl|num=1|since=c++11|1=
struct defer_lock_t { explicit defer_lock_t() = default; };
|1=
constexpr std::defer_lock_t defer_lock {};
dcl|num=3|since=c++11|1=
struct try_to_lock_t { explicit try_to_lock_t() = default; };
|1=
constexpr std::try_to_lock_t try_to_lock {};
dcl|num=5|since=c++11|1=
struct adopt_lock_t { explicit adopt_lock_t() = default; };
|1=
constexpr std::adopt_lock_t adopt_lock {};
```

@1,3,5@ The empty class tag types `std::defer_lock_t`, `std::try_to_lock_t` and `std::adopt_lock_t` can be used in the constructor's parameter list for `std::unique_lock` and `std::shared_lock` to specify locking strategy.
@2,4,6@ The corresponding `std::defer_lock`, `std::try_to_lock` and `std::adopt_lock` instances of  can be passed to the constructors to indicate the type of locking strategy.
One of the constructors of the class template `std::lock_guard` only accepts the tag `std::adopt_lock`.

## Example


## See also


| cpp/thread/dsc lock_tag_t | (see dedicated page) |
| cpp/thread/lock_guard/dsc constructor | (see dedicated page) |
| cpp/thread/unique_lock/dsc constructor | (see dedicated page) |


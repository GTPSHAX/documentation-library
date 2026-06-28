---
title: std::atomic(std::weak_ptr)
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/weak_ptr/atomic2
---


# atomicpetty|<std::weak_ptr>

ddcl|header=memory|since=c++20|
template< class T >
struct std::atomic<std::weak_ptr<T>>;
The partial template specialization of `std::atomic` for `std::weak_ptr<T>` allows users to manipulate weak_ptr objects atomically. `T` may be an incomplete type.
If multiple threads of execution access the same `std::weak_ptr` object without synchronization and any of those accesses uses a non-const member function of `weak_ptr` then a data race will occur unless all such access is performed through an instance of `std::atomic<std::weak_ptr>`.
Associated `use_count` increments are guaranteed to be part of the atomic operation. Associated `use_count` decrements are sequenced after the atomic operation, but are not required to be part of it, except for the `use_count` change when overriding `expected` in a failed CAS. Any associated deletion and deallocation are sequenced after the atomic update step and are not part of the atomic operation.
Note that the control block used by `std::weak_ptr` and `std::shared_ptr` is thread-safe: different non-atomic `std::weak_ptr` objects can be accessed using mutable operations, such as `1=operator=` or `reset`, simultaneously by multiple threads, even when these instances are copies or otherwise share the same control block internally.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions

All non-specialized `std::atomic` functions are also provided by this specialization, and no additional member functions.
member|atomic|2=

```cpp
dcl|num=1|1=
constexpr atomic() noexcept = default;
dcla|num=2|constexpr=c++26|
atomic( std::weak_ptr<T> desired ) noexcept;
dcl|num=3|1=
atomic( const atomic& ) = delete;
```

1. Initializes the underlying `weak_ptr<T>` to default-constructed value.
2. Initializes the underlying `weak_ptr<T>` to a copy of `desired`. As with any `std::atomic` type, initialization is not an atomic operation.
3. Atomic types are not copy/move constructible.
member|operator|2=

```cpp
dcl|num=1|1=
void operator=( const atomic& ) = delete;
dcla|num=2|constexpr=c++26|1=
void operator=( std::weak_ptr<T> desired ) noexcept;
```

1. Atomic types are not copy/move assignable.
2. Value assignment, equivalent to `store(desired)`.
member|is_lock_free|2=
ddcl|
bool is_lock_free() const noexcept;
Returns `true` if the atomic operations on all objects of this type are lock-free, `false` otherwise.
member|store|2=
ddcla|constexpr=c++26|1=
void store( std::weak_ptr<T> desired,
std::memory_order order = std::memory_order_seq_cst ) noexcept;
Atomically replaces the value of `*this` with the value of `desired` as if by `p.swap(desired)` where `p` is the underlying `std::weak_ptr<T>`. Memory is ordered according to `order`.
.
member|load|2=
ddcla|constexpr=c++26|1=
std::weak_ptr<T> load( std::memory_order order =
std::memory_order_seq_cst ) const noexcept;
Atomically returns a copy of the underlying `std::weak_ptr<T>`. Memory is ordered according to `order`.
.
member|operator std::weak_ptr<T>|2=
ddcla|constexpr=c++26|
operator std::weak_ptr<T>() const noexcept;
Equivalent to `return load();`.
member|exchange|2=
ddcla|constexpr=c++26|1=
std::weak_ptr<T> exchange( std::weak_ptr<T> desired,
std::memory_order order =
std::memory_order_seq_cst ) noexcept;
Atomically replaces the underlying `std::weak_ptr<T>` with `desired` as if by `p.swap(desired)` where `p` is the underlying `std::weak_ptr<T>`, and returns a copy of the value that `p` had immediately before the swap. Memory is ordered according to `order`. This is an atomic read-modify-write operation.
member|compare_exchange_weak, compare_exchange_strong|2=

```cpp
dcla|num=1|constexpr=c++26|
bool compare_exchange_strong
( std::weak_ptr<T>& expected, std::weak_ptr<T> desired,
std::memory_order success, std::memory_order failure ) noexcept;
dcla|num=2|constexpr=c++26|
bool compare_exchange_weak
( std::weak_ptr<T>& expected, std::weak_ptr<T> desired,
std::memory_order success, std::memory_order failure ) noexcept;
dcla|num=3|constexpr=c++26|1=
bool compare_exchange_strong
( std::weak_ptr<T>& expected, std::weak_ptr<T> desired,
std::memory_order order = std::memory_order_seq_cst ) noexcept;
dcla|num=4|constexpr=c++26|1=
bool compare_exchange_weak
( std::weak_ptr<T>& expected, std::weak_ptr<T> desired,
std::memory_order order = std::memory_order_seq_cst ) noexcept;
```

1. If the underlying `std::weak_ptr<T>` stores the same pointer value as `expected` and shares ownership with it, or if both underlying and `expected` are empty, assigns from `desired` to the underlying `std::weak_ptr<T>`, returns `true`, and orders memory according to `success`, otherwise assigns from the underlying `std::weak_ptr<T>` to `expected`, returns `false`, and orders memory according to `failure`.
* On success, the operation is an atomic read-modify-write operation on `*this` and `expected` is not accessed after the atomic update.
* On failure, the operation is an atomic load operation on `*this` and `expected` is updated with the existing value read from the atomic object. This update to `expected`'s use_count is part of this atomic operation, although the write itself (and any subsequent deallocation/destruction) is not required to be.
@@ The behavior is undefined if `failure` is `std::memory_order_release` or `std::memory_order_acq_rel`.
2. Same as , but may also fail spuriously.
3. Equivalent to `return compare_exchange_strong(expected, desired, order, fail_order);`, where `fail_order` is the same as `order` except that `std::memory_order_acq_rel` is replaced by `std::memory_order_acquire` and `std::memory_order_release` is replaced by `std::memory_order_relaxed`.
4. Equivalent to `return compare_exchange_weak(expected, desired, order, fail_order);`, where `fail_order` is the same as `order` except that `std::memory_order_acq_rel` is replaced by `std::memory_order_acquire` and `std::memory_order_release` is replaced by `std::memory_order_relaxed`.
member|wait|2=
ddcla|constexpr=c++26|1=
void wait( std::weak_ptr<T> old
std::memory_order order =
std::memory_order_seq_cst ) const noexcept;
Performs an atomic waiting operation.
Compares `load(order)` with `old` and if they are equivalent then blocks until `*this` is notified by `notify_one()` or `notify_all()`. This is repeated until `load(order)` changes. This function is guaranteed to return only if value has changed, even if underlying implementation unblocks spuriously. Memory is ordered according to `order`.
.
Notes: two `std::weak_ptr`s are equivalent if they store the same pointer and either share ownership or are both empty.
member|notify_one|2=
ddcla|constexpr=c++26|
void notify_one() noexcept;
Performs an atomic notifying operation.
If there is a thread blocked in atomic waiting operations (i.e. `wait()`) on `*this`, then unblocks at least one such thread; otherwise does nothing.
member|notify_all|2=
ddcla|constexpr=c++26|
void notify_all() noexcept;
Performs an atomic notifying operation.
Unblocks all threads blocked in atomic waiting operations (i.e. `wait()`) on `*this` (if any).

## Member constants

The only standard `std::atomic` member constant `is_always_lock_free` is also provided by this specialization.
member|is_always_lock_free|2=
ddcl|1=
static constexpr bool is_always_lock_free = /* implementation-defined */;

## Notes


### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `__cpp_lib_constexpr_memory` | 202506L | C++26 | Constexpr `std::atomic<std::weak_ptr>` |


## Example


## See also


| cpp/atomic/dsc atomic | (see dedicated page) |


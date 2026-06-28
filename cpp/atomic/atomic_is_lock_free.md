---
title: std::atomic_is_lock_free
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_is_lock_free
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++11|
template< class T >
bool atomic_is_lock_free( const volatile std::atomic<T>* obj ) noexcept;
dcl|num=2|since=c++11|
template< class T >
bool atomic_is_lock_free( const std::atomic<T>* obj ) noexcept;
dcl|num=3|since=c++11|
#define ATOMIC_BOOL_LOCK_FREE     /* unspecified */
#define ATOMIC_CHAR_LOCK_FREE     /* unspecified */
#define ATOMIC_CHAR16_T_LOCK_FREE /* unspecified */
#define ATOMIC_CHAR32_T_LOCK_FREE /* unspecified */
#define ATOMIC_WCHAR_T_LOCK_FREE  /* unspecified */
#define ATOMIC_SHORT_LOCK_FREE    /* unspecified */
#define ATOMIC_INT_LOCK_FREE      /* unspecified */
#define ATOMIC_LONG_LOCK_FREE     /* unspecified */
#define ATOMIC_LLONG_LOCK_FREE    /* unspecified */
#define ATOMIC_POINTER_LOCK_FREE  /* unspecified */
dcl|num=4|since=c++20|
#define ATOMIC_CHAR8_T_LOCK_FREE  /* unspecified */
```

@1,2@ Determines if the atomic object pointed to by `obj` is implemented lock-free, as if by calling `obj->is_lock_free()`. In any given program execution, the result of the lock-free query is the same for all atomic objects of the same type.
@3,4@ Expands to an integer constant expression with value
* `0` for the built-in atomic types that are never lock-free,
* `1` for the built-in atomic types that are ''sometimes'' lock-free,
* `2` for the built-in atomic types that are always lock-free.

## Parameters


### Parameters

- `obj` - pointer to the atomic object to examine

## Return value

`true` if `*obj` is a lock-free atomic, `false` otherwise.

## Notes

All atomic types except for `std::atomic_flag` may be implemented using mutexes or other locking operations, rather than using the lock-free atomic CPU instructions. Atomic types are also allowed to be ''sometimes'' lock-free: for example, if only some sub-architectures support lock-free atomic access for a given type (such as the [https://www.felixcloutier.com/x86/cmpxchg8b:cmpxchg16b CMPXCHG16B] instruction on x86-64), whether atomics are lock-free may not be known until runtime.
The C++ standard recommends (but does not require) that lock-free atomic operations are also address-free, that is, suitable for communication between processes using shared memory.

## Example


### Example

```cpp
#include <atomic>
#include <iostream>
#include <utility>

struct A { int a[4]; };
struct B { int x, y; };

int main()
{
    std::atomic<A> a;
    std::atomic<B> b;
    std::cout << std::boolalpha
              << "std::atomic<A> is lock free? "
              << std::atomic_is_lock_free(&a) << '\n'
              << "std::atomic<B> is lock free? "
              << std::atomic_is_lock_free(&b) << '\n';
}
```


**Output:**
```
std::atomic<A> is lock free? false
std::atomic<B> is lock free? true
```


## Defect reports


## See also


| cpp/atomic/atomic/dsc is_lock_free | (see dedicated page) |
| cpp/atomic/dsc atomic_flag | (see dedicated page) |
| cpp/atomic/atomic/dsc is_always_lock_free | (see dedicated page) |
| cpp/memory/shared_ptr/atomic|notes= | |


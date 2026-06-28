---
title: std::atomic
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic
---


```cpp
**Header:** `<`atomic`>`
dcl|num=1|since=c++11|
template< class T >
struct atomic;
dcl|num=2|since=c++11|
template< class U >
struct atomic<U*>;
**Header:** `<`memory`>`
dcla|num=3|since=c++20|
template< class U >
struct atomic<std::shared_ptr<U>>;
dcla|num=4|since=c++20|
template< class U >
struct atomic<std::weak_ptr<U>>;
**Header:** `<`stdatomic.h`>`
dcl|num=5|since=c++23|
#define _Atomic(T) /* see below */
```

Each instantiation and full specialization of the `std::atomic` template defines an atomic type. If one thread writes to an atomic object while another thread reads from it, the behavior is well-defined (see  for details on data races).
In addition, accesses to atomic objects may establish inter-thread synchronization and order non-atomic memory accesses as specified by `std::memory_order`.
Atomic operations are of the following types:
* '''Store''': Writes
* '''Load''': Reads
* '''Read-modify-write (RMW)''': Reads and then writes. Note: This is one atomic operation, not several.
All atomic operations have their , which determines the strictness of the restrictions on instruction reordering and the visibility requirements. Note that the standard requires that read-modify-write operations must each time read the value of the last write in the  preceding the associated write operation (in other words, RMW operations always read the latest value).
`std::atomic` is neither copyable nor movable.
rrev|since=c++23|
The compatibility macro `_Atomic` is provided in  such that `_Atomic(T)` is identical to `std::atomic<T>` while both are well-formed.
It is unspecified whether any declaration in namespace `std` is available when  is included.

## Specializations


### Primary template

The primary `std::atomic` template may be instantiated with any *TriviallyCopyable* type `T` satisfying both *CopyConstructible* and *CopyAssignable*. The program is ill-formed if any of following values is `false`:
* `std::is_trivially_copyable<T>::value`
* `std::is_copy_constructible<T>::value`
* `std::is_move_constructible<T>::value`
* `std::is_copy_assignable<T>::value`
* `std::is_move_assignable<T>::value`
* `std::is_same<T, typename std::remove_cv<T>::type>::value`

```cpp
struct Counters { int a; int b; }; // user-defined trivially-copyable type
std::atomic<Counters> cnt;         // specialization for the user-defined type
```

`std::atomic<bool>` uses the primary template. It is guaranteed to be a standard layout struct and has a .

### Partial specializations

The standard library provides partial specializations of the `std::atomic` template for the following types with additional properties that the primary template does not have:
2. Partial specializations `std::atomic&lt;U*>` for all pointer types. These specializations have standard layout<sup>(until C++20)</sup> , trivial default constructors, and trivial destructors. Besides the operations provided for all atomic types, these specializations additionally support atomic arithmetic operations appropriate to pointer types, such as , .
rrev|since=c++20|
@3,4@ Partial specializations `std::atomic<std::shared_ptr<U>>` and `std::atomic<std::weak_ptr<U>>` are provided for `std::shared_ptr` and `std::weak_ptr`.
See `cpp/memory/shared_ptr/atomic2|std::atomic and `cpp/memory/weak_ptr/atomic2|std::atomic for details.

### Specializations for integral types

When instantiated with one of the following integral types, `std::atomic` provides additional atomic operations appropriate to integral types such as , , , , :
:* The character types `char`<sup>(since C++20)</sup> , `char8_t`, `char16_t`, `char32_t`, and `wchar_t`;
:* The standard signed integer types: `signed char`, `short`, `int`, `long`, and `long long`;
:* The standard unsigned integer types: `unsigned char`, `unsigned short`, `unsigned int`, `unsigned long`, and `unsigned long long`;
:* Any additional integral types needed by the typedefs in the header .
Additionally, the resulting `std::atomic<''Integral''>` specialization has standard layout<sup>(until C++20)</sup> , a trivial default constructor, and a trivial destructor. Signed integer arithmetic is defined to use two's complement; there are no undefined results.
rrev|since=c++20|

### Specializations for floating-point types

When instantiated with one of the cv-unqualified floating-point types (`float`, `double`, `long double`<sup>(since C++23)</sup>  and cv-unqualified extended floating-point types), `std::atomic` provides additional atomic operations appropriate to floating-point types such as  and .
Additionally, the resulting `std::atomic<''Floating''>` specialization has standard layout and a trivial destructor.
No operations result in undefined behavior even if the result is not representable in the floating-point type. The floating-point environment in effect may be different from the calling thread's floating-point environment.

## Member types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| dsc|`difference_type`| | |
| rrev multi | |
| |rev1= | |
| `value_type`  specializations<br> | |
| |rev2= | |
| `std::ptrdiff_t` | |


## Member functions


| cpp/atomic/atomic/dsc constructor | (see dedicated page) |
| cpp/atomic/atomic/dsc operator{{= | (see dedicated page) |
| cpp/atomic/atomic/dsc is_lock_free | (see dedicated page) |
| cpp/atomic/atomic/dsc store | (see dedicated page) |
| cpp/atomic/atomic/dsc load | (see dedicated page) |
| cpp/atomic/atomic/dsc operator_T | (see dedicated page) |
| cpp/atomic/atomic/dsc exchange | (see dedicated page) |
| cpp/atomic/atomic/dsc compare_exchange | (see dedicated page) |
| cpp/atomic/atomic/dsc wait|atomic | (see dedicated page) |
| cpp/atomic/atomic/dsc notify_one|atomic | (see dedicated page) |
| cpp/atomic/atomic/dsc notify_all|atomic | (see dedicated page) |
| cpp/atomic/atomic/dsc is_always_lock_free | (see dedicated page) |


## Specialized member functions


#### Specialized for integral{{rev inl|since=c++20|, floating-point

| cpp/atomic/atomic/dsc fetch_add | (see dedicated page) |
| cpp/atomic/atomic/dsc fetch_sub | (see dedicated page) |
| cpp/atomic/atomic/dsc operator arith2 | (see dedicated page) |

#### Specialized for integral and pointer types only

| cpp/atomic/atomic/dsc fetch_max | (see dedicated page) |
| cpp/atomic/atomic/dsc fetch_min | (see dedicated page) |
| cpp/atomic/atomic/dsc operator arith | (see dedicated page) |

#### Specialized for integral types only

| cpp/atomic/atomic/dsc fetch_and | (see dedicated page) |
| cpp/atomic/atomic/dsc fetch_or | (see dedicated page) |
| cpp/atomic/atomic/dsc fetch_xor | (see dedicated page) |
| cpp/atomic/atomic/dsc operator arith3 | (see dedicated page) |


## Type aliases

Type aliases are provided for `bool` and all integral types listed above, as follows:


#### Aliases for all {{tt|std::atomic<Integral>

| cpp/atomic/atomic/dsc atomic integral types | (see dedicated page) |

#### Aliases for special-purpose types

| cpp/atomic/atomic/dsc atomic lock free aliases | (see dedicated page) |

Note: `std::atomic_int''N''_t`, `std::atomic_uint''N''_t`, `std::atomic_intptr_t`, and `std::atomic_uintptr_t` are defined if and only if `std::int''N''_t`, `std::uint''N''_t`, `std::intptr_t`, and `std::uintptr_t` are defined, respectively. rrev|since=c++20|
`std::atomic_signed_lock_free` and `std::atomic_unsigned_lock_free` are optional in freestanding implementations.

## Notes

There are non-member function template equivalents for all member functions of `std::atomic`. Those non-member functions may be additionally overloaded for types that are not specializations of `std::atomic`, but are able to guarantee atomicity. The only such type in the standard library is `std::shared_ptr<U>`.
`_Atomic` is a keyword and used to provide atomic types in C.
Implementations are recommended to ensure that the representation of `_Atomic(T)` in C is same as that of `std::atomic<T>` in C++ for every possible type `T`. The mechanisms used to ensure atomicity and memory ordering should be compatible.
On GCC and Clang, some of the functionality described here requires linking against `-latomic`.

## Example


### Example

```cpp
#include <atomic>
#include <iostream>
#include <thread>
#include <vector>

std::atomic_int acnt;
int cnt;

void f()
{
    for (auto n{10000}; n; --n)
    {
        ++acnt;
        ++cnt;
        // Note: for this example, relaxed memory order is sufficient,
        // e.g. acnt.fetch_add(1, std::memory_order_relaxed);
    }
}

int main()
{
    {
        std::vector<std::jthread> pool;
        for (int n = 0; n < 10; ++n)
            pool.emplace_back(f);
    }

    std::cout << "The atomic counter is " << acnt << '\n'
              << "The non-atomic counter is " << cnt << '\n';
}
```


**Output:**
```
The atomic counter is 100000
The non-atomic counter is 69696
```


## Defect reports


## See also


| cpp/atomic/dsc atomic_flag | (see dedicated page) |
| cpp/memory/shared_ptr/dsc atomic2 | (see dedicated page) |
| cpp/memory/weak_ptr/dsc atomic2 | (see dedicated page) |


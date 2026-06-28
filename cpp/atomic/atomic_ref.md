---
title: std::atomic_ref
type: Concurrency support
source: https://en.cppreference.com/w/cpp/atomic/atomic_ref
---


```cpp
**Header:** `<`atomic`>`
dcl|since=c++20|
template< class T >
struct atomic_ref;
```

The `std::atomic_ref` class template applies atomic operations to the object it references.
For the lifetime of the `std::atomic_ref` object, the object it references is considered an atomic object. If one thread writes to an atomic object while another thread reads from it, the behavior is well-defined (see  for details on data races). In addition, accesses to atomic objects may establish inter-thread synchronization and order non-atomic memory accesses as specified by `std::memory_order`.
The lifetime of an object must exceed the lifetime of all `std::atomic_ref`s that references the object. While any `std::atomic_ref` instance referencing an object exists, the object must be exclusively accessed through these `std::atomic_ref` instances. No subobject of an object referenced by an `std::atomic_ref` object may be concurrently referenced by any other `std::atomic_ref` object.
Atomic operations applied to an object through an `std::atomic_ref` are atomic with respect to atomic operations applied through any other `std::atomic_ref` referencing the same object.
Like s in the core language, constness is shallow for `std::atomic_ref` - it is possible to modify the referenced value through a `const` `std::atomic_ref` object.
If any of the following conditions are satisfied, the program is ill-formed:
* `std::is_trivially_copyable_v<T>` is `false`.
*  is `false` and `std::is_volatile_v<T>` is `true`.
`std::atomic_ref` is *CopyConstructible*.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |
| dsc|`difference_type`| | |
| * `value_type`, if `T` is an arithmetic type other than ''cv'' `bool`. | |
| * Otherwise, `std::ptrdiff_t`, if `T` is a pointer-to-object type. | |
| * Otherwise, not defined. | |


## Data members


| Item | Description |
|------|-------------|
| **Member** | Description |
| cpp/atomic/atomic_ref/dsc is_always_lock_free | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc required_alignment | (see dedicated page) |


## Member functions


| cpp/atomic/atomic_ref/dsc constructor | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc operator{{= | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc is_lock_free | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc store | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc load | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc operator_T | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc exchange | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc compare_exchange | (see dedicated page) |
| cpp/atomic/atomic/dsc wait|atomic_ref | (see dedicated page) |
| cpp/atomic/atomic/dsc notify_one|atomic_ref | (see dedicated page) |
| cpp/atomic/atomic/dsc notify_all|atomic_ref | (see dedicated page) |
| cpp/atomic/atomic/dsc address|atomic_ref | (see dedicated page) |

#### Provided only when {{tt|T

| cpp/atomic/atomic_ref/dsc fetch_add | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc fetch_sub | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc operator arith2 | (see dedicated page) |

#### Provided only when {{tt|T

| cpp/atomic/atomic_ref/dsc fetch_max | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc fetch_min | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc operator arith | (see dedicated page) |

#### Provided only when {{tt|T

| cpp/atomic/atomic_ref/dsc fetch_and | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc fetch_or | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc fetch_xor | (see dedicated page) |
| cpp/atomic/atomic_ref/dsc operator arith3 | (see dedicated page) |


## Specializations

The standard specifies that `std::atomic_ref` has following specializations:

```cpp
dcl|num=1|since=c++20|
template<>
struct atomic_ref</*integral-type*/>;
dcl|num=2|since=c++20|
template<>
struct atomic_ref</*floating-point-type*/>;
dcl|num=3|since=c++20|
template< class /*pointer-type*/ >
requires /* see below */
struct atomic_ref</*pointer-type*/>;
```

1. `/*integral-type*/` denotes a possibly cv-qualified integral type other than ''cv'' `bool`.
2. `/*floating-point-type*/` denotes a possibly cv-qualified floating-point type.
3. The partial specialization is provided for `/*pointer-type*/` types that are possibly cv-qualified pointer-to-object types.

## Notes

Implementations may merge the specified specializations. E.g. MSVC STL merges all of them into the primary template.
When `T` is ''cv'' `void` or a function type, `std::atomic_ref<T*>` (i.e. `std::atomic_ref<void*>`, `std::atomic_ref<int(*)()>` etc.) does not have `difference_type` or any operation requiring pointer arithmetic<sup>(since C++26)</sup>  or relational comparison.

## Defect reports


## See also


| cpp/atomic/dsc atomic | (see dedicated page) |


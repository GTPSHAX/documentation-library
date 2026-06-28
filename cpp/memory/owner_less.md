---
title: std::owner_less
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/owner_less
---


```cpp
**Header:** `<`memory`>`
dcl rev multi|num=1|since1=c++11|until1=c++17|dcl1=
template< class T >
struct owner_less; /* undefined */
|dcl2=
template< class T = void >
struct owner_less; /* undefined */
dcl|since=c++11|num=2|
template< class T >
struct owner_less<std::shared_ptr<T>>;
dcl|since=c++11|num=3|
template< class T >
struct owner_less<std::weak_ptr<T>>;
dcl|since=c++17|num=4|
template<>
struct owner_less<void>;
```

This function object provides owner-based (as opposed to value-based) mixed-type ordering of both `std::weak_ptr` and `std::shared_ptr`. The order is such that two smart pointers compare equivalent only if they are both empty or if they share ownership, even if the values of the raw pointers obtained by `get()` are different (e.g. because they point at different subobjects within the same object).
1. Owner-based mixed-type ordering is not provided for types other than `std::shared_ptr` and `std::weak_ptr`.
2. The owner-based mixed-type ordering of `std::shared_ptr`.
@@ It is the preferred comparison predicate when building associative containers with `std::shared_ptr` as keys, that is, `std::map<std::shared_ptr<T>, U, std::owner_less<std::shared_ptr<T>>>`.
3. The owner-based mixed-type ordering of `std::weak_ptr`.
@@ It is the preferred comparison predicate when building associative containers with `std::weak_ptr` as keys, that is, `std::map<std::weak_ptr<T>, U, std::owner_less<std::weak_ptr<T>>>`.
4. The `void` specialization deduces the parameter types from the arguments.
The default `operator<` is not defined for weak pointers, and may wrongly consider two shared pointers for the same object non-equivalent (see ).
rrev|since=c++17|

## Specializations

The standard library provides a specialization of `std::owner_less` when `T` is not specified. In this case, the parameter types are deduced from the arguments (each of which must still be either a `std::shared_ptr` or a `std::weak_ptr`).


| cpp/memory/dsc owner_less_void | (see dedicated page) |

rrev|until=c++20|

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions


| cpp/memory/owner_less|title=operator()|inlinemem=true|compares its arguments using owner-based semantics | |

member|operator()|

```cpp
dcla|num=1|since=c++11|constexpr=c++26|
bool operator()( const std::shared_ptr<T>& lhs,
const std::shared_ptr<T>& rhs ) const noexcept;
dcla|num=2|since=c++11|constexpr=c++26|
bool operator()( const std::weak_ptr<T>& lhs,
const std::weak_ptr<T>& rhs ) const noexcept;
dcla|num=3|since=c++11|constexpr=c++26|
bool operator()( const std::shared_ptr<T>& lhs,
const std::weak_ptr<T>& rhs ) const noexcept;
dcla|num=4|since=c++11|constexpr=c++26|
bool operator()( const std::weak_ptr<T>& lhs,
const std::shared_ptr<T>& rhs ) const noexcept;
```

Compares `lhs` and `rhs` using owner-based semantics. Effectively calls `lhs.owner_before(rhs)`.
The ordering is strict weak ordering relation.
`lhs` and `rhs` are equivalent only if they are both empty or share ownership.

## Parameters


### Parameters

- `lhs, rhs` - shared-ownership pointers to compare

## Return value

`true` if `lhs` is ''less than'' `rhs` as determined by the owner-based ordering, `false` otherwise.

## Notes


## Defect reports


## See also


| cpp/memory/shared_ptr/dsc owner_before | (see dedicated page) |
| cpp/memory/weak_ptr/dsc owner_before | (see dedicated page) |


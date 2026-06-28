---
title: std::owner_equal
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/owner_equal
---

ddcl|header=memory|since=c++26|
struct owner_equal;
This function object provides owner-based (as opposed to value-based) mixed-type equal comparison of both `std::weak_ptr` and `std::shared_ptr`. The comparison is such that two smart pointers compare equivalent only if they are both empty or if they share ownership, even if the values of the raw pointers obtained by `get()` are different (e.g. because they point at different subobjects within the same object).
It is the preferred comparison predicate when building unordered associative containers with `std::shared_ptr` and `std::weak_ptr` as keys together with `std::owner_hash`, that is, `std::unordered_map<std::shared_ptr<T>, U, std::owner_hash, std::owner_equal>` or `std::unordered_map<std::weak_ptr<T>, U, std::owner_hash, std::owner_equal>`.

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions


| cpp/memory/owner_equal|title=operator()|inlinemem=true|compares its arguments using owner-based semantics | |

member|operator()|

```cpp
dcl|num=1|since=c++26|
template< class T, class U >
constexpr bool operator()( const std::shared_ptr<T>& lhs,
const std::shared_ptr<U>& rhs ) const noexcept;
dcl|num=2|since=c++26|
template< class T, class U >
constexpr bool operator()( const std::shared_ptr<T>& lhs,
const std::weak_ptr<U>& rhs ) const noexcept;
dcl|num=3|since=c++26|
template< class T, class U >
constexpr bool operator()( const std::weak_ptr<T>& lhs,
const std::shared_ptr<U>& rhs ) const noexcept;
dcl|num=4|since=c++26|
template< class T, class U >
constexpr bool operator()( const std::weak_ptr<T>& lhs,
const std::weak_ptr<U>& rhs ) const noexcept;
```

Compares `lhs` and `rhs` using owner-based semantics. Effectively calls `lhs.owner_equal(rhs)`.
The equal comparison is an equivalence relation.
`lhs` and `rhs` are equivalent only if they are both empty or share ownership.

## Parameters


### Parameters

- `lhs, rhs` - shared-ownership pointers to compare

## Return value

`true` if `lhs` and `rhs` are both empty or share ownership as determined by the owner-based equal comparison, `false` otherwise.

## Notes


## See also


| cpp/memory/shared_ptr/dsc owner_equal | (see dedicated page) |
| cpp/memory/weak_ptr/dsc owner_equal | (see dedicated page) |


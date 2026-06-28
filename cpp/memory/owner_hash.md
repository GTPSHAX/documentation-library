---
title: std::owner_hash
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/owner_hash
---


```cpp
**Header:** `<`memory`>`
dcl|since=c++26|
struct owner_hash;
```

This function object provides owner-based (as opposed to value-based) hashing of both `std::weak_ptr` and `std::shared_ptr`.

## Nested types


| Item | Description |
|------|-------------|
| **Nested type** | Definition |


## Member functions


| cpp/memory/owner_hash|title=operator()|inlinemem=true|calculates the hash of the shared-ownership pointer | |

member|operator()|

```cpp
dcl|since=c++26|num=1|
template< class T >
std::size_t operator()( const std::shared_ptr<T>& key ) const noexcept;
dcl|since=c++26|num=2|
template< class T >
std::size_t operator()( const std::weak_ptr<T>& key ) const noexcept;
```

Equivalent to `return key.owner_hash();`.

## Parameters


### Parameters

- `key` - shared-ownership pointer to be hashed

## Return value

A hash value that is identical for any `std::shared_ptr` or `std::weak_ptr` object sharing the same ownership.

## Notes


## See also


| cpp/memory/shared_ptr/dsc owner_hash | (see dedicated page) |
| cpp/memory/weak_ptr/dsc owner_hash | (see dedicated page) |


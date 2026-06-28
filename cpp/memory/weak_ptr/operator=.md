---
title: std::weak_ptr::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/weak_ptr/operator=
---


```cpp
dcla|num=1|since=c++11|constexpr=c++26|1=
weak_ptr& operator=( const weak_ptr& r ) noexcept;
dcla|num=2|since=c++11|constexpr=c++26|1=
template< class Y >
weak_ptr& operator=( const weak_ptr<Y>& r ) noexcept;
dcla|num=3|since=c++11|constexpr=c++26|1=
template< class Y >
weak_ptr& operator=( const shared_ptr<Y>& r ) noexcept;
dcla|num=4|since=c++11|constexpr=c++26|1=
weak_ptr& operator=( weak_ptr&& r ) noexcept;
dcla|num=5|since=c++11|constexpr=c++26|1=
template< class Y >
weak_ptr& operator=( weak_ptr<Y>&& r ) noexcept;
```

Replaces the managed object with the one managed by `r`. The object is shared with `r`. If `r` manages no object, `*this` manages no object too.
@1-3@ Equivalent to `std::weak_ptr<T>(r).swap(*this)`.
@4,5@ Equivalent to `std::weak_ptr<T>(std::move(r)).swap(*this)`.

## Parameters


### Parameters

- `r` - smart pointer to share an object with

## Return value

`*this`

## Notes

The implementation may meet the requirements without creating a temporary `weak_ptr` object.

## Defect reports


## See also


| cpp/memory/weak_ptr/dsc constructor | (see dedicated page) |
| cpp/memory/weak_ptr/dsc swap | (see dedicated page) |


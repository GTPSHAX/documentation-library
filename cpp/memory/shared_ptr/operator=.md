---
title: std::shared_ptr::operator=
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/shared_ptr/operator=
---


```cpp
dcla|num=1|constexpr=c++26|1=
shared_ptr& operator=( const shared_ptr& r ) noexcept;
dcla|num=2|constexpr=c++26|1=
template< class Y >
shared_ptr& operator=( const shared_ptr<Y>& r ) noexcept;
dcla|num=3|constexpr=c++26|1=
shared_ptr& operator=( shared_ptr&& r ) noexcept;
dcla|num=4|constexpr=c++26|1=
template< class Y >
shared_ptr& operator=( shared_ptr<Y>&& r ) noexcept;
dcl|num=5|deprecated=c++11|until=c++17|1=
template< class Y >
shared_ptr& operator=( std::auto_ptr<Y>&& r );
dcla|num=6|constexpr=c++26|1=
template< class Y, class Deleter >
shared_ptr& operator=( std::unique_ptr<Y, Deleter>&& r );
```

Replaces the managed object with the one managed by `r`.
If `*this` already owns an object and it is the last `shared_ptr` owning it, and `r` is not the same as `*this`, the object is destroyed through the owned deleter.
@1,2@ Shares ownership of the object managed by `r`. If `r` manages no object, `*this` manages no object too.
@@ Equivalent to `shared_ptr<T>(r).swap(*this)`.
@3,4@ Move-assigns a `shared_ptr` from `r`. After the assignment, `*this` contains a copy of the previous state of `r`, and `r` is empty.
@@ Equivalent to `shared_ptr<T>(std::move(r)).swap(*this)`.
5. Transfers the ownership of the object managed by `r` to `*this`. If `r` manages no object, `*this` manages no object too. After the assignment, `*this` contains the pointer previously held by `r`, and `1=use_count() == 1`; also `r` is empty.
@@ Equivalent to `shared_ptr<T>(r).swap(*this)`.
6. Transfers the ownership of the object managed by `r` to `*this`. The deleter associated to `r` is stored for future deletion of the managed object. `r` manages no object after the call.
@@ Equivalent to `shared_ptr<T>(std::move(r)).swap(*this)`.

## Parameters


### Parameters

- `r` - another smart pointer to share the ownership to or acquire the ownership from

## Return value

`*this`

## Notes

The implementation may meet the requirements without creating a temporary `shared_ptr` object.

## Exceptions

@5,6@

## Example


## See also


| cpp/memory/shared_ptr/dsc reset | (see dedicated page) |


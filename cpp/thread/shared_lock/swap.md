---
title: std::shared_lock::swap
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/shared_lock/swap
---

ddcl|since=c++14|
template< class Mutex >
void swap( shared_lock<Mutex>& other ) noexcept;
Exchanges the internal states of the lock objects.

## Parameters


### Parameters

- `other` - the lock to swap the state with

## Return value

(none)

## Example


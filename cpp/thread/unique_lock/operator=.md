---
title: std::unique_lock::operator=
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/unique_lock/operator=
---

ddcl|since=c++11|1=
unique_lock& operator=( unique_lock&& other ) noexcept;
Move assignment operator. Equivalent to }.
If `other` is the same object as `*this`, there is no effect. Otherwise, if prior to the call `*this` has an associated mutex and has acquired ownership of it, the mutex is unlocked.

## Parameters


### Parameters

- `other` - another `unique_lock` to replace the state with

## Return value

`*this`

## Notes

With a recursive mutex it is possible for both `*this` and `other` to own the same mutex before the assignment. In this case, `*this` will own the mutex after the assignment and `other` will not.
The move assignment possibly raises undefined behavior. For example, when `*this` is constructed with `std::adopt_lock`, but the calling thread does not have the ownership of the associated mutex, the ownership of the associated mutex cannot be properly released.

## Defect reports


---
title: std::future_error::operator=
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/future_error/operator=
---

ddcl|since=c++11|1=
future_error& operator=( const future_error& other ) noexcept;
Assigns the contents with those of `other`. If `*this` and `other` both have dynamic type `std::future_error` then `1=std::strcmp(what(), other.what()) == 0` after assignment.

## Parameters


### Parameters

- `other` - another `future_error` object to assign with

## Return value

`*this`

## Example


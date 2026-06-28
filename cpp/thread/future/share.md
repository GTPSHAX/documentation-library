---
title: std::future::share
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/future/share
---

ddcl|note=<sup>(C++11)</sup>|
std::shared_future<T> share() noexcept;
Transfers the shared state of `*this`, if any, to a `std::shared_future` object. Multiple `std::shared_future` objects may reference the same shared state, which is not possible with `std::future`.
After calling `share` on a `std::future`, `valid()` ` .

## Parameters

(none)

## Return value

A `std::shared_future` object containing the shared state previously held by `*this`, if any, constructed as if by `std::shared_future<T>(std::move(*this))`.

## Example


## See also


| cpp/thread/dsc shared_future | (see dedicated page) |


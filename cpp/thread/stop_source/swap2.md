---
title: swap(std::stop_source)
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_source/swap2
---


# swapsmall|(std::stop_source)

ddcl|since=c++20|
friend void swap( stop_source& lhs, stop_source& rhs ) noexcept;
Overloads the `std::swap` algorithm for `std::stop_source`. Exchanges the stop-state of `lhs` with that of `rhs`. Effectively calls `lhs.swap(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - `stop_source`s to swap

## Return value

(none)

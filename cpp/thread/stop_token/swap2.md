---
title: swap(std::stop_token)
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_token/swap2
---


# swapsmall|(std::stop_token)

ddcl|since=c++20|
friend void swap( stop_token& lhs, stop_token& rhs ) noexcept;
Overloads the `std::swap` algorithm for `std::stop_token`. Exchanges the associated stop-state of `lhs` with that of `rhs`. Effectively calls `lhs.swap(rhs)`.

## Parameters


### Parameters

- `lhs, rhs` - `stop_token`s to swap

## Return value

(none)

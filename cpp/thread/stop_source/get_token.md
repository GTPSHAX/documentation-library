---
title: std::stop_source::get_token
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_source/get_token
---

ddcl|since=c++20|
std::stop_token get_token() const noexcept;
Returns a `stop_token` object associated with the `stop_source`'s stop-state, if the `stop_source` has stop-state; otherwise returns a default-constructed (empty) `stop_token`.

## Parameters

(none)

## Return value

A `stop_token` object, which will be empty if `1=this->stop_possible() == false`.

## Example


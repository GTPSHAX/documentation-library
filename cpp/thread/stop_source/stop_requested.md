---
title: std::stop_source::stop_requested
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_source/stop_requested
---

ddcl|since=c++20|
bool stop_requested() const noexcept;
Checks if the `stop_source` object has a stop-state and that state has received a stop request.

## Parameters

(none)

## Return value

`true` if the `stop_token` object has a stop-state and it has received a stop request, `false` otherwise.

## Example


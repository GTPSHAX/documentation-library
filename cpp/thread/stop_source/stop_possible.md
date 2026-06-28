---
title: std::stop_source::stop_possible
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/stop_source/stop_possible
---

ddcl|since=c++20|
bool stop_possible() const noexcept;
Checks if the `stop_source` object has a stop-state.

## Parameters

(none)

## Return value

`true` if the `stop_source` object has a stop-state, otherwise `false`.

## Notes

If the `stop_source` object has a stop-state and a stop request has already been made, this function still returns `true`.

## Example


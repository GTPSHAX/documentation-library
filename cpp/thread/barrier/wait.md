---
title: std::barrier::wait
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/barrier/wait
---

ddcl|since=c++20|
void wait( arrival_token&& arrival ) const;
If `arrival` is associated with the phase synchronization point for the current phase of `*this`, blocks at the synchronization point associated with `arrival` until the phase completion step of the synchronization point's phase is run.
Otherwise, if `arrival` is associated with the phase synchronization point for the immediately preceding phase of `*this`, returns immediately.
Otherwise, i.e. if `arrival` is associated with the phase synchronization point for an earlier phase of `*this` or any phase of a barrier object other than `*this`, the behavior is undefined.

## Parameters


### Parameters

- `arrival` - an `arrival_token` obtained by a previous call to `arrive` on the same `barrier`

## Return value

(none)

## Exceptions

Throws `std::system_error` with an error code allowed for mutex types on error.

## Example


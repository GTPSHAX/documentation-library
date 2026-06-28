---
title: std::once_flag
type: Concurrency support
source: https://en.cppreference.com/w/cpp/thread/once_flag
---

ddcl | header=mutex | since=c++11 |
class once_flag;
The class `std::once_flag` is a helper structure for `std::call_once`.
An object of type `std::once_flag` that is passed to multiple calls to `std::call_once` allows those calls to coordinate with each other such that only one of the calls will actually run to completion.
`std::once_flag` is neither copyable nor movable.

## Member functions

member | once_flag |
ddcl |
constexpr once_flag() noexcept;
Constructs an `once_flag` object. The internal state is set to indicate that no function has been called yet.

## Parameters

(none)

## See also


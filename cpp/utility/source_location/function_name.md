---
title: std::source_location::function_name
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/source_location/function_name
---

ddcl | since=c++20 |
constexpr const char* function_name() const noexcept;
Returns the name of the function associated with the position represented by this object, if any.

## Parameters

(none)

## Return value

If this object represents a position in a body of a function, returns an implementation-defined null-terminated byte string corresponding to the name of the function.
Otherwise, an empty string is returned.

## Example


## See also


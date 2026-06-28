---
title: std::basic_stacktrace::rend
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/basic_stacktrace/rend
---


```cpp
dcl | num=1 | since=c++23 |
const_reverse_iterator rend()  const noexcept;
dcl | num=2 | since=c++23 |
const_reverse_iterator crend() const noexcept;
```

Returns a reverse iterator pointing past the last entry of the reversed `basic_stacktrace`. It corresponds to the iterator preceding the first entry of the original `basic_stacktrace`. This iterator acts as a placeholder, attempting to dereference it results in undefined behavior.

## Parameters

(none)

## Return value

The end iterator of the reversed `basic_stacktrace`.

## Complexity

Constant.

## Example


## See also


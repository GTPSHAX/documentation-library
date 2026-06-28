---
title: std::basic_stacktrace::end
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/basic_stacktrace/end
---


```cpp
dcl | num=1 | since=c++23 |
const_iterator end()  const noexcept;
dcl | num=2 | since=c++23 |
const_iterator cend() const noexcept;
```

Returns the iterator pointing past the last entry of the `basic_stacktrace`.
This iterator acts as a placeholder; attempting to dereference it results in undefined behavior.

## Parameters

(none)

## Return value

The end iterator.

## Complexity

Constant.

## Example


## See also


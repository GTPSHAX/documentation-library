---
title: std::basic_stacktrace::cbegin
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/basic_stacktrace/begin
---


```cpp
dcl | num=1 | since=c++23 |
const_iterator begin()  const noexcept;
dcl | num=2 | since=c++23 |
const_iterator cbegin() const noexcept;
```

Returns an iterator to the first entry of the `basic_stacktrace`.
If the `basic_stacktrace` is empty, the returned iterator is equal to `end()`.

## Parameters

(none)

## Return value

Iterator to the first entry.

## Complexity

Constant.

## Example


## See also


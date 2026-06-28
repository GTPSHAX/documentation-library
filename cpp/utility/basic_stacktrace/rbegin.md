---
title: std::basic_stacktrace::rbegin
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/basic_stacktrace/rbegin
---


```cpp
dcl | num=1 | since=c++23 |
const_reverse_iterator rbegin()  const noexcept;
dcl | num=2 | since=c++23 |
const_reverse_iterator crbegin() const noexcept;
```

Returns a reverse iterator to the first entry of the reversed `basic_stacktrace`. It corresponds to the last entry of the original `basic_stacktrace`. If the `basic_stacktrace` is empty, the returned iterator is equal to `rend()`.

## Parameters

(none)

## Return value

Reverse iterator to the first entry.

## Complexity

Constant.

## Example


## See also


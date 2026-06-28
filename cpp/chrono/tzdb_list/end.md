---
title: std::chrono::tzdb_list::end
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/tzdb_list/end
---


```cpp
dcl|since=c++20|1=
const_iterator end() const noexcept;
dcl|since=c++20|1=
const_iterator cend() const noexcept;
```

Returns the past-the-end iterator of the `tzdb_list`. Attempting to dereference this iterator results in undefined behavior.

## Return value

The past-the-end iterator.

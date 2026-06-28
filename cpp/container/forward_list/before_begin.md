---
title: cbefore_begin
type: Containers
source: https://en.cppreference.com/w/cpp/container/forward_list/before_begin
---


```cpp
dcl|since=c++11|
iterator before_begin() noexcept;
dcl|since=c++11|
const_iterator before_begin() const noexcept;
dcl|since=c++11|
const_iterator cbefore_begin() const noexcept;
```

Returns an iterator to the element before the first element of the container. This element acts as a placeholder, attempting to access it results in undefined behavior. The only usage cases are in functions `insert_after()`, `emplace_after()`, `erase_after()`, `splice_after()` and the increment operator: incrementing the before-begin iterator gives exactly the same iterator as obtained from `begin()`/`cbegin()`.

## Parameters

(none)

## Return value

Iterator to the element before the first element.

## Complexity

Constant.

## Example


## See also


| cpp/container/dsc begin|forward_list | (see dedicated page) |
| cpp/container/dsc end|forward_list | (see dedicated page) |


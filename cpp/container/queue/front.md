---
title: std::queue::front
type: Containers
source: https://en.cppreference.com/w/cpp/container/queue/front
---


```cpp
dcl|
reference front();
dcl|
const_reference front() const;
```

Returns reference to the first element in the queue. This element will be the first element to be removed on a call to `pop()`. Effectively calls `c.front()`.

## Parameters

(none)

## Return value

Reference to the first element.

## Complexity

Constant.

## See also


| cpp/container/dsc back|queue | (see dedicated page) |
| cpp/container/dsc pop|queue | (see dedicated page) |


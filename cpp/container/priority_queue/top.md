---
title: std::priority_queue::top
type: Containers
source: https://en.cppreference.com/w/cpp/container/priority_queue/top
---

ddcl|
const_reference top() const;
Returns reference to the top element in the priority queue. This element will be removed on a call to `pop()`. If default comparison function is used, the returned element is also the greatest among the elements in the queue.

## Return value

Reference to the top element as if obtained by a call to `c.front()`.

## Complexity

Constant.

## Example


## See also


| cpp/container/dsc pop|priority_queue | (see dedicated page) |


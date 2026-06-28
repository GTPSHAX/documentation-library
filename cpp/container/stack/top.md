---
title: std::stack::top
type: Containers
source: https://en.cppreference.com/w/cpp/container/stack/top
---


```cpp
dcl|num=1|
reference top();
dcl|num=2|
const_reference top() const;
```

Returns reference to the top element in the stack. This is the most recently pushed element. This element will be removed on a call to `pop()`. Equivalent to: .

## Parameters

(none)

## Return value

Reference to the last element.

## Complexity

Constant.

## Example


### Example

```cpp
#include <iostream>
#include <stack>

void reportStackSize(const std::stack<int>& s)
{
    std::cout << s.size() << " elements on stack\n";
}

void reportStackTop(const std::stack<int>& s)
{
    // Leaves element on stack
    std::cout << "Top element: " << s.top() << '\n';
}

int main()
{
    std::stack<int> s;
    s.push(2);
    s.push(6);
    s.push(51);

    reportStackSize(s);
    reportStackTop(s);

    reportStackSize(s);
    s.pop();

    reportStackSize(s);
    reportStackTop(s);
}
```


**Output:**
```
3 elements on stack
Top element: 51
3 elements on stack
2 elements on stack
Top element: 6
```


## See also


| cpp/container/dsc push|stack | (see dedicated page) |
| cpp/container/dsc pop|stack | (see dedicated page) |


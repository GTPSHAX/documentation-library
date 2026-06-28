---
title: std::list::size
type: Containers
source: https://en.cppreference.com/w/cpp/container/list/size
---


```cpp
dcl|until=c++11|
size_type size() const;
dcl|since=c++11|
size_type size() const noexcept;
```

Returns the number of elements in the container, i.e. `std::distance(begin(), end())`.

## Return value

The number of elements in the container.

## Complexity

<sup>(until C++11)</sup> Constant or linear.
<sup>(since C++11)</sup> Constant.

## Example


### Example

```cpp
#include <iostream>
#include <list>

int main()
{ 
    std::list<int> nums{1, 3, 5, 7};

    std::cout << "nums contains " << nums.size() << " elements.\n";
}
```


**Output:**
```
nums contains 4 elements.
```


## See also


| cpp/container/dsc empty|list | (see dedicated page) |
| cpp/container/dsc max_size|list | (see dedicated page) |
| cpp/container/dsc resize|list | (see dedicated page) |


---
title: keyword: alignof
type: Keywords
source: https://en.cppreference.com/w/cpp/keyword/alignof
---


## Usage

* `alignof` operator

## Example


### Example

```cpp
#include <cstddef>
#include <iostream>

int main()
{
    std::cout << alignof(std::max_align_t) << '\n';
}
```


**Output:**
```
16
```


## See also

* `alignas`

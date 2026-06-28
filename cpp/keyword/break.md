---
title: keyword: break
type: Keywords
source: https://en.cppreference.com/w/cpp/keyword/break
---


## Usage

* `break` statement: as the declaration of the statement

## Example


### Example

```cpp
#include <iostream>

int main() noexcept
{
    for (int i{0}; i < 69; ++i)
    {
        if (i == 3) [[unlikely]]
            break; // breaks from the 'for' loop
        std::cout << i;
    }
}
```


**Output:**
```
012
```


## See also


---
title: keyword: do
type: Keywords
source: https://en.cppreference.com/w/cpp/keyword/do
---


## Usage

* `do-while` loop: as the declaration of the loop

## Example


### Example

```cpp
#include <iostream>

int main() noexcept
{
    int i{0};

    // executes statement 'std::cout << ++i;'
    // before checking the condition 'i <= 2'
    do
        std::cout << ++i;
    while (i <= 2);
}
```


**Output:**
```
123
```


## See also


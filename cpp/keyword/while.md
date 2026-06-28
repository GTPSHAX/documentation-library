---
title: keyword: while
type: Keywords
source: https://en.cppreference.com/w/cpp/keyword/while
---


## Usage

* `cpp/language/while` loop: as the declaration of the loop
* `cpp/language/do|do-while` loop: as the declaration of the terminating condition of the loop

## Example


### Example

```cpp
#include <iostream>

int main() noexcept
{
    int i{3};

    // The following 'while' loop statement:
    // 1. (condition) Checks if value of the variable 'i' is greater than zero
    //                and if not, ends the loop execution with end of this point.
    //                Post-decrements the variable 'i' (decreases its value by 1).
    // 2. (statement) Writes out a current value of the variable 'i' to the stdout.
    // 3.             Returns to the point 1 (condition).

    while (i --> 0)     // condition: i-- > 0
        std::cout << i; // statement: std::cout << i;
}
```


**Output:**
```
210
```


## See also


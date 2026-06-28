---
title: keyword: for
type: Keywords
source: https://en.cppreference.com/w/cpp/keyword/for
---


## Usage

* `cpp/language/for` loop: as the declaration of the loop
rrev|since=c++11|
* range-based `cpp/language/range-for|for` loop: as the declaration of the loop

## Example


### Example

```cpp
#include <iostream>

int main() noexcept
{
    // The following 'for' loop statement:
    // 1. (init-statement) Declares an integer named 'i' and initializes it with value '0'.
    // 2. (condition)      Checks if i is less than 3 and if not, ends the loop execution.
    // 3. (statement)      Writes out a current value of the integer 'i' to the stdout.
    // 4. (expression)     Pre-increments the integer 'i' (increases its value by 1).
    // 5.                  Returns to the point 2 (condition).

                                // init-statement: int i{0};
                                // condition:      i < 3
    for (int i{0}; i < 3; ++i)  // expression:     ++i
        std::cout << i;         // statement:      std::cout << i;
}
```


**Output:**
```
012
```


## See also


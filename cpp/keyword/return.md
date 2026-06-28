---
title: keyword: return
type: Keywords
source: https://en.cppreference.com/w/cpp/keyword/return
---


## Usage

* `cpp/language/return` statement: as the declaration of the statement

## Example


### Example

```cpp
#include <cstdlib>
#include <iostream>

[[nodiscard]] constexpr auto clamp(int value, int min, int max) noexcept
{
    if (value <= min)
        return min;
    else if (max <= value)
        return max;

    return value;
    // won't be executed past 'return' statement

    std::exit(value);
}

int main() noexcept
{
    std::cout << clamp(1, 2, 4);
    std::cout << clamp(3, 2, 4);
    std::cout << clamp(5, 2, 4);

    return 0; // the value '0' that in main() indicates a success
}
```


**Output:**
```
234
```


## See also


---
title: std::bad_function_call
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/bad_function_call
---

ddcl|header=functional|
class bad_function_call;
`std::bad_function_call` is the type of the exception thrown by  if the function wrapper has no target.

## Member functions


## Example


### Example

```cpp
#include <functional>
#include <iostream>

int main()
{
    std::function<int()> f = nullptr;
    try
    {
        f();
    }
    catch (const std::bad_function_call& e)
    {
        std::cout << e.what() << '\n';
    }
}
```


**Output:**
```
bad function call
```


## Defect reports


## See also


| cpp/utility/functional/dsc function | (see dedicated page) |


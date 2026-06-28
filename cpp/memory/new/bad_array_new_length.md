---
title: std::bad_array_new_length
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/new/bad_array_new_length
---

ddcl|header=new|since=c++11|
class bad_array_new_length;
`std::bad_array_new_length` is the type of the object thrown as exceptions by the new-expressions to report invalid array lengths if
# Array length is negative,
# Total size of the new array would exceed implementation-defined maximum value,
# The number of initializer-clauses exceeds the number of elements to initialize.
Only the first array dimension may generate this exception; dimensions other than the first are constant expressions and are checked at compile time.

## Member functions


## Notes


## Example


### Example

```cpp
#include <climits>
#include <iostream>
#include <new>

int main()
{
    try
    {
        int negative = -1;
        new int[negative];
    }
    catch (const std::bad_array_new_length& e)
    {
        std::cout << "1) " << e.what() << ": negative size\n";
    }

    try
    {
        int small = 1;
        new int[small]{1,2,3};
    }
    catch (const std::bad_array_new_length& e)
    {
        std::cout << "2) " << e.what() << ": too many initializers\n";
    }

    try
    {
        long large = LONG_MAX;
        new int[large][1000];
    } 
    catch (const std::bad_array_new_length& e)
    {
        std::cout << "3) " << e.what() << ": too large\n";
    }

    std::cout << "End\n";
}
```


**Output:**
```
1) std::bad_array_new_length: negative size
2) std::bad_array_new_length: too many initializers
3) std::bad_array_new_length: too large
End
```


## See also


| cpp/memory/new/dsc operator_new | (see dedicated page) |
| cpp/memory/new/dsc bad_alloc | (see dedicated page) |


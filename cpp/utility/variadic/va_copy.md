---
title: va_copy
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variadic/va_copy
---


```cpp
**Header:** `<`cstdarg`>`
dcl|since=c++11|
void va_copy( std::va_list dest, std::va_list src );
```

The `va_copy` macro copies `src` to `dest`.
`va_end` should be called on `dest` before the function returns or any subsequent re-initialization of `dest` (via calls to `va_start` or `va_copy`).

## Parameters


### Parameters

- `dest` - an instance of the `va_list` type to initialize
- `src` - the source `va_list` that will be used to initialize `dest`

## Expanded value

(none)

## Example


### Example

```cpp
#include <cmath>
#include <cstdarg>
#include <iostream>

double sample_stddev(int count, ...) 
{
    double sum = 0;
    std::va_list args1;
    va_start(args1, count);
    std::va_list args2;
    va_copy(args2, args1);
    for (int i = 0; i < count; ++i)
    {
        double num = va_arg(args1, double);
        sum += num;
    }
    va_end(args1);
    double mean = sum / count;

    double sum_sq_diff = 0;
    for (int i = 0; i < count; ++i)
    {
        double num = va_arg(args2, double);
        sum_sq_diff += (num - mean) * (num - mean);
    }
    va_end(args2);
    return std::sqrt(sum_sq_diff / count);
}

int main() 
{
    std::cout << sample_stddev(4, 25.0, 27.3, 26.9, 25.7) << '\n';
}
```


**Output:**
```
0.920258
```


## See also


| cpp/utility/variadic/dsc va_start | (see dedicated page) |
| cpp/utility/variadic/dsc va_arg | (see dedicated page) |
| cpp/utility/variadic/dsc va_end | (see dedicated page) |


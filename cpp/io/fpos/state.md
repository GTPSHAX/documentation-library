---
title: std::fpos::state
type: Input/output
source: https://en.cppreference.com/w/cpp/io/fpos/state
---


```cpp
dcl|num=1|
State state() const;
dcl|num=2|
void state( State st );
```

Manages the file position state.
1. Returns the value of the file position state.
2. Replaces the file position state with the value of `st`.
For the specializations of `std::fpos` that are used in the standard library, `State` is always `std::mbstate_t`.

## Parameters


### Parameters

- `st` - new value for the state

## Return value

1. The current value of the `fpos` state.
2. (none)

## Example


### Example

```cpp
#include <cwchar>
#include <iostream>
#include <sstream>

int main()
{
    std::istringstream s("test");
    std::mbstate_t st = s.tellg().state();

    if (std::mbsinit(&st))
        std::cout << "The stream is in the initial shift state\n";
}
```


**Output:**
```
The stream is in the initial shift state
```


## Defect reports


## See also


| cpp/string/multibyte/dsc mbstate_t | (see dedicated page) |


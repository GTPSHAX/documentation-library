---
title: std::basic_ios::setstate
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios/setstate
---


```cpp
dcl|
void setstate( iostate state );
```

Sets the stream error flags `state` in addition to currently set flags. Essentially calls `clear(rdstate() . May throw an exception.

## Parameters


### Parameters

- `state` - stream error state flags to set. It can be a combination of the following constants:

## Return value

(none)

## Example


### Example

```cpp
#include <iostream>
#include <sstream>

int main()
{
    std::ostringstream stream;

    if (!stream.fail())
        std::cout << "stream is not fail\n";

    stream.setstate(std::ios_base::failbit);

    if (stream.fail())
        std::cout << "now stream is fail\n";

    if (!stream.good())
        std::cout << "and stream is not good\n";
}
```


**Output:**
```
stream is not fail
now stream is fail
and stream is not good
```


## See also


| cpp/io/basic_ios/dsc rdstate | (see dedicated page) |
| cpp/io/basic_ios/dsc clear | (see dedicated page) |


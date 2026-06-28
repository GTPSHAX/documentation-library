---
title: std::basic_ios::rdstate
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios/rdstate
---


```cpp
dcl|1=
iostate rdstate() const;
```

Returns the current stream error state.

## Parameters

(none)

## Return value

current stream error state. It is a bitmask type and can be a combination of the following constants:

## Example


### Example

```cpp
#include <iostream>
#include <sstream>

int main()
{
    std::ostringstream stream;

    if (stream.rdstate() == std::ios_base::goodbit)
        std::cout << "stream state is goodbit\n";

    stream.setstate(std::ios_base::eofbit);

    // check state is exactly eofbit (no failbit and no badbit)
    if (stream.rdstate() == std::ios_base::eofbit)
        std::cout << "stream state is eofbit\n";
}
```


**Output:**
```
stream state is goodbit
stream state is eofbit
```


## See also


| cpp/io/basic_ios/dsc setstate | (see dedicated page) |
| cpp/io/basic_ios/dsc clear | (see dedicated page) |


---
title: std::setiosflags
type: Input/output
source: https://en.cppreference.com/w/cpp/io/manip/setiosflags
---

ddcl|header=iomanip|
/*unspecified*/ setiosflags( std::ios_base::fmtflags mask );
When used in an expression `out << setiosflags(mask)` or `in >> setiosflags(mask)`, sets all format flags of the stream `out` or `in` as specified by the `mask`.

## Parameters


### Parameters

- `mask` - bitmask of the flags to set

## Return value


## Example


### Example

```cpp
#include <iomanip>
#include <iostream>

int main()
{
    std::cout << std::resetiosflags(std::ios_base::dec) 
              << std::setiosflags(  std::ios_base::hex
                                  {{!
```

| std::ios_base::showbase) << 42 << '\n';
}
|output=
0X2A

## Defect reports


## See also


| cpp/io/ios_base/dsc setf | (see dedicated page) |
| cpp/io/manip/dsc resetiosflags | (see dedicated page) |


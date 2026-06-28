---
title: std::resetiosflags
type: Input/output
source: https://en.cppreference.com/w/cpp/io/manip/resetiosflags
---

ddcl|header=iomanip|
/*unspecified*/ resetiosflags( std::ios_base::fmtflags mask );
When used in an expression `out << resetiosflags(mask)` or `in >> resetiosflags(mask)`, clears all format flags of the stream `out` or `in` as specified by the `mask`.

## Parameters


### Parameters

- `mask` - bitmask of the flags to clear

## Return value


## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <sstream>

int main()
{
    std::istringstream in("10 010 10 010 10 010");
    int n1, n2;

    in >> std::oct >> n1 >> n2;
    std::cout << "Parsing \"10 010\" with std::oct gives: " << n1 << ' ' << n2 << '\n';

    in >> std::dec >> n1 >> n2;
    std::cout << "Parsing \"10 010\" with std::dec gives: " << n1 << ' ' << n2 << '\n';

    in >> std::resetiosflags(std::ios_base::basefield) >> n1 >> n2;
    std::cout << "Parsing \"10 010\" with autodetect gives: " << n1 << ' ' << n2 << '\n';
}
```


**Output:**
```
Parsing "10 010" with std::oct gives: 8 8
Parsing "10 010" with std::dec gives: 10 10
Parsing "10 010" with autodetect gives: 10 8
```


## Defect reports


## See also


| cpp/io/ios_base/dsc setf | (see dedicated page) |
| cpp/io/manip/dsc setiosflags | (see dedicated page) |


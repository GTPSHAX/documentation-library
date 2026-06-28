---
title: keyword: and_eq
type: Keywords
source: https://en.cppreference.com/w/cpp/keyword/and_eq
---


## Usage

* alternative operators: as an alternative for `1=&=`

## Example


### Example

```cpp
#include <bitset>
#include <iostream>

int main()
{
    std::bitset<4> mask("1100");
    std::bitset<4> val("0111");
    val and_eq mask;
    std::cout << val << '\n';
}
```


**Output:**
```
0100
```


## See also


---
title: std::basic_string::push_back
type: Strings
source: https://en.cppreference.com/w/cpp/string/basic_string/push_back
---

ddcla|constexpr=c++20|
void push_back( CharT ch );
Appends the given character `ch` to the end of the string.

## Parameters


### Parameters

- `ch` - the character to append

## Return value

(none)

## Complexity

Amortized constant.

## Exceptions


## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <string>

int main()
{
    std::string str{"Short string"};
    std::cout << "1) " << std::quoted(str) << ", size: " << str.size() << '\n';

    str.push_back('!');
    std::cout << "2) " << std::quoted(str) << ", size: " << str.size() << '\n';
}
```


**Output:**
```
1) "Short string", size: 12
2) "Short string!", size: 13
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-847 | C++98 | there was no exception safety guarantee | added strong exception safety guarantee |


## See also


| cpp/string/basic_string/dsc pop_back | (see dedicated page) |


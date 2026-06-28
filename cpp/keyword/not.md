---
title: keyword: not
type: Keywords
source: https://en.cppreference.com/w/cpp/keyword/not
---


## Usage

* alternative operators: as an alternative for `!`

## Example


### Example

```cpp
#include <iostream>

void show(bool z, const char* s, int n)
{
    const char* r{z ? " true  " : " false "};
    if (n == 0) std::cout << "┌───────────┬─────────┐\n";
    if (n <= 1) std::cout << "│ " <<s<< " │ "<<r<<" │\n";
    if (n == 1) std::cout << "└───────────┴─────────┘\n";
}

int main()
{
    show(not true , "not true ", 0);
    show(not false, "not false", 1);
}
```


**Output:**
```
┌───────────┬─────────┐
│ not true  │  false  │
│ not false │  true   │
└───────────┴─────────┘
```


## See also


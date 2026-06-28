---
title: continue statement
type: Language
source: https://en.cppreference.com/w/cpp/language/continue
---


# tt|continue

Terminates the current iteration.

## Syntax


**Syntax:**

- `**`continue`** **`;`**`

### Parameters

- `{{spar` - attr|<sup>(C++11)</sup> any number of `attributes`

## Explanation

`continue` statements must be `enclosed` by any of the following statements:
*  (`for`, `range-`for``, `while` or `do-while`)
rrev|since=c++26|
*  (`template for`)

### For iteration statements

When executing a `continue` statement, if the innermost such enclosing statement is an iteration statement, then control passes to the end of the iteration element's *statement* (i.e. the loop body).

```cpp
while (/* ... */)
{
    /* executed statements */
    continue;
    /* skipped statements */
}

do
{
    /* executed statements */
    continue;
    /* skipped statements */
} while (/* ... */)

for (/* ... */)
{
    /* executed statements */
    continue;
    /* skipped statements */
}
```

rrev|since=c++26|

### For expansion statements

When executing a `continue` statement, if the innermost such enclosing statement is an expansion statement, then control passes to the end of the expansion element's current expansion item's *compound-statement*.

```cpp
template for (/* ... */)
{
    if (/* current item is the Nth */)
        continue;
    /* statements only skipped for the Nth item */
}
```


## Keywords

`cpp/keyword/continue`

## Example


### Example

```cpp
#include <iostream>

int main()
{
    for (int i = 0; i < 10; ++i)
    {
        if (i != 5)
            continue;
        std::cout << i << ' ';      // this statement is skipped each time i != 5
    }
    std::cout << '\n';

    for (int j = 0; 2 != j; ++j)
        for (int k = 0; k < 5; ++k) // only this loop is affected by continue
        {
            if (k == 3)
                continue;
            // this statement is skipped each time k == 3:
            std::cout << '(' << j << ',' << k << ") ";
        }
    std::cout << '\n';
}
```


**Output:**
```
5
(0,0) (0,1) (0,2) (0,4) (1,0) (1,1) (1,2) (1,4)
```


## See also


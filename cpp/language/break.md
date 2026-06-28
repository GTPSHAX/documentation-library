---
title: break statement
type: Language
source: https://en.cppreference.com/w/cpp/language/break
---


# tt|break

Terminates specific enclosing statements.

## Syntax


**Syntax:**

- `**`break`** **`;`**`

### Parameters

- `{{spar` - attr|<sup>(C++11)</sup> any number of `attributes`

## Explanation

`break` statements must be `enclosed` by any of the following statements:
*  (`for`, `range-`for``, `while` or `do-while`)
rrev|since=c++26|
*  (`template for`)
* `switch` statements
Executing a `break` statement causes termination of the innermost such enclosing statement, then control passes to the statement following the terminated statement (if any).

## Notes

As with any block exit, all automatic storage objects declared in enclosing compound statement or in the *condition* of a loop/switch are destroyed, in reverse order of construction, before the execution of the first line following the enclosing loop.
A `break` statement cannot be used to break out of multiple nested loops. The `goto` statement may be used for this purpose.

## Keywords

`cpp/keyword/break`

## Example


### Example

```cpp
#include <iostream>

int main()
{
    int i = 2;
    switch (i)
    {
        case 1: std::cout << "1";   // <---- maybe warning: fall through
        case 2: std::cout << "2";   // execution starts at this case label (+warning)
        case 3: std::cout << "3";   // <---- maybe warning: fall through
        case 4:                     // <---- maybe warning: fall through
        case 5: std::cout << "45";  //
                break;              // execution of subsequent statements is terminated
        case 6: std::cout << "6";
    }
    std::cout << '\n';

    for (char c = 'a'; c < 'c'; c++)
    {
        for (int i = 0; i < 5; i++)      // only this loop is affected by break
        {                                //
            if (i == 2)                  //
                break;                   //
            std::cout << c << i << ' ';  //
        }
    }
    std::cout << '\n';
}
```


**Output:**
```
2345
a0 a1 b0 b1
```


## See also


| cpp/language/attributes/dsc fallthrough | (see dedicated page) |


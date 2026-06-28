---
title: std::chrono::duration::operators
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/duration/operator_arith2
---


```cpp
|
duration& operator++();
|
duration operator++( int );
|
duration& operator--();
|
duration operator--( int );
```

Increments or decrements the number of ticks for this duration.
If `rep_` is a member variable holding the number of ticks in a duration object,
1. Equivalent to `++rep_; return *this;`.
2. Equivalent to `return duration(rep_++)`.
3. Equivalent to `--rep_; return *this;`.
4. Equivalent to `return duration(rep_--);`.

## Parameters

(none)

## Return value

@1,3@ A reference to this duration after modification.
@2,4@ A copy of the duration made before modification.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    std::chrono::hours h(1);
    std::chrono::minutes m = ++h;
    m--;
    std::cout << m.count() << " minutes\n";
}
```


**Output:**
```
119 minutes
```


## See also


| cpp/chrono/duration/dsc operator_arith3 | (see dedicated page) |
| cpp/chrono/duration/dsc operator_arith4 | (see dedicated page) |


---
title: std::basic_istream::peek
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_istream/peek
---

ddcl|
int_type peek();
Behaves as *UnformattedInputFunction*. After constructing and testing the sentry object, reads the next character from the input stream without extracting it.

## Parameters

(none)

## Return value

If `good() , returns the next character as obtained by `rdbuf()->sgetc()`.
Otherwise, returns `Traits::eof()`.

## Exceptions


## Example


### Example

```cpp
#include <iostream>
#include <sstream>

int main()
{
    std::istringstream s1("Hello, world.");
    char c1 = s1.peek();
    char c2 = s1.get();
    std::cout << "Peeked: " << c1 << " got: " << c2 << '\n';
}
```


**Output:**
```
Peeked: H got: H
```


## See also


| cpp/io/basic_streambuf/dsc sgetc | (see dedicated page) |
| cpp/io/basic_istream/dsc get | (see dedicated page) |
| cpp/io/basic_istream/dsc unget | (see dedicated page) |


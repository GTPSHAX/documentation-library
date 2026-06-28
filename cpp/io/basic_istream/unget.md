---
title: std::basic_istream::unget
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_istream/unget
---

ddcl|
basic_istream& unget();
Makes the most recently extracted character available again.
First clears `cpp/io/ios_base/iostate|eofbit`, then behaves as *UnformattedInputFunction*. After constructing and checking the sentry object, if any `ios_base::iostate` flags are set, the function sets `failbit` and returns. Otherwise, calls `rdbuf()->sungetc()`.
If `rdbuf()->sungetc()` returns `Traits::eof()`, calls `setstate(badbit)`.
In any case, sets the `gcount()` counter to zero.

## Parameters

(none)

## Return value

`*this`

## Exceptions


## Example


### Example

```cpp
#include <iostream>
#include <sstream>

int main()
{
    std::istringstream s1("Hello, world.");
    char c1 = s1.get();
    if (s1.unget())
    {
        char c2 = s1.get();
        std::cout << "Got: '" << c1 << "'. Got again: '" << c2 << "'.\n";
    }
}
```


**Output:**
```
Got: 'H'. Got again: 'H'.
```


## Defect reports


## See also


| cpp/io/basic_streambuf/dsc sungetc | (see dedicated page) |
| cpp/io/basic_istream/dsc get | (see dedicated page) |
| cpp/io/basic_istream/dsc peek | (see dedicated page) |
| cpp/io/basic_istream/dsc putback | (see dedicated page) |


---
title: std::basic_istream::putback
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_istream/putback
---

ddcl|
basic_istream& putback( char_type ch );
Puts the character `ch` back to the input stream so the next extracted character will be `ch`.
First clears `eofbit`, then behaves as *UnformattedInputFunction*. After constructing and checking the sentry object, if  is not null, calls `rdbuf()->sputbackc(ch)`, which calls `rdbuf()->pbackfail(ch)` if `ch` does not equal the most recently extracted character.
If `rdbuf()` is null or if `rdbuf->sputbackc(ch)` returns `Traits::eof()`, calls `setstate(badbit)`.
In any case, sets the  counter to zero.

## Parameters


### Parameters

- `ch` - character to put into input stream

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
    std::stringstream s1("Hello, world"); // IO stream
    s1.get();
    if (s1.putback('Y')) // modifies the buffer
        std::cout << s1.rdbuf() << '\n';
    else
        std::cout << "putback failed\n";

    std::cout << "--\n";

    std::istringstream s2("Hello, world"); // input-only stream
    s2.get();
    if (s2.putback('Y')) // cannot modify input-only buffer
        std::cout << s2.rdbuf() << '\n';
    else
        std::cout << "putback failed\n"; 
    s2.clear();

    std::cout << "--\n";

    if (s2.putback('H')) // non-modifying putback
        std::cout << s2.rdbuf() << '\n';
    else
        std::cout << "putback failed\n";
}
```


**Output:**
```
Yello, world
--
putback failed
--
Hello, world
```


## Defect reports


## See also


| cpp/io/basic_streambuf/dsc sputbackc | (see dedicated page) |
| cpp/io/basic_istream/dsc unget | (see dedicated page) |
| cpp/io/basic_istream/dsc peek | (see dedicated page) |


---
title: std::basic_istream::tellg
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_istream/tellg
---

ddcl|
pos_type tellg();
Returns input position indicator of the current associated `streambuf` object.
Behaves as *UnformattedInputFunction*, except that `gcount()` is not affected. After constructing and checking the sentry object, if `1=fail() == true`, returns `pos_type(-1)`. Otherwise, returns `rdbuf()->pubseekoff(0, std::ios_base::cur, std::ios_base::in)`.

## Parameters

(none)

## Return value

The current position of the get pointer on success, `pos_type(-1)` on failure.

## Exceptions


## Example


### Example

```cpp
#include <iostream>
#include <sstream>
#include <string>

int main()
{
    std::string str = "Hello, world";
    std::istringstream in(str);
    std::string word;
    in >> word;
    std::cout << "After reading the word \"" << word
              << "\" tellg() returns " << in.tellg() << '\n';
}
```


**Output:**
```
After reading the word "Hello," tellg() returns 6
```


## See also


| cpp/io/basic_filebuf/dsc seekoff | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc seekoff | (see dedicated page) |
| cpp/io/strstreambuf/dsc seekoff | (see dedicated page) |
| cpp/io/basic_istream/dsc seekg | (see dedicated page) |
| cpp/io/basic_ostream/dsc tellp|mem=std::basic_ostream | (see dedicated page) |
| cpp/io/basic_ostream/dsc seekp|mem=std::basic_ostream | (see dedicated page) |


---
title: std::basic_osyncstream::operator=
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_osyncstream/operator=
---


```cpp
dcl|since=c++20|1=
basic_osyncstream& operator=( std::basic_osyncstream&& other );
```

Move-assigns a synchronized output stream:
Move-assigns the wrapped `std::basic_syncbuf` from the corresponding member of `other` (after this move-assignment, `other.get_wrapped()` returns a null pointer and destruction of `other` produces no output; any pending buffered output will be emitted) and move-assigns the base `std::basic_ostream` (this swaps all stream state variables except for `rdbuf` between `*this` and `other`)

## Parameters


### Parameters

- `other` - another synchronized output stream to move from

## Return value

`*this`

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <sstream>
#include <syncstream>
#include <utility>

int main()
{
    std::osyncstream out(std::cout);
    out << "test\n";
    std::ostringstream str_out;
    std::osyncstream{str_out} = std::move(out); // Note that out is emitted here
    std::cout << "str_out = " << std::quoted(str_out.view()) << '\n';
}
```


**Output:**
```
test
str_out = ""
```


## Defect reports


## See also


| cpp/io/basic_osyncstream/dsc constructor | (see dedicated page) |
| cpp/io/basic_osyncstream/dsc destructor | (see dedicated page) |
| cpp/io/basic_osyncstream/dsc emit | (see dedicated page) |


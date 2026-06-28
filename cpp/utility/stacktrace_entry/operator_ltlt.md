---
title: std::operator<<(std::stacktrace_entry)
type: Diagnostics
source: https://en.cppreference.com/w/cpp/utility/stacktrace_entry/operator_ltlt
---

ddcl|header=stacktrace|since=c++23|
std::ostream& operator<<( std::ostream& os, const std::stacktrace_entry& f );
Inserts the description of `f` into the output stream `os`. Equivalent to `return os << std::to_string(f);`.

## Parameters


### Parameters

- `os` - an output stream
- `f` - a `stacktrace_entry` whose description is to be inserted

## Return value

`os`

## Example


### Example

```cpp
#include <iostream>
#include <stacktrace>

int main()
{
    for (const auto& f : std::stacktrace::current())
        std::cout << f << '\n';
}
```


**Output:**
```
<!--obtained from Boost.Stacktrace-->
0x0000000000402AA7 in ./prog.exe
__libc_start_main in /lib/x86_64-linux-gnu/libc.so.6
0x00000000004029B9 in ./prog.exe
```


## See also


| cpp/utility/basic_stacktrace/dsc operator ltlt | (see dedicated page) |


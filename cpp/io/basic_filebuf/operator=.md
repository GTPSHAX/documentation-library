---
title: std::basic_filebuf::operator=
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/operator=
---


```cpp
dcl|num=1|since=c++11|1=
std::basic_filebuf& operator=( std::basic_filebuf&& rhs );
dcl|num=2|1=
std::basic_filebuf& operator=( const std::basic_filebuf& rhs ) = delete;
```

Assigns another `basic_filebuf` object.
1. First calls `close()` to close the associated file, then moves the contents of `rhs` into `*this`: the put and get buffers, the associated file, the locale, the openmode, the is_open flag, and any other state. After the move, `rhs` is not associated with a file and `1=rhs.is_open() == false`.
2. The copy assignment operator is deleted; `basic_filebuf` is not *CopyAssignable*.

## Parameters


### Parameters

- `rhs` - another `basic_filebuf` that will be moved from

## Return value

`*this`

## Example


### Example

```cpp
#include <cassert>
#include <fstream>
#include <iostream>
#include <string>

int main()
{
    std::ofstream{"test.in"} << "test\n"; // writes via a temporary object
    std::ifstream fin("test.in"); // read-only stream
    std::ofstream fout("test.out"); // write-only stream

    std::string s;
    std::getline(fin, s);
    std::cout << "s = [" << s << "]\n"; // s contains "test"

    assert(fout.is_open());
    *fin.rdbuf() = std::move(*fout.rdbuf());
    assert(!fout.is_open());

    std::getline(fin, s);
    std::cout << "s = [" << s << "]\n"; // s is empty input
}
```


**Output:**
```
s = [test]
s = []
```


## See also


| cpp/io/basic_filebuf/dsc basic_filebuf | (see dedicated page) |
| cpp/io/basic_filebuf/dsc swap | (see dedicated page) |


---
title: std::basic_filebuf::swap
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/swap
---


```cpp
dcl|since=c++11|
void swap( std::basic_filebuf& rhs );
```

Swaps the state and the contents of `*this` and `rhs`.

## Parameters


### Parameters

- `rhs` - another `basic_filebuf`

## Return value

(none)

## Notes

This function is called automatically when swapping `std::fstream` objects, it is rarely necessary to call it directly.

## Example


### Example

```cpp
#include <fstream>
#include <iostream>
#include <string>

int main()
{
    std::ifstream fin("test.in"); // read-only
    std::ofstream fout("test.out"); // write-only

    std::string s;
    getline(fin, s);
    std::cout << s << '\n'; // outputs the first line of test.in

    fin.rdbuf()->swap(*fout.rdbuf()); //swap the underlying buffers

    getline(fin, s); // fails: cannot read from a write-only filebuf
    std::cout << s << '\n'; // prints empty line
}
```


## See also


| cpp/io/basic_filebuf/dsc operator{{= | (see dedicated page) |
| cpp/io/basic_filebuf/dsc swap2 | (see dedicated page) |
| cpp/io/basic_fstream/dsc swap|basic_fstream | (see dedicated page) |


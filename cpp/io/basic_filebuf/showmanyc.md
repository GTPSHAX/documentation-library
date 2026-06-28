---
title: std::basic_filebuf::showmanyc
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_filebuf/showmanyc
---

ddcl|notes=|
protected:
virtual std::streamsize showmanyc()
If implemented, returns the number of characters left to read from the file.

## Return value

The number of characters available for reading from the file, or `-1` if the end of file was reached.

## Notes

This function is optional. If not implemented, this function returns `0` (since the base class version `std::basic_streambuf::showmanyc` gets called).
Whether implemented or not, this function is normally called by `std::basic_streambuf::in_avail` if the get area is empty.
The name of this function stands for “'''s'''tream: how many '''c'''haracters?”, so it is pronounced “'''S''' how many '''C'''", rather than “show many C”.

## Example


### Example

```cpp
#include <fstream>
#include <iostream>

struct mybuf : std::filebuf
{
    using std::filebuf::showmanyc;
};

int main()
{
    mybuf fin;
    fin.open("main.cpp", std::ios_base::in);
    std::cout << "showmanyc() returns " << fin.showmanyc() << '\n';
}
```


**Output:**
```
showmanyc() returns 254
```


## See also


| cpp/io/basic_streambuf/dsc in_avail | (see dedicated page) |
| cpp/io/basic_istream/dsc readsome | (see dedicated page) |


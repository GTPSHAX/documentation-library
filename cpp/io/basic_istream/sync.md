---
title: std::basic_istream::sync
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_istream/sync
---

ddcl|
int sync();
Synchronizes the input buffer with the associated data source.
Behaves as *UnformattedInputFunction*, except that `gcount()` is not affected. After constructing and checking the sentry object,
If `rdbuf()` is a null pointer, returns `-1`.
Otherwise, calls `rdbuf()->pubsync()`. If that function returns `-1`, calls `setstate(badbit)` and returns `-1`. Otherwise, returns `0`.

## Parameters

(none)

## Return value

`0` on success, `-1` on failure or if the stream does not support this operation (is unbuffered).

## Notes

As with `readsome()`, it is implementation-defined whether this function does anything with library-supplied streams. The intent is typically for the next read operation to pick up any changes that may have been made to the associated input sequence after the stream buffer last filled its get area. To achieve that, `sync()` may empty the get area, or it may refill it, or it may do nothing. A notable exception is Visual Studio, where this operation discards the unprocessed input when called with a standard input stream.

## Example


### Example

```cpp
#include <fstream>
#include <iostream>

void file_abc()
{
    std::ofstream f("test.txt");
    f << "abc\n";
}

void file_123()
{
    std::ofstream f("test.txt");
    f << "123\n";
}

int main()
{
    file_abc(); // file now contains "abc"
    std::ifstream f("test.txt");
    std::cout << "Reading from the file\n";
    char c;
    f >> c;
    std::cout << c;
    file_123(); // file now contains "123"
    f >> c;
    std::cout << c;
    f >> c;
    std::cout << c << '\n';
    f.close();

    file_abc(); // file now contains "abc"
    f.open("test.txt");
    std::cout << "Reading from the file, with sync()\n";
    f >> c;
    std::cout << c;
    file_123(); // file now contains "123"
    f.sync();
    f >> c;
    std::cout << c;
    f >> c;
    std::cout << c << '\n';
}
```


**Output:**
```
<!--Note: output as seen on Sun and IBM, but the Linux/gcc that was tested printed "abc" both times-->
Reading from the file
abc
Reading from the file, with sync()
a23
```


## Defect reports


## See also


| cpp/io/basic_streambuf/dsc sync | (see dedicated page) |
| cpp/io/basic_ostream/dsc flush | (see dedicated page) |


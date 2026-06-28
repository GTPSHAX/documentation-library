---
title: std::basic_istream::seekg
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_istream/seekg
---


```cpp
dcl|num=1|1=
basic_istream& seekg( pos_type pos );
dcl|num=2|1=
basic_istream& seekg( off_type off, std::ios_base::seekdir dir );
```

Sets input position indicator of the current associated `streambuf` object.
Before doing anything else, `seekg` clears `eofbit`.
`seekg` behaves as *UnformattedInputFunction*, except that `gcount()` is not affected. After constructing and checking the sentry object,
1. if `1=fail() != true`, sets the input position indicator to absolute (relative to the beginning of the file) value `pos`. Specifically, executes `rdbuf()->pubseekpos(pos, std::ios_base::in)` (`cpp/io/basic_streambuf/pubseekpos`, in turn, calls seekpos of the specific buffer, such as , , or ). In case of failure, calls `setstate(std::ios_base::failbit)`.
2. if `1=fail() != true`, sets the input position indicator to position `off`, relative to position, defined by `dir`. Specifically, executes `rdbuf()->pubseekoff(off, dir, std::ios_base::in)`. In case of failure, calls `setstate(std::ios_base::failbit)`.

## Parameters


### Parameters

- `pos` - absolute position to set the input position indicator to
- `off` - relative position (positive or negative) to set the input position indicator to
- `dir` - defines base position to apply the relative offset to. It can be one of the following constants:

## Return value

`*this`

## Exceptions


## Notes

`seekg(n)` is not necessarily equivalent to `seekg(n, ios::beg)`. `std::basic_ifstream`, for example, requires the absolute position `n` to come from `tellg()`.

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
    std::string word1, word2;

    in >> word1;
    in.seekg(0); // rewind
    in >> word2;

    std::cout << "word1 = " << word1 << '\n'
              << "word2 = " << word2 << '\n';
}
```


**Output:**
```
word1 = Hello,
word2 = Hello,
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-129 | C++98 | there was no way to indicate a failure | sets tt |


## See also


| cpp/io/basic_istream/dsc tellg | (see dedicated page) |
| cpp/io/basic_ostream/dsc tellp|mem=std::basic_ostream | (see dedicated page) |
| cpp/io/basic_ostream/dsc seekp|mem=std::basic_ostream | (see dedicated page) |
| cpp/io/basic_streambuf/dsc pubseekpos | (see dedicated page) |
| cpp/io/basic_filebuf/dsc seekpos | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc seekpos | (see dedicated page) |
| cpp/io/strstreambuf/dsc seekpos | (see dedicated page) |
| cpp/io/basic_streambuf/dsc pubseekoff | (see dedicated page) |
| cpp/io/basic_filebuf/dsc seekoff | (see dedicated page) |
| cpp/io/basic_stringbuf/dsc seekoff | (see dedicated page) |
| cpp/io/strstreambuf/dsc seekoff | (see dedicated page) |


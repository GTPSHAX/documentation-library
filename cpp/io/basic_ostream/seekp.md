---
title: std::basic_ostream::seekp
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ostream/seekp
---


```cpp
dcl|num=1|1=
basic_ostream& seekp( pos_type pos );
dcl|num=2|1=
basic_ostream& seekp( off_type off, std::ios_base::seekdir dir );
```

Sets the output position indicator of the current associated `streambuf` object.
rrev|since=c++11|
Behaves as *UnformattedOutputFunction* (except without actually performing output). After constructing and checking the sentry object,
1. if `1=fail() != true`, sets the output position indicator to absolute (relative to the beginning of the file) value `pos` by calling `rdbuf()->pubseekpos(pos, std::ios_base::out)`. In case of failure, calls `setstate(std::ios_base::failbit)`.
2. if `1=fail() != true`, sets the output position indicator to offset `off` relative to `dir` by calling `rdbuf()->pubseekoff(off, dir, std::ios_base::out)`. In case of failure, calls `setstate(std::ios_base::failbit)`.

## Parameters


### Parameters

- `pos` - absolute position to set the output position indicator to
- `off` - relative position (positive or negative) to set the output position indicator to
- `dir` - defines base position to apply the relative offset to. It can be one of the following constants:

## Return value

`*this`

## Exceptions

@1,2@ May throw `std::ios_base::failure` in case of failure, if `1=exceptions() & failbit != 0`.

## Example


### Example

```cpp
#include <iostream>
#include <sstream>

int main()
{
    std::ostringstream os("hello, world");
    os.seekp(7);
    os << 'W';
    os.seekp(0, std::ios_base::end);
    os << '!';
    os.seekp(0);
    os << 'H';
    std::cout << os.str() << '\n';
}
```


**Output:**
```
Hello, World!
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-129 | C++98 | there was no way to indicate a failure | sets tt |


## See also


| cpp/io/basic_ostream/dsc tellp | (see dedicated page) |
| cpp/io/basic_istream/dsc tellg | (see dedicated page) |
| cpp/io/basic_istream/dsc seekg | (see dedicated page) |


---
title: std::basic_istream::ignore
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_istream/ignore
---


```cpp
dcl|num=1|1=
basic_istream& ignore( std::streamsize count = 1, int_type delim = Traits::eof() );
dcl|num=2|1=
basic_istream& ignore( std::streamsize count, char_type delim );
```

1. Extracts and discards characters from the input stream until and including `delim`.
2. Equivalent to `return ignore(count, traits::to_int_type(delim));`. .
`ignore` behaves as an *UnformattedInputFunction*. After constructing and checking the sentry object, it extracts characters from the stream and discards them until any of the following conditions occurs:
* `count` characters were extracted. This test is disabled in the special case when `count` equals `std::numeric_limits<std::streamsize>::max()`.
* end of file conditions occurs in the input sequence, in which case the function calls `setstate(eofbit)`.
* the next available character `c` in the input sequence is `delim`, as determined by `Traits::eq_int_type(Traits::to_int_type(c), delim)`. The delimiter character is extracted and discarded. This test is disabled if `delim` is `Traits::eof()`.

## Parameters


### Parameters

- `count` - number of characters to extract
- `delim` - delimiting character to stop the extraction at. It is also extracted

## Return value

`*this`

## Exceptions


## Example


### Example

```cpp
#include <iostream>
#include <limits>
#include <sstream>

constexpr auto max_size = std::numeric_limits<std::streamsize>::max();

int main()
{
    std::istringstream input("1\n"
                             "some non-numeric input\n"
                             "2\n");
    for (;;)
    {
        int n;
        input >> n;

        if (input.eof() {{!!
```

break;
else if (input.fail())
{
input.clear(); // unset failbit
input.ignore(max_size, '\n'); // skip bad input
}
else
std::cout << n << '\n';
}
}
|output=
1
2

## Defect reports


## See also


| cpp/io/basic_istream/dsc get | (see dedicated page) |
| cpp/io/basic_istream/dsc getline | (see dedicated page) |


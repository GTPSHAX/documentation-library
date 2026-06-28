---
title: std::basic_ostream::sentry
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ostream/sentry
---


```cpp
dcl|1=
class sentry;
```

An object of class `basic_ostream::sentry` is constructed in local scope at the beginning of each member function of `std::basic_ostream` that performs output (both formatted and unformatted). Its constructor prepares the output stream: checks if the stream is already in a failed state, flushes the tie()'d output streams, and performs other implementation-defined tasks if necessary. Implementation-defined cleanup, as well as flushing of the output stream if necessary, is performed in the destructor, so that it is guaranteed to happen if exceptions are thrown during output.

## Member functions


| cpp/io/basic_ostream/sentry/dsc constructor | (see dedicated page) |
| cpp/io/basic_ostream/sentry/dsc operator bool | (see dedicated page) |

member|sentry| 2=
ddcl|1=
explicit sentry( std::basic_ostream<CharT, Traits>& os );
Prepares the stream for formatted output.
If `os.good()` is `false`, returns. Otherwise, if `os.tie()` is not a null pointer, calls `os.tie()->flush()` to synchronize the output sequence with external streams. During preparation, the constructor may call `setstate(failbit)` (which may throw `std::ios_base::failure`).
If after preparation is completed, `1=os.good() == true`, then any subsequent calls to `operator bool` will return `true`.

## Parameters


### Parameters

- `os` - output stream to prepare

## Exceptions

`std::ios_base::failure` if the end of file condition occurs.
member|~sentry|2=
ddcl|1=
~sentry();
If `(os.flags() & std::ios_base::unitbuf) && !std::uncaught_exception() && os.good())` is `true`, calls `os.rdbuf()->pubsync()`. If that function returns `-1`, sets `badbit` in `os.rdstate()` without propagating an exception.
member|operator bool|2=
ddcl|1=
explicit operator bool() const;
Checks whether the preparation of the output stream was successful.

## Parameters

(none)

## Return value

`true` if the preparation of the output stream was successful, `false` otherwise.

## Example


### Example

```cpp
#include <iostream>
#include <sstream>

struct Foo
{
    char n[6];
};

std::ostream& operator<<(std::ostream& os, Foo& f)
{
    std::ostream::sentry s(os);
    if (s)
        os.write(f.n, 5);
    return os;
}

int main()
{
    Foo f = {"abcde"};
    std::cout << f << '\n';
}
```


**Output:**
```
abcde
```


## Defect reports


## See also


| cpp/io/basic_ostream/dsc operator ltlt | (see dedicated page) |


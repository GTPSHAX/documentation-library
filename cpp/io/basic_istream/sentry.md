---
title: std::basic_istream::sentry
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_istream/sentry
---


```cpp
dcl|1=
class sentry;
```

An object of class `basic_istream::sentry` is constructed in local scope at the beginning of each member function of `std::basic_istream` that performs input (both formatted and unformatted). Its constructor prepares the input stream: checks if the stream is already in a failed state, flushes the tie()'d output streams, skips leading whitespace unless `noskipws` flag is set, and performs other implementation-defined tasks if necessary. All cleanup, if necessary, is performed in the destructor, so that it is guaranteed to happen if exceptions are thrown during input.

## Member types


## Member functions


| cpp/io/basic_istream/sentry/dsc constructor | (see dedicated page) |
| cpp/io/basic_istream/sentry/dsc destructor | (see dedicated page) |
| cpp/io/basic_istream/sentry/dsc operator bool | (see dedicated page) |

member|sentry|2=
ddcl|1=
explicit sentry( std::basic_istream<CharT, Traits>& is, bool noskipws = false );
Prepares the stream for formatted input.
If `is.good()` is `false`, calls `is.setstate(std::ios_base::failbit)` and returns. Otherwise, if `is.tie()` is not a null pointer, calls `is.tie()->flush()` to synchronize the output sequence with external streams. This call can be suppressed if the put area of `is.tie()` is empty. The implementation may defer the call to `flush()` until a call of `is.rdbuf()->underflow()` occurs. If no such call occurs before the sentry object is destroyed, it may be eliminated entirely.
If `noskipws` is zero and `is.flags() & std::ios_base::skipws` is nonzero, the function extracts and discards all whitespace characters until the next available character is not a whitespace character (as determined by the currently imbued locale in `is`). If `is.rdbuf()->sbumpc()` or `is.rdbuf()->sgetc()` returns `traits::eof()`, the function calls `setstate(std::ios_base::failbit  (which may throw `std::ios_base::failure`).
Additional implementation-defined preparation may take place, which may call `setstate(std::ios_base::failbit)` (which may throw `std::ios_base::failure`).
If after preparation is completed, `1=is.good() == true`, then any subsequent calls to `operator bool` will return `true`.

## Parameters


### Parameters

- `is` - input stream to prepare
- `noskipws` - `true` if whitespace should not be skipped

## Exceptions

`std::ios_base::failure` if the end of file condition occurs when skipping whitespace.
member|~sentry|2=
ddcl|1=
~sentry();
Does nothing.
member|operator bool|2=
ddcl|1=
explicit operator bool() const;
Checks whether the preparation of the input stream was successful.

## Parameters

(none)

## Return value

`true` if the initialization of the input stream was successful, `false` otherwise.

## Example


### Example

```cpp
#include <iostream>
#include <sstream>

struct Foo
{
    char n[5];
};

std::istream& operator>>(std::istream& is, Foo& f)
{
    std::istream::sentry s(is);
    if (s)
        is.read(f.n, 5);
    return is;
}

int main()
{
    std::string input = "   abcde";
    std::istringstream stream(input);
    Foo f;
    stream >> f;
    std::cout.write(f.n, 5);
    std::cout << '\n';
}
```


**Output:**
```
abcde
```


## Defect reports


## See also


| cpp/io/basic_istream/dsc operator_gtgt | (see dedicated page) |
| cpp/io/basic_istream/dsc operator_gtgt2 | (see dedicated page) |


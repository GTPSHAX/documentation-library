---
title: std::unitbuf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/manip/unitbuf
---


```cpp
**Header:** `<`ios`>`
dcl|num=1|
std::ios_base& unitbuf( std::ios_base& str );
dcl|num=2|
std::ios_base& nounitbuf( std::ios_base& str );
```

Enables or disables automatic flushing of the output stream after any output operation. Has no effect on input.
1. Enables the `unitbuf` flag in the stream `str` as if by calling `str.setf(std::ios_base::unitbuf)`.
2. Disables the `unitbuf` flag in the stream `str` as if by calling `str.unsetf(std::ios_base::unitbuf)`.
This is an I/O manipulator, it may be called with an expression such as `out << std::unitbuf` for any `out` of type `std::basic_ostream` or with an expression such as `in >> std::unitbuf` for any `in` of type `std::basic_istream`.

## Notes

Flushing is performed in the destructor of the `std::basic_ostream::sentry` object, which calls `str.rdbuf()->pubsync()` if `str.flags() & std::ios_base::unitbuf` is `true`.
The standard output objects `std::cerr` and `std::wcerr` have their `unitbuf` bit set by default.

## Parameters


### Parameters

- `str` - reference to I/O stream

## Return value

`str` (reference to the stream after manipulation).

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

template<typename Diff>
void log_progress(Diff d)
{
    std::cout << std::chrono::duration_cast<std::chrono::milliseconds>(d)
              << " ... ";
}

int main()
{
    volatile int sink = 0;
    std::cout << std::unitbuf; // enable automatic flushing

    const auto start = std::chrono::high_resolution_clock::now();
    for (int j = 0; j < 5; ++j)
    {
        for (int n = 0; n < 10000; ++n)
            for (int m = 0; m < 20000; ++m)
                sink += m * n; // do some work
        log_progress(std::chrono::high_resolution_clock::now() - start);
    }
    std::cout << '\n';
}
```


**Output:**
```
571ms ... 1146ms ... 1722ms ... 2294ms ... 2865ms ...
```


## See also


| cpp/io/manip/dsc flush | (see dedicated page) |
| cpp/io/manip/dsc endl | (see dedicated page) |


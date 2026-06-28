---
title: std::wcerr
type: Input/output
source: https://en.cppreference.com/w/cpp/io/cerr
---


```cpp
**Header:** `<`iostream`>`
dcl|num=1|1=
extern std::ostream cerr;
dcl|num=2|1=
extern std::wostream wcerr;
```

The global objects `std::cerr` and `std::wcerr` control output to a stream buffer of implementation-defined type (derived from `std::streambuf` and `std::wstreambuf`, respectively), associated with the standard C error output stream `stderr`.
These objects are guaranteed to be initialized during or before the first time an object of type `std::ios_base::Init` is constructed and are available for use in the constructors and destructors of static objects with ordered initialization (as long as  is included before the object is defined).
Unless `std::ios_base::sync_with_stdio(false)` has been issued, it is safe to concurrently access these objects from multiple threads for both formatted and unformatted output.
Once initialized, `1=(std::cerr.flags() & unitbuf) != 0` (same for `std::wcerr`) meaning that any output sent to these stream objects is immediately flushed to the OS (via `std::basic_ostream::sentry`'s destructor).
In addition, `std::cerr.tie()` returns `&std::cout` (same for `std::wcerr` and `std::wcout`), meaning that any output operation on `std::cerr` first executes `std::cout.flush()` (via `std::basic_ostream::sentry`'s constructor).

## Notes

The 'c' in the name refers to "character" ([https://www.stroustrup.com/bs_faq2.html#cout stroustrup.com FAQ]); `cerr` means "character error (stream)" and `wcerr` means "wide character error (stream)".

## Example


### Example

```cpp
#include <chrono>
#include <iostream>
#include <thread>
using namespace std::chrono_literals;

void f()
{
    std::cout << "Output from thread...";
    std::this_thread::sleep_for(2s);
    std::cout << "...thread calls flush()" << std::endl;
}

int main()
{
    std::jthread t1{f};
    std::this_thread::sleep_for(1000ms);
    std::clog << "This output from main is not tie()'d to cout\n";
    std::cerr << "This output is tie()'d to cout\n";
}
```


**Output:**
```
This output from main is not tie()'d to cout
Output from thread...This output is tie()'d to cout
...thread calls flush()
```


## Defect reports


## See also


| cpp/io/ios_base/dsc Init | (see dedicated page) |
| cpp/io/dsc clog | (see dedicated page) |
| cpp/io/dsc cout | (see dedicated page) |
| cpp/io/c/dsc std streams | (see dedicated page) |


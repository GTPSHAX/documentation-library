---
title: std::wcout
type: Input/output
source: https://en.cppreference.com/w/cpp/io/cout
---


```cpp
**Header:** `<`iostream`>`
dcl|num=1|1=
extern std::ostream cout;
dcl|num=2|1=
extern std::wostream wcout;
```

The global objects `std::cout` and `std::wcout` control output to a stream buffer of implementation-defined type (derived from `std::streambuf`), associated with the standard C output stream `stdout`.
These objects are guaranteed to be initialized during or before the first time an object of type `std::ios_base::Init` is constructed and are available for use in the constructors and destructors of static objects with ordered initialization (as long as  is included before the object is defined).
Unless `std::ios_base::sync_with_stdio(false)` has been issued, it is safe to concurrently access these objects from multiple threads for both formatted and unformatted output.
By specification of `std::cin`, `std::cin.tie()` returns `&std::cout`. This means that any input operation on `std::cin` executes `std::cout.flush()` (via `std::basic_istream::sentry`'s constructor). Similarly, `std::wcin.tie()` returns `&std::wcout`.
By specification of `std::cerr`, `std::cerr.tie()` returns `&std::cout`. This means that any output operation on `std::cerr` executes `std::cout.flush()` (via `std::basic_ostream::sentry`'s constructor). Similarly, `std::wcerr.tie()` returns `&std::wcout`. <sup>(C++11)</sup>

## Notes

The 'c' in the name refers to "character" ([https://www.stroustrup.com/bs_faq2.html#cout stroustrup.com FAQ]); `cout` means "character output" and `wcout` means "wide character output".
Because dynamic initialization of templated variables are unordered, it is not guaranteed that `std::cout` has been initialized to a usable state before the initialization of such variables begins, unless an object of type `std::ios_base::Init` has been constructed.

## Example


### Example

```cpp
#include <iostream>

struct Foo
{
    int n;
    Foo()
    {
        std::cout << "static constructor\n";
    }
    ~Foo()
    {
        std::cout << "static destructor\n";
    }
};

Foo f; // static object

int main()
{
    std::cout << "main function\n";
}
```


**Output:**
```
static constructor
main function
static destructor
```


## See also


| cpp/io/ios_base/dsc Init | (see dedicated page) |
| cpp/io/dsc cerr | (see dedicated page) |
| cpp/io/dsc clog | (see dedicated page) |
| cpp/io/c/dsc std streams | (see dedicated page) |


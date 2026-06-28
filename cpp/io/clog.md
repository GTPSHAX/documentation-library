---
title: std::wclog
type: Input/output
source: https://en.cppreference.com/w/cpp/io/clog
---


```cpp
**Header:** `<`iostream`>`
dcl|num=1|
extern std::ostream clog;
dcl|num=2|
extern std::wostream wclog;
```

The global objects `std::clog` and `std::wclog` control output to a stream buffer of implementation-defined type (derived from `std::streambuf`), associated with the standard C output stream `stderr`, but, unlike `std::cerr`/`std::wcerr`, these streams are not automatically flushed and cout is not automatically tie()'d with these streams.
These objects are guaranteed to be initialized during or before the first time an object of type `std::ios_base::Init` is constructed and are available for use in the constructors and destructors of static objects with ordered initialization (as long as  is included before the object is defined).
Unless `sync_with_stdio(false)` has been issued, it is safe to concurrently access these objects from multiple threads for both formatted and unformatted output.

## Notes

The “c” in the name refers to “character” ([https://www.stroustrup.com/bs_faq2.html#cout stroustrup.com FAQ]); `clog` means “character log” and `wclog` means “wide character log”.

## Example


### Example

```cpp
#include <iostream>

struct Foo
{
    int n;
    Foo()
    {
        std::clog << "constructor\n";
    }
    ~Foo()
    {
        std::clog << "destructor\n";
    }
};

Foo f; // static object

int main()
{
    std::clog << "main function\n";
}
```


**Output:**
```
constructor
main function
destructor
```


## See also


| cpp/io/ios_base/dsc Init | (see dedicated page) |
| cpp/io/dsc cerr | (see dedicated page) |
| cpp/io/dsc cout | (see dedicated page) |
| cpp/io/c/dsc std streams | (see dedicated page) |


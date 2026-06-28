---
title: std::wcin
type: Input/output
source: https://en.cppreference.com/w/cpp/io/cin
---


```cpp
**Header:** `<`iostream`>`
dcl|num=1|
extern std::istream cin;
dcl|num=2|
extern std::wistream wcin;
```

The global objects `std::cin` and `std::wcin` control input from a stream buffer of implementation-defined type (derived from `std::streambuf`), associated with the standard C input stream `stdin`.
These objects are guaranteed to be initialized during or before the first time an object of type `std::ios_base::Init` is constructed and are available for use in the constructors and destructors of static objects with ordered initialization (as long as  is included before the object is defined).
Unless `sync_with_stdio(false)` has been issued, it is safe to concurrently access these objects from multiple threads for both formatted and unformatted input.
Once initialized:
1.  returns `&std::cout`. This means that any input operation on `std::cin` forces a call to  if any characters are pending for output..
2. `std::wcin.tie()` returns `&std::wcout`. This means that any input operation on `std::wcin` forces a call to `std::wcout.flush()` if any characters are pending for output.

## Notes

The “c” in the name refers to “character” ([https://www.stroustrup.com/bs_faq2.html#cout stroustrup.com FAQ]); `cin` means “character input” and `wcin` means “wide character input”.

## Example


### Example

```cpp
#include <iostream>

struct Foo
{
    int n;
    Foo()
    {
        std::cout << "Enter n: "; // no flush needed
        std::cin >> n;
    }
};

Foo f; // static object

int main()
{
    std::cout << "f.n is " << f.n << '\n';
}
```


**Output:**
```
Enter n: 10
f.n is 10
```


## See also


| cpp/io/ios_base/dsc Init | (see dedicated page) |
| cpp/io/dsc cout | (see dedicated page) |
| cpp/io/c/dsc std streams | (see dedicated page) |


---
title: std::strstreambuf::freeze
type: Input/output
source: https://en.cppreference.com/w/cpp/io/strstreambuf/freeze
---

ddcl|deprecated=c++98|removed=c++26|1=
void freeze( bool freezefl = true );
If the buffer uses dynamic allocation, sets the frozen status of the stream to `freezefl`.
While the stream is frozen, `overflow()` will not reallocate the buffer and the `destructor` will not deallocate the buffer (thereby causing a memory leak).

## Parameters


### Parameters

- `freezefl` - new value to set the freeze status to

## Return value

(none)

## Notes

Every call to `str()` freezes the stream to preserve the validity of the pointer it returns. To allow the destructor to deallocate the buffer, `freeze(false)` needs to be called explicitly.

## Example


### Example

```cpp
#include <iostream>
#include <strstream>

int main()
{
    {
        std::strstream dyn; // dynamically-allocated read/write buffer
        dyn << "Test: " << 1.23; // note: no std::ends to demonstrate append behavior
        std::cout << "dynamic buffer holds " << dyn.pcount() << " characters: '";
        std::cout.write(dyn.str(), dyn.pcount()) << "'\n";
        // the buffer is now frozen, further output will not make the buffer grow
        dyn << "more output, hopefully enough to run out of the allocated space"
            << std::ends;
        std::cout << "After more output, it holds "
                  << dyn.pcount() << " characters: '" << dyn.str() << "'\n";
        dyn.freeze(false); // unfreeze before destructor
    } // memory freed by the destructor

    {
        char arr[20];
        std::ostrstream st(arr, sizeof arr); // fixed-size buffer
        st << 1.23; // note: no std::ends to demonstrate append behavior
        std::cout << "static buffer holds "
                  << st.pcount() << " characters: '";
        std::cout.write(st.str(), st.pcount());
        std::cout << "'\n";
        st << "more output, hopefully enough to run out of the allocated space"
           << std::ends;
        std::cout << "static buffer holds "
                  << st.pcount() << " characters: '";
        std::cout.write(st.str(), st.pcount());
        std::cout << "'\n";
    } // nothing to deallocate, no need to unfreeze,
}
```


**Output:**
```
dynamic buffer holds 10 characters: 'Test: 1.23'
After more output, it holds 16 characters: 'Test: 1.23more o'
static buffer holds 4 characters: '1.23'
static buffer holds 20 characters: '1.23more output, hop'
```


## See also


| cpp/io/strstream/dsc freeze|strstream | (see dedicated page) |
| cpp/io/strstream/dsc freeze|ostrstream | (see dedicated page) |
| cpp/io/strstreambuf/dsc ~strstreambuf | (see dedicated page) |
| cpp/io/strstreambuf/dsc overflow | (see dedicated page) |


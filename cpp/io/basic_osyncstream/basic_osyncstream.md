---
title: std::basic_osyncstream::basic_osyncstream
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_osyncstream/basic_osyncstream
---


```cpp
dcl|num=1|1=
basic_osyncstream( streambuf_type* buf, const Allocator& a );
dcl|num=2|1=
explicit basic_osyncstream( streambuf_type* buf );
dcl|num=3|1=
basic_osyncstream( std::basic_ostream<CharT, Traits>& os, const Allocator& a );
dcl|num=4|1=
explicit basic_osyncstream( std::basic_ostream<CharT, Traits>& os );
dcl|num=5|1=
basic_osyncstream( std::basic_osyncstream&& other ) noexcept;
```

Constructs new synchronized output stream.
@1-4@ Constructs the private member `std::basic_syncbuf` using the buffer and the allocator provided, and initializes the base class with a pointer to the member `std::basic_streambuf`.
5. Move constructor. Move-constructs the `std::basic_ostream` base and the std::basic_syncbuf member from the corresponding subobjects of `other`, then calls `cpp/io/basic_ios/set_rdbuf|set_rdbuf` with the pointer to the newly-constructed underlying `std::basic_syncbuf` to complete the initialization of the base. After this move constructor, `other.get_wrapped()` returns `nullptr` and destruction of `other` produces no output.

## Parameters


### Parameters

- `buf` - pointer to the `std::basic_streambuf` that will be wrapped
- `os` - reference to a `std::basic_ostream`, whose rdbuf() will be wrapped
- `a` - the allocator to pass to the constructor of the member `std::basic_syncbuf`
- `other` - another osyncstream to move from

## Example


### Example

```cpp
#include <iostream>
#include <string_view>
#include <syncstream>
#include <thread>

void worker(const int id, std::ostream &os)
{
    std::string_view block;
    switch (id)
    {
        default: [[fallthrough]];
        case 0: block = "██";
                break;
        case 1: block = "▓▓";
                break;
        case 2: block = "▒▒";
                break;
        case 3: block = "░░";
                break;
    }
    for (int i = 1; i <= 50; ++i)
        os << block << std::flush;
    os << std::endl;
}

int main()
{
    std::cout << "Synchronized output should not cause any interference:" << std::endl;
    {
        auto scout1 = std::osyncstream{std::cout};
        auto scout2 = std::osyncstream{std::cout};
        auto scout3 = std::osyncstream{std::cout};
        auto scout4 = std::osyncstream{std::cout};
        auto w1 = std::jthread{worker, 0, std::ref(scout1)};
        auto w2 = std::jthread{worker, 1, std::ref(scout2)};
        auto w3 = std::jthread{worker, 2, std::ref(scout3)};
        auto w4 = std::jthread{worker, 3, std::ref(scout4)};
    }

    std::cout << "\nLack of synchronization may cause some interference on output:"
              << std::endl;
    {
        auto w1 = std::jthread{worker, 0, std::ref(std::cout)};
        auto w2 = std::jthread{worker, 1, std::ref(std::cout)};
        auto w3 = std::jthread{worker, 2, std::ref(std::cout)};
        auto w4 = std::jthread{worker, 3, std::ref(std::cout)};
    }
}
```


**Output:**
```
Synchronized output should not cause any interference:
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
████████████████████████████████████████████████████████████████████████████████████████████████████

Lack of synchronization may cause some interference on output:
████▓▓██▒▒▒▒▓▓██░░▒▒██░░▒▒░░░░▒▒░░▓▓▒▒██░░████████████▓▓██████▓▓▒▒▓▓██░░████▓▓▓▓██▒▒░░░░░░░░▓▓░░▓▓██▒▒▒▒▒▒▒▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▓▓
▒▒▒▒██░░██████████████████████████░░░░░░░░░░░░░░██░░▒▒░░░░░░██████████████████
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒
░░░░░░
```


## See also


| cpp/io/basic_syncbuf/dsc constructor | (see dedicated page) |


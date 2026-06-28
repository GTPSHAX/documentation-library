---
title: std::basic_ios::copyfmt
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios/copyfmt
---

ddcl|
basic_ios& copyfmt( const basic_ios& other );
If `other` refers to the same object as `*this`, has no effects. Otherwise, copies the state of the stream `other` into `*this`. This is done in the following sequence:
1. Calls every callback registered by `register_callback()` passing `cpp/io/ios_base/event|erase_event` as parameter.
2. Copies all member objects from `other` to `*this` except for `rdstate()`, the exception mask, and `rdbuf()`. In particular, makes copies of the locale, the formatting flags, the contents of the arrays `std::ios_base::iword` and `std::ios_base::pword` (but not the `iword` and `pword` pointers themselves), the callbacks, and the tied stream.
3. Calls every callback registered by `register_callback()` passing `cpp/io/ios_base/event|copyfmt_event` as parameter.
4. Copies the exception mask from `other` to `*this` as if by calling `exceptions(other.exceptions())`.

## Parameters


### Parameters

- `other` - another stream to use as source

## Return value

`*this`

## Notes

The second pass through the callbacks may be used to deep-copy the user-defined objects pointed to by the pointers in `std::ios_base::pword`.
`copyfmt()` may be used to save and restore the state of a stream. Boost provides a more fine-grained [https://www.boost.org/doc/libs/release/libs/io/doc/ios_state.html I/O state savers] library for the same purpose.

## Example


### Example

```cpp
#include <bitset>
#include <climits>
#include <fstream>
#include <iostream>

int main()
{
    std::ofstream out;

    out.copyfmt(std::cout); // copy everything except rdstate and rdbuf
    out.clear(std::cout.rdstate()); // copy rdstate
    out.basic_ios<char>::rdbuf(std::cout.rdbuf()); // share the buffer

    out << "Hello, world\n";

    auto bin = [](std::ios_base::fmtflags f)
    {
        return std::bitset<sizeof(std::ios_base::fmtflags) * CHAR_BIT>
            { static_cast<unsigned long long>(f) };
    };
    std::ofstream out2;
    std::cout << "1) out2.flags(): " << bin(out2.flags()) << '\n';
    std::cout << "2) cout.flags(): " << bin(std::cout.flags()) << '\n';
    std::cout.setf(std::ios::hex {{!
```

std::cout << "3) cout.flags(): " << bin(std::cout.flags()) << '\n';
out2.copyfmt(std::cout); // copy everything except rdstate and rdbuf
std::cout << "4) out2.flags(): " << bin(out2.flags()) << '\n';
}
|p=true
|output=
Hello, world
1) out2.flags(): 00000000000000000001000000000010
2) cout.flags(): 00000000000000000001000000000010
3) cout.flags(): 00000000000000000001000000001111
4) out2.flags(): 00000000000000000001000000001111

## Defect reports


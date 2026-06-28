---
title: std::ios_base::fmtflags
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ios_base/fmtflags
---


```cpp
dcl|
typedef /*implementation defined*/ fmtflags;
dcl|1=
static constexpr fmtflags dec = /*implementation defined*/
static constexpr fmtflags oct = /*implementation defined*/
static constexpr fmtflags hex = /*implementation defined*/
static constexpr fmtflags basefield = dec | oct | hex;
dcl|1=
static constexpr fmtflags left = /*implementation defined*/
static constexpr fmtflags right = /*implementation defined*/
static constexpr fmtflags internal = /*implementation defined*/
static constexpr fmtflags adjustfield = left | right | internal;
dcl|1=
static constexpr fmtflags scientific = /*implementation defined*/
static constexpr fmtflags fixed = /*implementation defined*/
static constexpr fmtflags floatfield = scientific | fixed;
dcl|1=
static constexpr fmtflags boolalpha = /*implementation defined*/
static constexpr fmtflags showbase = /*implementation defined*/
static constexpr fmtflags showpoint = /*implementation defined*/
static constexpr fmtflags showpos = /*implementation defined*/
static constexpr fmtflags skipws = /*implementation defined*/
static constexpr fmtflags unitbuf = /*implementation defined*/
static constexpr fmtflags uppercase = /*implementation defined*/
```

Specifies available formatting flags. It is a *BitmaskType*. The following constants are defined:

## Example


### Example

```cpp
#include <iostream>

int main()
{
    const int num = 150;

    // using fmtflags as class member constants:
    std::cout.setf(std::ios_base::hex, std::ios_base::basefield);
    std::cout.setf(std::ios_base::showbase);
    std::cout << num << '\n';

    // using fmtflags as inherited class member constants:
    std::cout.setf (std::ios::hex, std::ios::basefield);
    std::cout.setf (std::ios::showbase);
    std::cout << num << '\n';

    // using fmtflags as object member constants:
    std::cout.setf(std::cout.hex, std::cout.basefield);
    std::cout.setf(std::cout.showbase);
    std::cout << num << '\n';

    // using fmtflags as a type:
    std::ios_base::fmtflags ff;
    ff = std::cout.flags();
    ff &= ~std::cout.basefield;   // unset basefield bits
    ff {{!
```

ff |= std::cout.showbase;     // set showbase
std::cout.flags(ff);
std::cout << num << '\n';
// not using fmtflags, but using manipulators:
std::cout << std::hex << std::showbase << num << '\n';
}
|output=
0x96
0x96
0x96
0x96
0x96

## See also


| cpp/io/ios_base/dsc flags | (see dedicated page) |
| cpp/io/ios_base/dsc setf | (see dedicated page) |
| cpp/io/ios_base/dsc unsetf | (see dedicated page) |
| cpp/io/manip/dsc setbase | (see dedicated page) |
| cpp/io/manip/dsc setfill | (see dedicated page) |
| cpp/io/manip/dsc fixed | (see dedicated page) |
| cpp/io/manip/dsc showbase | (see dedicated page) |
| cpp/io/manip/dsc boolalpha | (see dedicated page) |
| cpp/io/manip/dsc showpos | (see dedicated page) |
| cpp/io/manip/dsc showpoint | (see dedicated page) |
| cpp/io/manip/dsc unitbuf | (see dedicated page) |
| cpp/io/manip/dsc skipws | (see dedicated page) |
| cpp/io/manip/dsc uppercase | (see dedicated page) |


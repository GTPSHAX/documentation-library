---
title: std::unreachable
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/unreachable
---

ddcl|header=utility|since=c++23|
noreturn void unreachable();
Invokes undefined behavior at a given point.
An implementation may use this to optimize impossible code branches away (typically, in optimized builds) or to trap them to prevent further execution (typically, in debug builds).

## Notes


## Possible implementation

eq fun
|1=
noreturn inline void unreachable()
{
// Uses compiler specific extensions if possible.
// Even if no extension is used, undefined behavior is still raised by
// an empty function body and the noreturn attribute.
#if defined(_MSC_VER) && !defined(__clang__) // MSVC
__assume(false);
#else // GCC, Clang
__builtin_unreachable();
#endif
}

## Example


### Example

```cpp
#include <cassert>
#include <cstddef>
#include <cstdint>
#include <utility>
#include <vector>

struct Color { std::uint8_t r, g, b, a; };

// Assume that only restricted set of texture caps is supported.
void generate_texture(std::vector<Color>& tex, std::size_t xy)
{
    switch (xy)
    {
    case 128: [[fallthrough]];
    case 256: [[fallthrough]];
    case 512: /* ... */
        tex.clear();
        tex.resize(xy * xy, Color{0, 0, 0, 0});
        break;
    default:
        std::unreachable();
    }
}

int main()
{
    std::vector<Color> tex;
    generate_texture(tex, 128); // OK
    assert(tex.size() == 128 * 128);
    generate_texture(tex, 32);  // Results in undefined behavior
}
```


**Output:**
```
Segmentation fault
```


## See also


| cpp/language/attributes/dsc assume | (see dedicated page) |
| cpp/memory/dsc assume_aligned | (see dedicated page) |


## External Links


---
title: std::source_location::current
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/source_location/current
---


```cpp
dcl|since=c++20|
static consteval source_location current() noexcept;
```

Constructs a new `source_location` object corresponding to the location of the call site.

## Return value

If `current()` is invoked directly (via a function call that names `current()`),  it returns a `source_location` object with implementation-defined values representing the location of the call. The values should be affected by the `#line` preprocessor directive in the same manner as the predefined macros `__LINE__` and `__FILE__`.
If `current()` is used in a default member initializer, the return value corresponds to the location of the constructor definition or aggregate initialization that initializes the data member.
If `current()` is used in a default argument, the return value corresponds to the location of the call to `current()` at the call site.
If `current()` is invoked in any other manner, the return value is unspecified.

## Notes

`std::source_location::current` typically requires compiler's built-in implementation.

## Example


### Example

```cpp
#include <print>
#include <source_location>

struct src_rec
{
    std::source_location srcl = std::source_location::current();
    int dummy{};

    src_rec(std::source_location loc = std::source_location::current()) :
        srcl(loc)    // values of member refer to the location of the calling function
    {}
    src_rec(int i) : // values of member refer to this location
        dummy(i)
    {}
    src_rec(double)  // values of member refer to this location
    {}
};

std::source_location src_clone(std::source_location a = std::source_location::current())
{
    return a;
}

std::source_location src_make()
{
    return std::source_location::current();
}

int main()
{
    const auto r0 = src_rec();
    const auto r1 = src_rec(0);
    const auto r2 = src_rec(0.0);
    const auto s0 = std::source_location::current();
    const auto s1 = src_clone(s0);
    const auto s2 = src_clone();
    const auto s3 = src_make();

    std::println("#{1} {0} {2}", "r0", r0.srcl.line(), r0.srcl.function_name());
    std::println("#{1} {0} {2}", "r1", r1.srcl.line(), r1.srcl.function_name());
    std::println("#{1} {0} {2}", "r2", r2.srcl.line(), r2.srcl.function_name());
    std::println("#{1} {0} {2}", "s0", s0.line(), s0.function_name());
    std::println("#{1} {0} {2}", "s1", s1.line(), s1.function_name());
    std::println("#{1} {0} {2}", "s2", s2.line(), s2.function_name());
    std::println("#{1} {0} {2}", "s3", s3.line(), s3.function_name());
}
```


**Output:**
```
#31 r0 int main()
#13 r1 src_rec::src_rec(int)
#16 r2 src_rec::src_rec(double)
#34 s0 int main()
#34 s1 int main()
#36 s2 int main()
#26 s3 std::source_location src_make()
```


## See also


| cpp/utility/source_location/dsc constructor | (see dedicated page) |
| cpp/utility/basic_stacktrace/dsc current | (see dedicated page) |


---
title: assert
type: Diagnostics
source: https://en.cppreference.com/w/cpp/error/assert
---


# assert


```cpp
**Header:** `<`cassert`>`
dcl rev multi|num=1|until1=c++26|dcl1=
#define assert(condition) ((void)0)
|dcl2=
#define assert(...)       ((void)0)
dcl rev multi|num=2|until1=c++26|dcl1=
#define assert(condition) /* unspecified */
|dcl2=
#define assert(...)       /* unspecified */
```

The definition of the macro `assert` depends on another macro, `NDEBUG`, which is not defined by the standard library.
1. If `NDEBUG` is defined as a macro name at the point in the source code where  or `cpp/header/cassert|<assert.h>` is included, the assertion is disabled: `assert` does nothing.
2. Otherwise, the assertion is enabled:
rev|until=c++26|
`assert` checks if its argument (which must have scalar type):
* If the argument compares unequal to zero, there are no further effects.
* Otherwise, `assert` creates a diagnostic on the standard error stream and calls `std::abort()`.
rev|since=c++26|
`assert` puts a diagnostic test into programs and expands to an expression of type `void`. `__VA_ARGS__` is evaluated and contextually converted to `bool`:
* If the evaluation yields `true`, there are no further effects.
* Otherwise, `assert` creates a diagnostic on the standard error stream and calls `std::abort()`.
The diagnostic information has an implementation-defined format, but it always includes the following information:
rev|until=c++26|
* the text of `condition`
rev|since=c++26|
* `#__VA_ARGS__`
* the source file name (i.e., )
* the source line number (i.e., )
* the name of the enclosing function (i.e., )
rrev|since=c++11|
The expression `assert(E)` is guaranteed to be a , if either
* `NDEBUG` is defined at the point where `assert` is last defined or redefined, or
* `E`, contextually converted to `bool`, is a constant subexpression that evaluates to `true`.

## Parameters


### Parameters

- `condition` - expression of scalar type

## Notes

rrev|until=c++26|
Because `assert` is a function-like macro, commas anywhere in the argument that are not protected by parentheses are interpreted as macro argument separators. Such commas are often found in template argument lists and list-initialization:

```cpp
assert(std::is_same_v<int, int>);        // error: assert does not take two arguments
assert((std::is_same_v<int, int>));      // OK: one argument
static_assert(std::is_same_v<int, int>); // OK: not a macro

std::complex<double> c;
assert(c == std::complex<double>{0, 0});   // error
assert((c == std::complex<double>{0, 0})); // OK
```

There is no standardized interface to add an additional message to `assert` errors. A portable way to include one is to use a comma operator provided it has not been overloaded, or use `&&` with a string literal:

```cpp
assert(("There are five lights", 2 + 2 == 5));
assert(2 + 2 == 5 && "There are five lights");
```

The implementation of `assert` in [https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/assert-macro-assert-wassert Microsoft CRT] does not conform to C++11 and later revisions, because its underlying function (`_wassert`) takes neither `__func__` nor an equivalent replacement.
Since C++20, the values needed for the diagnostic message can also be obtained from .
Even though the change of `assert` in C23/C++26 is not formally a defect report, the C committee [https://www.open-std.org/jtc1/sc22/wg14/www/previous.html recommends] implementations to backport the change to old modes.

## Example


### Example

```cpp
#include <iostream>
// uncomment to disable assert()
// #define NDEBUG
#include <cassert>

// Use (void) to silence unused warnings.
#define assertm(exp, msg) assert((void(msg), exp))

int main()
{
    assert(2 + 2 == 4);
    std::cout << "Checkpoint #1\n";

    assert((void("void helps to avoid 'unused value' warning"), 2 * 2 == 4));
    std::cout << "Checkpoint #2\n";

    assert((010 + 010 == 16) && "Yet another way to add an assert message");
    std::cout << "Checkpoint #3\n";

    assertm((2 + 2) % 3 == 1, "Success");
    std::cout << "Checkpoint #4\n";

    assertm(2 + 2 == 5, "Failed"); // assertion fails
    std::cout << "Execution continues past the last assert\n"; // No output
}
```


**Output:**
```
Checkpoint #1
Checkpoint #2
Checkpoint #3
Checkpoint #4
main.cpp:23: int main(): Assertion `((void)"Failed", 2 + 2 == 5)' failed.
Aborted
```


## Defect reports


## See also


| cpp/language/dsc contract_assert | (see dedicated page) |
| cpp/language/dsc static_assert | (see dedicated page) |
| cpp/utility/program/dsc abort | (see dedicated page) |


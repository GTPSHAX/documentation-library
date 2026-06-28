---
title: attribute: noreturn
type: Language
source: https://en.cppreference.com/w/cpp/language/attributes/noreturn
---

Indicates that the function does not return.

## Syntax


**Syntax:**

- `sdsc|`
- `**``noreturn``**`

## Explanation

Indicates that the function will not return control flow to the calling function after it finishes (e.g. functions that terminate the application, throw exceptions, loop indefinitely, etc.). This attribute applies to the name of the function being declared in function declarations only.
If a function previously declared with `noreturn` is invoked and that invocation eventually returns, the behavior is runtime-undefined.
The first declaration of the function must specify this attribute if any declaration specifies it. If a function is declared with `noreturn` in one translation unit, and the same function is declared without `noreturn` in another translation unit, the program is ill-formed; no diagnostic required.

## Example


### Example

```cpp
[[noreturn]] void f()
{
    throw "error";
    // OK
}

void q [[noreturn]] (int i)
{
    // behavior is undefined if called with an argument <= 0
    if (i > 0)
        throw "positive";
}

// void h() [[noreturn]]; // error: attribute applied to function type of h, not h itself

int main()
{
    try { f(); } catch(...) {}
    try { q(42); } catch(...) {}
}
```


## Standard library

The following standard functions are declared with `noreturn` attribute:


#### Terminating functions

| cpp/utility/program/dsc _Exit | (see dedicated page) |
| cpp/utility/program/dsc abort | (see dedicated page) |
| cpp/utility/program/dsc exit | (see dedicated page) |
| cpp/utility/program/dsc quick_exit | (see dedicated page) |
| cpp/error/dsc terminate | (see dedicated page) |
| cpp/error/dsc unexpected | (see dedicated page) |

#### Compiler hints

| cpp/utility/dsc unreachable | (see dedicated page) |

#### Always-throwing functions

| cpp/error/dsc rethrow_exception | (see dedicated page) |
| cpp/error/dsc throw_with_nested | (see dedicated page) |

#### Non-local jumps {{mark since c++17

| cpp/utility/program/dsc longjmp | (see dedicated page) |


## Defect reports


## References


## See also


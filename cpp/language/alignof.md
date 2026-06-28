---
title: alignof operator
type: Language
source: https://en.cppreference.com/w/cpp/language/alignof
---


# tt|alignof

Queries alignment requirements of a type.

## Syntax


**Syntax:**

- `*type-id* **`)`**`
Returns a value of type `std::size_t`.

## Explanation

Returns `the alignment`, in bytes, required for any instance of the type indicated by `type-id`, which is either `complete` object type, an array type whose element type is complete, or a reference type to one of those types.
If the type is reference type, the operator returns the alignment of referenced type; if the type is array type, alignment requirement of the element type is returned.

## Notes

See `alignment` for the meaning and properties of the value returned by `alignof`.

## Keywords

`cpp/keyword/alignof`

## Example


### Example

```cpp
#include <iostream>

struct Foo
{
    int   i;
    float f;
    char  c;
};

// Note: alignas(alignof(long double)) below can be
// simplified to alignas(long double) if desired.
struct alignas(alignof(long double)) Foo2
{
    // put your definition here
}; 

struct Empty {};

struct alignas(64) Empty64 {};

#define SHOW(expr) std::cout << #expr << " = " << (expr) << '\n'

int main()
{
    SHOW(alignof(char));
    SHOW(alignof(int*));
    SHOW(alignof(Foo));
    SHOW(alignof(Foo2));
    SHOW(alignof(Empty));
    SHOW(alignof(Empty64));
}
```


**Output:**
```
alignof(char) = 1
alignof(int*) = 8
alignof(Foo) = 4
alignof(Foo2) = 16
alignof(Empty) = 1
alignof(Empty64) = 64
```


## Defect reports


## References


## See also


| cpp/language/dsc alignas | (see dedicated page) |
| cpp/types/dsc alignment_of | (see dedicated page) |


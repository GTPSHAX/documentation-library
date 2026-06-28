---
title: attribute: no_unique_address
type: Language
source: https://en.cppreference.com/w/cpp/language/attributes/no_unique_address
---

Allows this data member to be overlapped with other non-static data members or base class subobjects of its class.

## Syntax


**Syntax:**

- `sdsc|`
- `**``no_unique_address``**`

## Explanation

Applies to the name being declared in the declaration of a non-static data member that is not a bit-field.
Makes this member subobject potentially-overlapping, i.e., allows this member to be overlapped with other non-static data members or base class subobjects of its class. This means that if the member has an empty class type (e.g. stateless allocator), the compiler may optimize it to occupy no space, just like if it were an empty base. If the member is not empty, any tail padding in it may be also reused to store other data members.

## Notes

`no_unique_address` is ignored by MSVC even in C++20 mode; instead, `msvc::no_unique_address` is provided.

## Example


### Example

```cpp
#include <boost/type_index.hpp>
#include <iostream>

struct Empty {}; // The size of any object of empty class type is at least 1
static_assert(sizeof(Empty) >= 1);

struct X
{
    int i;
    Empty e; // At least one more byte is needed to give ‘e’ a unique address
};
static_assert(sizeof(X) >= sizeof(int) + 1);

struct Y
{
    int i;
    [[no_unique_address]] Empty e; // Empty member optimized out
};
static_assert(sizeof(Y) >= sizeof(int));

struct Z
{
    char c;
    // e1 and e2 cannot share the same address because they have the
    // same type, even though they are marked with [[no_unique_address]].
    // However, either may share address with ‘c’.
    [[no_unique_address]] Empty e1, e2;
};
static_assert(sizeof(Z) >= 2);

struct W
{
    char c[2];
    // e1 and e2 cannot have the same address, but one of
    // them can share with c[0] and the other with c[1]:
    [[no_unique_address]] Empty e1, e2;
};
static_assert(sizeof(W) >= 2);

template <typename T>
void print_size_of()
{
    using boost::typeindex::type_id;
    std::cout << "sizeof(" << type_id<T>() << ") == " << sizeof(T) << '\n';
}

int main()
{
    print_size_of<Empty>();
    print_size_of<int>();
    print_size_of<X>();
    print_size_of<Y>();
    print_size_of<Z>();
    print_size_of<W>();
}
```


**Output:**
```
sizeof(Empty) == 1
sizeof(int) == 4
sizeof(X) == 8
sizeof(Y) == 4
sizeof(Z) == 2
sizeof(W) == 3
```


## References


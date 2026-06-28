---
title: std::is_empty
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_empty
---

cpp/types/traits/is|1=is_empty
|description=If `T` is an empty type (that is, a non-union class type with no non-static data members other than bit-fields of size 0, no virtual functions, no virtual base classes, and no non-empty base classes), provides the member constant `value` equal to `true`. For any other type, `value` is `false`.
If `T` is an incomplete non-union class type, the behavior is undefined.
|inherit_desc= `T` is an empty class type

## Notes

Inheriting from empty base classes usually does not increase the size of a class due to empty base optimization.
`std::is_empty<T>` and all other type traits are empty classes.

## Example


### Example

```cpp
#include <iostream>
#include <type_traits>

struct A {};
static_assert(std::is_empty_v<A> == true);

struct B { int m; };
static_assert(std::is_empty_v<B> == false);

struct C { static int m; };
static_assert(std::is_empty_v<C> == true);

struct D { virtual ~D(); };
static_assert(std::is_empty_v<D> == false);

union E {};
static_assert(std::is_empty_v<E> == false);

struct F { [[no_unique_address]] E e; };

struct G
{
    int:0;
    // C++ standard allow "as a special case, an unnamed bit-field with a width of zero
    // specifies alignment of the next bit-field at an allocation unit boundary.
    // Only when declaring an unnamed bit-field may the width be zero."
};
static_assert(std::is_empty_v<G>); // holds only unnamed bit-fields of zero width

int main()
{
    std::cout << std::boolalpha;
    std::cout << "F: " << std::is_empty_v<F> << '\n'; // the result is ABI-dependent
}
```


**Output:**
```
F: true
```


## Defect reports


## See also


| cpp/types/dsc is_class | (see dedicated page) |


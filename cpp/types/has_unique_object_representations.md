---
title: std::has_unique_object_representations
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/has_unique_object_representations
---

cpp/types/traits/is|1=has_unique_object_representations
|std=c++17
|description=If `T` is trivially copyable and if any two objects of type `T` with the same value have the same object representation, provides the member constant `value` equal `true`. For any other type, `value` is `false`.
For the purpose of this trait, two arrays have the same value if their elements have the same values, two non-union classes have the same value if their direct subobjects have the same value, and two unions have the same value if they have the same active member and the value of that member is the same.
It is implementation-defined which scalar types satisfy this trait, but<sup>(until C++20)</sup>  unsigned integer types that do not use padding bits are guaranteed to have unique object representations.
If `std::remove_all_extents_t<T>` is an incomplete type other than (possibly cv-qualified) `void`, the behavior is undefined.
|inherit_desc=`T` has unique object representations

## Notes

This trait was introduced to make it possible to determine whether a type can be correctly hashed by hashing its object representation as a byte array.

## Example


### Example

```cpp
#include <cstdint>
#include <type_traits>

struct unpadded
{
    std::uint32_t a, b;
};

struct likely_padded
{
    std::uint8_t c;
    std::uint16_t st;
    std::uint32_t i;
};

int main()
{
    // Every value of a char corresponds to exactly one object representation.
    static_assert(std::has_unique_object_representations_v<char>);
    // For IEC 559 floats, assertion passes because the value NaN has
    // multiple object representations.
    static_assert(!std::has_unique_object_representations_v<float>);

    // Should succeed in any sane implementation because unpadded
    // is typically not padded, and std::uint32_t cannot contain padding bits.
    static_assert(std::has_unique_object_representations_v<unpadded>);
    // Fails in most implementations because padding bits are inserted
    // between the data members c and st for the purpose of aligning st to 16 bits.
    static_assert(!std::has_unique_object_representations_v<likely_padded>);

    // Notable architectural divergence:
    static_assert(std::has_unique_object_representations_v<bool>);  // x86
 // static_assert(!std::has_unique_object_representations_v<bool>); // ARM
}
```


## Defect reports


## See also


| cpp/types/dsc is_standard_layout | (see dedicated page) |
| cpp/utility/dsc hash | (see dedicated page) |


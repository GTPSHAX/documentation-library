---
title: Empty base optimization
type: Language
source: https://en.cppreference.com/w/cpp/language/ebo
---


# Empty base optimization

Allows the size of an empty base subobject to be zero.

## Explanation

The size of any `object` or member subobject is required to be at least 1 even if the type is an empty `class type` (that is, a class or struct that has no non-static data members), <sup>(since C++20)</sup> (unless with  in order to be able to guarantee that the addresses of distinct objects of the same type are always distinct.
However, base class subobjects are not so constrained, and can be completely optimized out from the object layout:
Empty base optimization is prohibited if one of the empty base classes is also the type or the base of the type of the first non-static data member, since the two base subobjects of the same type are required to have different addresses within the object representation of the most derived type.
A typical example of such situation is the naive implementation of `std::reverse_iterator` (derived from the empty base `std::iterator`), which holds the underlying iterator (also derived from `std::iterator`) as its first non-static data member.
rev|since=c++11|
Empty base optimization is ''required'' for *StandardLayoutType*s in order to maintain the requirement that the pointer to a standard-layout object, converted using `reinterpret_cast`, points to its initial member, which is why the requirements for a standard layout type include "has all non-static data members declared in the same class (either all in the derived or all in some base)" and "has no base classes of the same type as the first non-static data member".
rev|since=c++20|
The empty member subobjects are permitted to be optimized out just like the empty bases if they use the attribute . Taking the address of such member results in an address that may equal the address of some other member of the same object.

## Notes

Empty base optimization is commonly used by allocator-aware standard library classes (`std::vector`, `std::function`, `std::shared_ptr`, etc) to avoid occupying any additional storage for its allocator member if the allocator is stateless. This is achieved by storing one of the required data members (e.g., `begin`, `end`, or `capacity` pointer for the `vector`) in an equivalent of [https://www.boost.org/doc/libs/release/libs/utility/doc/html/utility/utilities/compressed_pair.html `boost::compressed_pair`] with the allocator.
In MSVC, empty base optimization is not fully compliant with the standard requirements ([https://stackoverflow.com/questions/12701469/why-is-the-empty-base-class-optimization-ebo-is-not-working-in-msvc Why is the empty base class optimization (EBO) is not working in MSVC?]).

## References


## External links


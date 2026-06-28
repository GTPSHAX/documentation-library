---
title: std::inout_ptr_t
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/inout_ptr_t
---

ddcl|header=memory|since=c++23|
template< class Smart, class Pointer, class... Args >
class inout_ptr_t;
`inout_ptr_t` is used to adapt types such as smart pointers for foreign functions that reset ownership via a `Pointer*` (usually `T**` for some object type `T`) or `void**` parameter.
`inout_ptr_t` captures additional arguments on construction, provides a storage for the result which such an aforementioned foreign function accesses, releases the ownership held by the adapted `Smart` object, and finally resets the adapted `Smart` object with the result and the captured arguments when it is destroyed.
`inout_ptr_t` behaves as if it holds following non-static data members:
* a `Smart&` reference, which is bound to the adapted object on construction,
* for every `T` in `Args...`, a member of type `T`, which is an argument captured on construction and used for resetting while destruction, and
* a member subobject that suitable for storing a `Pointer` within it and providing a `void*` object, where the `Pointer` or `void*` object is generally exposed to a foreign function for ownership resetting.
If `Smart` is not a pointer type, `release()` is called at most once on the adapted object. Implementations may call `release()` within constructor, or before resetting within destructor if the `Pointer` value is not null.
Users can control whether each argument for resetting is captured by copy or by reference, by specifying an object type or a reference type in `Args...` respectively.

## Template parameters


### Parameters

- `Smart` - the type of the object (typically a smart pointer) to adapt
- `Pointer` - type of the object (typically a raw pointer) to which a foreign function accesses for ownership resetting
- `Args...` - type of captured arguments used for resetting the adapted object

**Type requirements:**

- `Pointer`

## Specializations

Unlike most class templates in the standard library, program-defined specializations of `inout_ptr_t` that depend on at least one  need not meet the requirements for the primary template.
This license allows a program-defined specialization to expose the raw pointer stored within a non-standard smart pointer to foreign functions.

## Member functions


## Non-member functions


| cpp/memory/inout_ptr_t/dsc inout_ptr | (see dedicated page) |


## Notes

`inout_ptr_t` expects that the foreign functions release the ownership represented by the value of the pointed-to `Pointer`, and then re-initialize it. As such operation requires unique ownership, the usage with `std::shared_ptr` is forbidden.
The typical usage of `inout_ptr_t` is creating its temporary objects by `std::inout_ptr`, which resets the adapted smart pointer immediately. E.g. given a setter function and a smart pointer of appropriate type declared with `int foreign_resetter(T**);` and `std::unique_ptr<T, D> up;` respectively,

```cpp
if (int ec = foreign_resetter(std::inout_ptr(up)))
    return ec;
```

is roughly equivalent to

```cpp
T *raw_p = up.get();
up.release();
int ec = foreign_resetter(&raw_p);
up.reset(raw_p);
if (ec != 0)
    return ec;
```

It is not recommended to create an `inout_ptr_t` object of a  other than automatic storage duration, because such code is likely to produce dangling references and result in undefined behavior on destruction.
Captured arguments are typically packed into a `std::tuple<Args...>`. Implementations may use different mechanism to provide the `Pointer` or `void*` object they need hold.

## Example


---
title: std::out_ptr_t
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/out_ptr_t
---

ddcl|header=memory|since=c++23|
template< class Smart, class Pointer, class... Args >
class out_ptr_t;
`out_ptr_t` is used to adapt types such as smart pointers for foreign functions that output their results via a `Pointer*` (usually `T**` for some object type `T`) or `void**` parameter.
`out_ptr_t` captures additional arguments on construction, provides storage for the result to which such an aforementioned foreign function writes, and finally resets the adapted `Smart` object with the result and the captured arguments when it is destroyed.
`out_ptr_t` behaves as if it holds following non-static data members:
* a `Smart&` reference, which is bound to the adapted object on construction,
* for every `T` in `Args...`, a member of type `T`, which is an argument captured on construction and used for resetting while destruction, and
* a member subobject that suitable for storing a `Pointer` within it and providing a `void*` object, where the `Pointer` or `void*` object is generally exposed to a foreign function for re-initialization.
Users can control whether each argument for resetting is captured by copy or by reference, by specifying an object type or a reference type in `Args...` respectively.

## Template parameters


### Parameters

- `Smart` - the type of the object (typically a smart pointer) to adapt
- `Pointer` - type of the object (typically a raw pointer) to which a foreign function writes its result
- `Args...` - type of captured arguments used for resetting the adapted object

**Type requirements:**

- `Pointer`

## Specializations

Unlike most class templates in the standard library, program-defined specializations of `out_ptr_t` that depend on at least one  need not meet the requirements for the primary template.
This license allows a program-defined specialization to expose the raw pointer stored within a non-standard smart pointer to foreign functions.

## Member functions


## Non-member functions


| cpp/memory/out_ptr_t/dsc out_ptr | (see dedicated page) |


## Notes

`out_ptr_t` expects that the foreign functions do not used the value of the pointed-to `Pointer`, and only re-initialize it. The value of the smart pointer before adaption is not used.
The typical usage of `out_ptr_t` is creating its temporary objects by `std::out_ptr`, which resets the adapted smart pointer immediately. E.g. given a setter function and a smart pointer of appropriate type declared with `int foreign_setter(T**);` and `std::unique_ptr<T, D> up;` respectively,

```cpp
int foreign_setter(T**);
std::unique_ptr<T, D> up;

if (int ec = foreign_setter(std::out_ptr(up)))
    return ec;
```

is roughly equivalent to

```cpp
int foreign_setter(T**);
std::unique_ptr<T, D> up;
T* raw_p{};

int ec = foreign_setter(&raw_p);
up.reset(raw_p);
if (ec != 0)
    return ec;
```

It is not recommended to create an `out_ptr_t` object of a  other than automatic storage duration, because such code is likely to produce dangling references and result in undefined behavior on destruction.
`out_ptr_t` forbids the usage that would reset a `std::shared_ptr` without specifying a deleter, because it would call `std::shared_ptr::reset` and replace a custom deleter later.
Captured arguments are typically packed into a `std::tuple<Args...>`. Implementations may use different mechanism to provide the `Pointer` or `void*` object they need hold.

## Example


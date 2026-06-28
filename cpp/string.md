---
title: Strings library
type: Strings
source: https://en.cppreference.com/w/cpp/string
---


# Strings library


## Characters

In the C++ standard library, a ''character'' is an object which, when treated sequentially, can represent text.
The term means not only objects of character types, but also any value that can be represented by a type that provides the definitions specified in the strings library and following libraries:
* localization library
* input/output library
rrev|since=c++11|
* regular expressions library
In the strings library<sup>(since C++11)</sup>  and regular expressions library, a character can be of only ''char-like types'', i.e. those non-array types that satisfy the requirements of
<sup>(until C++20)</sup> *PODType*<sup>(since C++20)</sup> until=c++26|*TrivialType and <sup>(since C++26)</sup> *TriviallyCopyable and .
rrev|since=c++26|
For any char-like type `T`, `std::is_trivially_default_constructible_v<T>` is `true`.
Therefore, characters are also referred as ''char-like objects'' in the strings library<sup>(since C++11)</sup>  and regular expressions library.
Some standard library components accept ''character container types''. They, too, are types used to represent individual characters. Such types are used for one of the template arguments of `std::char_traits` and the class templates which use `std::char_traits`.

## Library components

The C++ strings library includes the following components:

### Character traits

Many character-related class templates (such as `std::basic_string`) need a set of related types and functions to complete the definition of their semantics. These types and functions are provided as a set of member `typedef` names and functions in the template parameter `Traits` used by each such template. The classes which are able to complete those semantics are *CharTraits*.
The string library provides the class template `std::char_traits` that defines types and functions for `std::basic_string`<sup>(since C++17)</sup>  and `std::basic_string_view`.
The following specializations are defined, all of them satisfy the *CharTraits* requirements:

```cpp
**Header:** `<`string`>`
```

When a user-defined character container type for `std::basic_string`<sup>(since C++17)</sup>  and `std::basic_string_view` is used, it is also necessary to provide a corresponding character trait class (which can be a specialization of `std::char_traits`).

### String classes (`std::string` etc.)

The class template `std::basic_string` generalizes how sequences of characters are manipulated and stored.  String creation, manipulation, and destruction are all handled by a convenient set of class methods and related functions.
Several specializations of `std::basic_string` are provided for commonly-used types:


| Item | Description |
|------|-------------|
| string | |
| **Type** | Definition |


### String view classes (`std::string_view` etc.) <sup>(C++17)</sup>

The class template `std::basic_string_view` provides a lightweight object that offers read-only access to a string or a part of a string using an interface similar to the interface of `std::basic_string`.
Several specializations of `std::basic_string_view` are provided for commonly-used types:


| Item | Description |
|------|-------------|
| string_view | |
| **Type** | Definition |


## Relevant libraries

The text processing library provides support for localizations, string conversions (e.g. ), character classification functions (e.g. ), and text encoding recognition ().

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-1170 | C++98 | char-like types could be array types | prohibited |


## See also


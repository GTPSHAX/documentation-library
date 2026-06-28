---
title: Converting constructor
type: Language
source: https://en.cppreference.com/w/cpp/language/converting_constructor
---


# Converting constructor

A constructor that is not declared with the specifier `explicit` <sup>(until C++11)</sup> and which can be called with a single parameter is called a ''converting constructor''.
Unlike explicit constructors, which are only considered during `direct initialization` (which includes `explicit conversions` such as `static_cast`), converting constructors are also considered during `copy initialization`, as part of `user-defined conversion sequence`.
It is said that a converting constructor specifies an implicit conversion from the types of its arguments (if any) to the type of its class. Note that non-explicit `user-defined conversion function` also specifies an implicit conversion.
Implicitly-declared and user-defined non-explicit `copy constructor`s and `move constructor`s are converting constructors.

## Example


## See also

* `copy assignment`
* `copy constructor`
* `copy elision`
* `default constructor`
* `destructor`
* `explicit`
* `initialization`
** `aggregate initialization`
** `constant initialization`
** `copy initialization`
** `default initialization`
** `direct initialization`
** `initializer list`
** `list initialization`
** `reference initialization`
** `value initialization`
** `zero initialization`
* `move assignment`
* `move constructor`
* `new`

---
title: Default constructors
type: Language
source: https://en.cppreference.com/w/cpp/language/default_constructor
---


# Default constructors

A default constructor is a `constructor` which can be called with no arguments.

## Syntax


**Syntax:**

- `**`(`***parameter-list* (optional)**`);`**`
- `**`(`***parameter-list* (optional)**`)`** *function-body*`
- `**`() = default;`**|notes=<sup>(C++11)</sup>`
- `**`(`***parameter-list* (optional)**`) = delete;`**|notes=<sup>(C++11)</sup>`
- `**`::`**class-name**`(`***parameter-list* (optional)**`)`** *function-body*`
- `**`::`**class-name**`() = default;`**|notes=<sup>(C++11)</sup>`

### Parameters

- `{{spar` - class-name|the class whose default constructor is being declared
- `{{spar` - parameter-list|a  where all parameters<sup>(since C++11)</sup>  (except `parameter packs)` have `default arguments`
- `{{spar` - function-body|the `function body` of the default constructor

## Explanation

1. Declaration of a default constructor inside of class definition.
@2-4@ Definition of a default constructor inside of class definition.
:@3@ The default constructor is explicitly-defaulted.
:@4@ The default constructor is deleted.
@5,6@ Definition of a default constructor outside of class definition (the class must contain a declaration ).
:@6@ The default constructor is explicitly-defaulted.
Default constructors are called during `default initialization`s and `value initialization`s.

## Implicitly-declared default constructor

If there is no user-declared constructor or constructor template for a class type, the compiler will implicitly declare a default constructor as an `inline public` member of its class.
The implicitly-declared (or defaulted on its first declaration) default constructor has an exception specification as described in <sup>(until C++17)</sup> `dynamic exception specification` <sup>(since C++17)</sup> `noexcept specification`.

## Implicitly-defined default constructor

If <sup>(until C++11)</sup> the constructor is implicitly-declared<sup>(since C++11)</sup> the implicitly-declared or explicitly-defaulted default constructor is not defined as deleted, it is implicitly-defined by the compiler when `odr-used`<sup>(since C++11)</sup>  or `needed for constant evaluation`.
rrev|since=c++26|
If a default constructor of a `union-like class` `T` is trivial, then for each union `U` that is either `T` or an anonymous union member of `T`, if the first variant member (if any) of `U` has , the default constructor of `T` begins the lifetime of that member if it is not the active member of its union.
<sup>(until C++26)</sup> An<sup>(since C++26)</sup> Otherwise, an implicitly-defined default constructor has the same effect as a user-defined constructor with empty body and empty initializer list. That is, it calls the default constructors of the bases and of the non-static members of this class. Class types with an empty user-provided constructor may get treated differently than those with an implicitly-defined default constructor during `value initialization`.
rrev|since=c++11|
If this satisfies the requirements of a <sup>(until C++23)</sup> ``constexpr` constructor`<sup>(since C++23)</sup> ``constexpr` function`, the generated constructor is `constexpr`.
If some user-defined constructors are present, the user may still force the automatic generation of a default constructor by the compiler that would be implicitly-declared otherwise with the keyword `default`.
rrev|since=c++11|

## Deleted default constructor

The implicitly-declared or explicitly-defaulted default constructor for class `T` is defined as deleted if any of the following conditions is satisfied:
* `T` has a non-static data member of reference type without a default initializer.
* `T`<sup>(since C++26)</sup>  is a non-`union class and` has a non-variant non-static non-`const-default-constructible` data member of const-qualified type (or possibly multidimensional array thereof) without a default member initializer.
rrev|until=c++26|
* `T` is a `union` and all of its variant members are of const-qualified type (or possibly multidimensional array thereof).
* `T` is a non-union class and all members of any `anonymous union` member are of const-qualified type (or possibly multidimensional array thereof).
* Given a class type `M`, `T` has a  `obj` of type `M` (or possibly multidimensional array thereof), and any of the following conditions is satisfied:
:* `M` has a destructor that is deleted or inaccessible from the default constructor<sup>(since C++26)</sup> , and either `obj` is non-variant or `obj` has a default member initializer.
:* All following conditions are satisfied:
::* `obj` is not a non-static data member with a default initializer.
::* `obj` is not a variant member<sup>(until C++26)</sup>  of a union where another non-static data member has a default initializer.
::* The overload resolution as applied to find `M`'s default constructor does not result in a usable candidate<sup>(until C++26)</sup> , or in the case of `obj` being a variant member, selects a non-trivial function.
If no user-defined constructors are present and the implicitly-declared default constructor is not trivial, the user may still inhibit the automatic generation of an implicitly-defined default constructor by the compiler with the keyword `delete`.

## Trivial default constructor

The default constructor for class `T` is trivial if all following conditions are satisfied:
* The constructor is <sup>(until C++11)</sup> implicitly-declared<sup>(since C++11)</sup> not `user-provided`.
* `T` has no virtual member functions.
* `T` has no virtual base classes.
rrev|since=c++11|
* `T` has no non-static members with default initializers.
* Every direct base of `T` has a trivial default constructor.
rev|until=c++26|
* Every non-static member of class type (or array thereof) has a trivial default constructor.
rev|since=c++26|
* Either `T` is a union, or every non-variant non-static member of class type (or array thereof) has a trivial default constructor.
A trivial default constructor is a constructor that performs no action. All data types compatible with the C language (POD types) are trivially default-constructible.

## Eligible default constructor

Triviality of eligible default constructors determines whether the class is an implicit-lifetime type, and whether the class is a .

## Notes


## Example


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-1353 | C++11 | the conditions where implicitly-declared default constructors are<br>defined as deleted did not consider multidimensional array types | consider these types |
| cwg-2084 | C++11 | default member initializers had no effect on whether<br>a defaulted default constructor of a union is deleted | they prevent the defaulted default<br>constructor from being deleted |
| cwg-2595 | C++20 | a default constructor was not eligible if there is<br>another default constructor which is more constrained<br>but does not satisfy its associated constraints | it can be eligible in this case |
| cwg-2871 | C++98 | a default constructor would be implicitly declared<br>even if there is a user-declared constructor template | no implicit declaration<br>in this case |


## See also

* `constructor`
* `initialization`
** `aggregate initialization`
** `constant initialization`
** `copy initialization`
** `default initialization`
** `direct initialization`
** `list initialization`
** `reference initialization`
** `value initialization`
** `zero initialization`
* `new`

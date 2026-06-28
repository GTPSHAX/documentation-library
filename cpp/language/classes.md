---
title: Classes
type: Language
source: https://en.cppreference.com/w/cpp/language/classes
---


# Classes

A class is a user-defined type.
A class type is defined by class-specifier, which appears in *decl-specifier-seq* of the `declaration` syntax. See `class declaration` for the syntax of the class specifier.
A class can have the following kinds of members:
1. data members:
:@a@ `non-static data members`, including `bit-fields`.
:@b@ `static data members`
2. member functions:
:@a@ `non-static member functions`
:@b@ `static member functions`
3. nested types:
:@a@ `nested classes` and `enumerations` defined within the class definition
:@b@ aliases of existing types, defined with `typedef` <sup>(since C++11)</sup> or `type alias `declarations
:@c@ the name of the class within its own definition acts as a public member type alias of itself for the purpose of `lookup` (except when used to name a `constructor`): this is known as ''`injected-class-name`''
4. `enumerators` from all unscoped enumerations defined within the class<sup>(since C++20)</sup> , or introduced by `using-declarations or `enum#Using-enum-declaration|using-enum-declaration`s`
5. `member template`s (<sup>(since C++14)</sup> variable templates, class templates or function templates) may appear in the body of any non-local class/struct/union.
All members are defined at once in the class definition, they cannot be added to an already-defined class (unlike the members of namespaces)
A member of a class `T` cannot use `T` as its name if the member is
* a static data member,
* a member function,
* a member type,
* a member template,
* an enumerator of an enumeration <sup>(since C++11)</sup> (unless the enumeration is scoped), or
* a member of a member anonymous union.
However, a non-static data member may use the name `T` as long as there are no user-declared constructors.
A class with at least one declared or inherited `virtual` member function is ''polymorphic''. Objects of this type are `polymorphic objects` and have runtime type information stored as part of the object representation, which may be queried with `dynamic_cast` and `typeid`. Virtual member functions participate in dynamic binding.
A class with at least one declared or inherited pure virtual member function is an `abstract class`. Objects of this type cannot be created.
rrev|since=c++11|
A class with a `constexpr` constructor is a *LiteralType*: objects of this type can be manipulated by `constexpr` functions at compile time.

## Properties of classes

rrev|since=c++11|1=

### Trivially copyable class

A ''trivially copyable class'' is a class that
* has at least one eligible `copy constructor`, `move constructor`, `copy assignment operator`, or `move assignment operator`,
* each eligible copy constructor is `trivial`
* each eligible move constructor is `trivial`
* each eligible copy assignment operator is `trivial`
* each eligible move assignment operator is `trivial`, and
* has a non-deleted `trivial destructor`.
<tr class="t-rev">
<td>

### Trivial class

A ''trivial class'' is a class that
* is trivially copyable, and
* has one or more `eligible default constructors` such that each is `trivial`.
</td>
<td><sup>(deprecated C++26)</sup></td>
</tr>

### Standard-layout class

A ''standard-layout class'' is a class that
* has no `non-static data members` of type non-standard-layout class (or array of such types) or reference,
* has no `virtual functions` and no `virtual base classes`,
* has the same `access control` for all non-static data members,
* has no non-standard-layout base classes,
* only one class in the hierarchy has non-static data members, and
<!-- the rules below displayed on the page was copied from the standard, it may be substituted by the following contents taken from cpp/named_req/StandardLayoutType page if needed:
* None of the base class subobjects has the same type as
:* for non-union types, as the first non-static data member (see `empty base optimization`), and, recursively, the first non-static data member of that data member if it has non-union class type, or all non-static data members of that data member if it has union type, or an element of that data member if it has array type, etc.
:* for union types, as any non-static data members, and, recursively, the first non-static data member of every member of non-union class type, and all non-static data members of all members of union type, and element type of all non-static data members of array type, etc.
:* for array types, as the type of the array element, and, recursively, the first non-static data member of the array element if it has non-union class type, or as any non-static data member of the array element if it has union type, or as the element type of the array element if it has array type, etc.
-->
* Informally, none of the base classes has the same type as the first non-static data member. Or, formally: given the class as S, has no element of the set M(S) of types as a base class, where M(X) for a type X is defined as:
:* If X is a non-union class type with no (possibly inherited) non-static data members, the set M(X) is empty.
:* If X is a non-union class type whose first non-static data member has type X0 (where said member may be an anonymous union), the set M(X) consists of X0 and the elements of M(X0).
:* If X is a union type, the set M(X) is the union of all M(Ui) and the set containing all Ui, where each Ui is the type of the ith non-static data member of X.
:* If X is an array type with element type Xe, the set M(X) consists of Xe and the elements of M(Xe).
:* If X is a non-class, non-array type, the set M(X) is empty.
A ''standard-layout struct'' is a standard-layout class defined with the class keyword `cpp/keyword/struct` or the class keyword `cpp/keyword/class`. A ''standard-layout union'' is a standard-layout class defined with the class keyword `cpp/keyword/union`.

### Implicit-lifetime class

An ''implicit-lifetime class'' is a class that
* is an `aggregate` whose destructor is not <sup>(until C++11)</sup> user-declared<sup>(since C++11)</sup> `user-provided`, or
* has at least one trivial eligible constructor and a trivial, non-deleted destructor.
Notes: the implicit-lifetime property is clarified by defect report `P0593R6`.
<tr class="t-rev">
<td>

### POD class

A ''POD class'' is a class that
rrev multi|rev1=
* is an `aggregate`,
* has no user-declared copy assignment operator,
* has no user-declared destructor, and
* has no non-static data members of type non-POD class (or array of such types) or reference.
|since2=c++11|rev2=
* is a trivial class,
* is a standard-layout class, and
* has no non-static data members of type non-POD class (or array of such types).
A ''POD struct'' is a non-union POD class. A ''POD union'' is a union that is a POD class.
</td>
<td><sup>(deprecated C++20)</sup></td>
</tr>

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-148 | C++98 | POD classes could not contain pointers to member,<br>which are themselves POD (scalar) types | restriction removed |
| cwg-383 | C++98 | copy assignment operators or destructors could be<br>user-declared in POD classes if they are not defined | not allowed |
| cwg-1363 | C++11 | a class that has both trivial default constructors and non-trivial<br> default constructors at the same time could be trivial | it is non-trivial |
| cwg-1496 | C++11 | a class that only has constructors that<br>are all defined as deleted could be trivial | it is non-trivial |
| cwg-1672 | C++11 | a class could be a standard-layout class<br>if it has multiple empty base classes | it is not a standard-layout class |
| cwg-1734 | C++11 | a trivially copyable class could not have non-trivial<br>deleted copy/move constructors/assignment operators | can be trivial if deleted |
| cwg-1813 | C++11 | a class was never a standard-layout class if it has a<br>base class that inherits a non-static data member | it can be a standard-layout class |
| cwg-1881 | C++11 | for a standard-layout class and its base classes,<br>unnamed bit-fields might be declared in a<br>different class declaring the data members | all non-static data members<br>and bit-fields need to be first<br>declared in the same class |
| cwg-1909 | C++98 | a member template could have the same name as its class | prohibited |
| cwg-2120 | C++11 | the definition of M(X) in determining a standard-<br>layout class did not consider the case of<br>a class whose first member is an array | addressed this case in<br>the definition of M(X) |
| cwg-2605 | C++98 | an implicit-lifetime class could have a user-provided destructor | prohibited |


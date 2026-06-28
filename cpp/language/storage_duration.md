---
title: Storage class specifiers
type: Language
source: https://en.cppreference.com/w/cpp/language/storage_duration
---


# Storage class specifiers

The storage class specifiers are a part of the *decl-specifier-seq* of a name's `declaration syntax`. Together with the `scope` of the name, they control two independent properties of the name: its ''storage duration'' and its ''linkage''.

## Storage duration

The ''storage duration'' is the property of an `object` that defines the minimum potential lifetime of the storage containing the object. The storage duration is determined by the construct used to create the object and is one of the following:
* static storage duration
rrev|since=c++11|
* thread storage duration
* automatic storage duration
* dynamic storage duration
Static<sup>(since C++11)</sup> , thread, and automatic storage durations are associated with objects introduced by `declarations` and with `temporary objects`. The dynamic storage duration is associated with objects created by a ``new` expression` or with `implicitly created objects`.
The storage duration categories apply to references as well.
The storage duration of  and reference members is that of their complete object.

### Specifiers

The following keywords are ''storage class specifiers'':
rev|until=c++11|
* `auto`
rev|until=c++17|
* `register`
* `static`
rrev|since=c++11|
* `thread_local`
* `extern`
* `mutable`
In a *decl-specifier-seq*, there can be at most one storage class specifier<sup>(since C++11)</sup> , except that `thread_local` may appear with `static` or `extern`.
`mutable` has no effect on storage duration. For its usage, see `const/volatile`.
Other storage class specifiers can appear in the decl-specifier-seqs of the following declarations:


| rowspan=4 | Specifier |
| colspan=9 | Can appear in the spar sep | decl-specifier-seqs of |
| - |
| colspan=4 | Variable declarations |
| colspan=3 | Function declarations |
| rowspan=3 | Structured binding declarations<br><sup>(C++17)</sup> |
| - |
| colspan=2 | Non-member |
| colspan=2 | Member |
| rowspan=2 | Non-member |
| colspan=2 | Member |
| - |
| Non-parameter |
| Function parameter |
| Non-static |
| Static |
| Non-static |
| Static |
| - |
| c/core | auto |
| maybe | Block scope only |  |  |  |
|  |  |  |  |
| - |
| c/core | register |
| maybe | Block scope only |  |  |  |
|  |  |  |  |
| - |
| c/core | static |
|  |  | colspan=2 yes | Declares static |
| maybe | Namespace scope only | colspan=2 yes | Declares static |  |
| - |
| c/core | thread_local |
|  |  |  |  |
|  |  |  |  |
| - |
| c/core | extern |
|  |  |  |  |
|  |  |  |  |

can also be declared with `static`.
rrev|until=c++17|
`register` is a hint that the variable so declared will be heavily used, so that its value can be stored in a CPU register. The hint can be ignored, and in most implementations it will be ignored if the address of the variable is taken. This use is deprecated.

### Static storage duration

A variable satisfying all following conditions has ''static storage duration'':
* It belongs to a  or are first declared with `static` or `extern`.
rrev|since=c++11|
* It does not have thread storage duration.
The storage for these entities lasts for the duration of the program.
rrev|since=c++11|

### Thread storage duration

All variables declared with `thread_local` have ''thread storage duration''.
The storage for these entities lasts for the duration of the thread in which they are created. There is a distinct object or reference per thread, and use of the declared name refers to the entity associated with the current thread.

### Automatic storage duration

The following variables have ''automatic storage duration'':
* Variables that belong to a  and are not explicitly declared `static`<sup>(since C++11)</sup> , `thread_local`, or `extern`. The storage for such variables lasts until the block in which they are created exits.
* Variables that belong to a parameter scope (i.e. function parameters). The storage for a function parameter lasts until immediately after its `destruction`.
In addition, `temporary objects` also have an automatic storage duration.

### Dynamic storage duration

Objects created by the following methods during program execution have ''dynamic storage duration'':
* ``new` expressions`. The storage for such objects is allocated by allocation functions and deallocated by deallocation functions.
* `Implicitly creation` by other means. The storage for such objects overlaps with some existing storage.
* s. The storage for such objects is allocated and deallocated in an unspecified way.

## Linkage

A name can have ''external linkage''<sup>(since C++20)</sup> , ''module linkage'', ''internal linkage'', or ''no linkage'':
* An entity whose name has external linkage can be `redeclared` in another `translation unit`<sup>(since C++20)</sup> , and the redeclaration can be `attached to a different module`.
rrev|since=c++20|
* An entity whose name has module linkage can be redeclared in another translation unit, as long as the redeclaration is attached to the same module.
* An entity whose name has internal linkage can be redeclared in another scope in the same translation unit.
* An entity whose name has no linkage can only be redeclared in the same scope.
The following linkages are recognized:

### No linkage

Any of the following names declared at block scope have no linkage:
* variables that are not explicitly declared `extern` (regardless of the `static` modifier);
*  and their member functions;
* other names declared at block scope such as typedefs, enumerations, and enumerators.
Names not specified with external<sup>(since C++20)</sup> , module, or internal linkage also have no linkage, regardless of which scope they are declared in.

### Internal linkage

Any of the following names declared at namespace scope have internal linkage:
* variables<sup>(since C++14)</sup> , variable templates, functions, or function templates declared `static`;
* <sup>(since C++14)</sup> non-template variables of non-volatile const-qualified type, unless
rev|since=c++17|
:* they are inline,
rev|since=c++20|
:* they are declared in the purview of a `module interface unit` (outside the , if any) or `module partition`,
:* they are explicitly declared `extern`, or
:* they were previously declared and the prior declaration did not have internal linkage;
* data members of `anonymous unions`.
rrev|since=c++11|
In addition, all names declared in  or a namespace within an unnamed namespace, even ones explicitly declared `extern`, have internal linkage.

### External linkage

Variables and functions with external linkage also have `language linkage`, which makes it possible to link translation units written in different programming languages.
Any of the following names declared at namespace scope have external linkage, unless they are declared in an unnamed namespace<sup>(since C++20)</sup>  or their declarations are attached to a named module and are not exported:
* variables and functions not listed above (that is, functions not declared `static`, non-const variables not declared `static`, and any variables declared `extern`);
* enumerations;
* names of classes, their member functions, static data members (const or not), nested classes and enumerations, and functions first introduced with `friend` declarations inside class bodies;
* names of all templates not listed above (that is, not function templates declared `static`).
Any of the following names first declared at block scope have external linkage:
* names of variables declared `extern`;
* names of functions.
rrev|since=c++20|

### Module linkage

Names declared at namespace scope have module linkage if their declarations are attached to a named module and are not exported, and do not have internal linkage.

## Static block variables

Block variables with static<sup>(since C++11)</sup>  or thread storage duration are initialized the first time control passes through their declaration (unless their initialization is `zero-` or `constant-initialization`, which can be performed before the block is first entered). On all further calls, the declaration is skipped.
* If the initialization `throws an exception`, the variable is not considered to be initialized, and initialization will be attempted again the next time control passes through the declaration.
* If the initialization recursively enters the block in which the variable is being initialized, the behavior is undefined.
rrev|since=c++11|
* If multiple threads attempt to initialize the same static local variable concurrently, the initialization occurs exactly once (similar behavior can be obtained for arbitrary functions with `std::call_once`).
:* Usual implementations of this feature use variants of the double-checked locking pattern, which reduces runtime overhead for already-initialized local statics to a single non-atomic boolean comparison.
The destructor for a block variable with static storage duration is called at program exit, but only if the initialization took place successfully.
Variables with static storage duration in all definitions of the same `inline function` (which may be implicitly inline) all refer to the same object defined in one translation unit, as long as the function has external linkage.

## Translation-unit-local entities

The concept of translation-unit-local entities is standardized in C++20, see `this page` for more details.
An entity is ''translation-unit-local'' (or ''TU-local'' for short) if
* it has a name with internal linkage, or
* it does not have a name with linkage and is introduced within the definition of a TU-local entity, or
* it is a template or template specialization whose template argument or template declaration uses a TU-local entity.
Bad things (usually violation of `ODR`) can happen if the type of a non-TU-local entity depends on a TU-local entity, or if a declaration of<sup>(since C++17)</sup> , or a `deduction guide for,` a non-TU-local entity names a TU-local entity outside its
* function-body for a non-inline function or function template
* initializer for a variable or variable template
* friend declarations in a class definition
* use of value of a variable, if the variable is
rrev|since=c++20|
Such uses are disallowed in a `module interface unit` (outside its private-module-fragment, if any) or a module partition, and are deprecated in any other context.
A declaration that appears in one translation unit cannot name a TU-local entity declared in another translation unit that is not a header unit. A declaration instantiated for a `template` appears at the point of instantiation of the specialization.

## Notes

Names at the top-level namespace scope (file scope in C) that are `const` and not `extern` have external linkage in C, but internal linkage in C++.
Since C++11, `auto` is no longer a storage class specifier; it is used to indicate type deduction.
rrev multi|until1=c++17
|rev1=
In C, the address of a `register` variable cannot be taken, but in C++, a variable declared `register` is semantically indistinguishable from a variable declared without any storage class specifiers.
|rev2=
In C++, unlike C, variables cannot be declared `register`.
Names of `thread_local` variables with internal or external linkage referred from different scopes may refer to the same or to different instances depending on whether the code is executing in the same or in different threads.
The `extern` keyword can also be used to specify `language linkage` and `explicit template instantiation declarations`, but it's not a storage class specifier in those cases (except when a declaration is directly contained in a language linkage specification, in which case the declaration is treated as if it contains the `extern` specifier).
Storage class specifiers, except for `thread_local`, are not allowed on `explicit specializations` and s:

```cpp
template<class T>
struct S
{
    thread_local static int tlm;
};

template<>
thread_local int S<float>::tlm = 0; // "static" does not appear here
```

rev|since=c++14|
A `const` (may be implied by `constexpr`) variable template used to have internal linkage by default, which was inconsistent with other templated entities. Defect report `CWG2387` corrected this.
rev|since=c++17|1=
`inline` acts as a workaround for `CWG2387` by giving external linkage by default. This is why the `inline` was [https://wg21.link/p0607r0 added] to many variable templates and then [https://github.com/cplusplus/draft/pull/4625 removed] after having CWG2387 accepted. Standard library implementations also need to use `inline` as long as a supported compiler has not get CWG2387 implemented. See [https://gcc.gnu.org/bugzilla/show_bug.cgi?id=109126 GCC Bugzilla #109126] and [https://github.com/microsoft/STL/pull/4546 MSVC STL PR #4546].

## Keywords

`cpp/keyword/auto`,
`cpp/keyword/register`,
`cpp/keyword/static`,
`cpp/keyword/extern`,
`cpp/keyword/thread_local`,
`cpp/keyword/mutable`

## Example


### Example

```cpp
#include <iostream>
#include <mutex>
#include <string>
#include <thread>

thread_local unsigned int rage = 1;
std::mutex cout_mutex;

void increase_rage(const std::string& thread_name)
{
    ++rage; // modifying outside a lock is okay; this is a thread-local variable
    std::lock_guard<std::mutex> lock(cout_mutex);
    std::cout << "Rage counter for " << thread_name << ": " << rage << '\n';
}

int main()
{
    std::thread a(increase_rage, "a"), b(increase_rage, "b");

    {
        std::lock_guard<std::mutex> lock(cout_mutex);
        std::cout << "Rage counter for main: " << rage << '\n';
    }

    a.join();
    b.join();
}
```


**Output:**
```
Rage counter for a: 2
Rage counter for main: 1
Rage counter for b: 2
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-216 | C++98 | unnamed class and enumeration in class scope have<br>different linkage from those in namespace scope | they all have external<br>linkage in these scopes |
| cwg-389 | C++98 | a name with no linkage should not be<br>used to declare an entity with linkage | a type without linkage shall not be used<br>as the type of a variable or function<br>with linkage, unless the variable<br>or function has C language linkage |
| cwg-426 | C++98 | an entity could be declared with both internal<br>and external linkage in the same translation unit | the program is ill-formed in this case |
| cwg-527 | C++98 | the type restriction introduced by the resolution of CWG<br>389 was also applied to variables and functions that<br>cannot be named outside their own translation units | the restriction is lifted for these<br>variables and functions (i.e. with no<br>linkage or internal linkage, or declared<br>within unnamed namespaces) |
| cwg-2019 | C++98 | the storage duration of reference<br>members were unspecified | same as their complete object |
| cwg-2387 | C++14 | unclear whether const-qualified variable<br>template have internal linkage by default | const qualifier does not affect<br>the linkage of variable<br>templates or their instances |
| cwg-2533 | C++98 | the storage duration of implicitly-<br>created objects were unclear | made clear |
| cwg-2850 | C++98 | it was unclear when the storage for<br>function parameters are deallocated | made clear |
| cwg-2872 | C++98 | the meaning of “can be referred to” was unclear | improved wording |


## References


## See also


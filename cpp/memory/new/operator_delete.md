---
title: operators (delete[])
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/new/operator_delete
---


# small|operator


```cpp
**Header:** `<`new`>`
dcl rev multi|num=1|anchor=1|until1=c++11
|dcl1=void operator delete  ( void* ptr ) throw();
|dcl2=void operator delete  ( void* ptr ) noexcept;
dcl rev multi|num=2|anchor=2|until1=c++11
|dcl1=void operator delete[]( void* ptr ) throw();
|dcl2=void operator delete[]( void* ptr ) noexcept;
dcla|num=7|since=c++17|void operator delete  ( void* ptr, std::size_t sz,
std::align_val_t al ) noexcept;
dcla|num=8|since=c++17|void operator delete[]( void* ptr, std::size_t sz,
std::align_val_t al ) noexcept;
dcl rev multi|num=9|anchor=9|until1=c++11
|dcl1=void operator delete  ( void* ptr, const std::nothrow_t& tag ) throw();
|dcl2=void operator delete  ( void* ptr, const std::nothrow_t& tag ) noexcept;
dcl rev multi|num=10|anchor=10|until1=c++11
|dcl1=void operator delete[]( void* ptr, const std::nothrow_t& tag ) throw();
|dcl2=void operator delete[]( void* ptr, const std::nothrow_t& tag ) noexcept;
dcla|num=11|since=c++17|void operator delete  ( void* ptr, std::align_val_t al,
const std::nothrow_t& tag ) noexcept;
dcla|num=12|since=c++17|void operator delete[]( void* ptr, std::align_val_t al,
const std::nothrow_t& tag ) noexcept;
dcl rev multi|num=13|anchor=13|until1=c++11
|dcl1=void operator delete  ( void* ptr, void* place ) throw();
|dcl2=void operator delete  ( void* ptr, void* place ) noexcept;
dcl rev multi|num=14|anchor=14|until1=c++11
|dcl1=void operator delete[]( void* ptr, void* place ) throw();
|dcl2=void operator delete[]( void* ptr, void* place ) noexcept;
dcla|since=c++20|num=28|void T::operator delete( T* ptr, std::destroying_delete_t,
std::align_val_t al );
dcla|since=c++20|num=30|void T::operator delete( T* ptr, std::destroying_delete_t,
std::size_t sz, std::align_val_t al );
```

Deallocates storage previously allocated by a matching `operator new` or `operator new[]`. These deallocation functions are called by [[cpp/language/delete|`delete` and `delete[]` expressions]] and by placement `new` expressions to deallocate memory after destructing (or failing to construct) objects with dynamic storage duration. They may also be called using regular function call syntax.
@1-12@ Replaceable deallocation functions. The standard library provides default implementations for these functions, for the effects of the default implementations, see below.
:@1-8@ Called by `delete` and `delete[]` expressions. Invalidates any non-null `ptr`.
:@9-12@ Called by placement `new` expressions upon . `operator delete[]` invalidates any non-null `ptr`.
: If `ptr` is not a null pointer and one of the following conditions is satisfied, the behavior is undefined:
:* For `operator delete`, the value of `ptr` does not represent the address of a block of memory allocated by an earlier call to (possibly replaced) `operator new(std::size_t)` (for overloads ) or `operator new(std::size_t, std::align_val_t)` (for overloads ) which has not been invalidated by an intervening call to `operator delete`.
:* For `operator delete[]`, the value of `ptr` does not represent the address of a block of memory allocated by an earlier call to (possibly replaced) `operator new[](std::size_t)` (for overloads ) or `operator new[](std::size_t, std::align_val_t)` (for overloads ) which has not been invalidated by an intervening call to `operator delete[]`.
@13,14@ Called by placement `new` expressions that invoked `non-allocating placement allocation function` when any part of the initialization in the expression terminates by throwing an exception. Performs no action.
@15-30@ User-defined deallocation functions called by `delete`, `delete[]` and placement `new` expressions.
:@27-30@ If defined, `delete` expressions does not execute the destructor for `*ptr` before placing a call to `operator delete`. Instead, direct invocation of the destructor such as by `ptr->~T();` becomes the responsibility of this `operator delete`.
Overloads  are implicitly declared in each translation unit even if the  header is not included.
See `delete` expression for the criteria of selecting overload.

## Parameters


### Parameters

- `ptr` - pointer to a memory block to deallocate or a null pointer
- `sz` - the size that was passed to the matching allocation function
- `place` - pointer used as the placement parameter in the matching placement new
- `tag` - overload disambiguation tag matching the tag used by non-throwing operator new
- `al` - alignment of the object or array element that was allocated
- `args` - arbitrary parameters matching a placement allocation function (may include `std::size_t` and `std::align_val_t`)

## Exceptions

<sup>(since C++11)</sup> All deallocation functions are `noexcept(true)` unless specified otherwise in the declaration.
If a deallocation function terminates by throwing an exception, the behavior is undefined<sup>(since C++11)</sup> , even if it is declared with `noexcept(false)`.

## Global replacements

Overloads  are replaceable. The effects of the default versions are:
1. If `ptr` is null, does nothing. Otherwise, reclaims the storage allocated by the earlier call to `operator new`.
2. Calls `operator delete(ptr)` as if overload  can reclaim the storage allocated by the earlier call to `operator new[]`.
3. Same as .
4. Calls `operator delete(ptr, al)` as if overload  can reclaim the storage allocated by the earlier call to `operator new[]`.
5. Calls `operator delete(ptr)`.
6. Calls `operator delete[](ptr)`.
7. Calls `operator delete(ptr, al)`.
8. Calls `operator delete[](ptr, al)`.
9. Calls `operator delete(ptr)`.
10. Calls `operator delete[](ptr)`.
11. Calls `operator delete(ptr, al)`.
12. Calls `operator delete[](ptr, al)`.
Overloads of `operator delete` and `operator delete[]` with additional user-defined parameters ("placement forms", ) may be declared at global scope as usual, and are called by the matching placement forms of `new` expressions if a constructor of the object that is being allocated throws an exception.
The standard library placement forms of `operator delete` and `operator delete[]`  cannot be replaced and can only be customized if the placement `new` expression did not use the `::new` syntax, by providing a class-specific placement delete  with matching signature: `void T::operator delete(void*, void*)` or `void T::operator delete[](void*, void*)`.

## Class-specific overloads

Deallocation functions  may be defined as static member functions of a class. These deallocation functions, if provided, are called by `delete` expressions when deleting objects  and arrays  of this class, unless the delete expression used the form `::delete` which bypasses class-scope lookup. The keyword `static` is optional for these function declarations: whether the keyword is used or not, the deallocation function is always a static member function.
The delete expression looks for appropriate deallocation function's name starting from the class scope (array form looks in the scope of the array element class) and proceeds to the global scope if no members are found as usual. Note, that as per name lookup rules, any deallocation functions declared in class scope hides all global deallocation functions.
If the static type of the object that is being deleted differs from its dynamic type (such as when deleting a polymorphic object through a pointer to base), and if the destructor in the static type is virtual, the single object form of delete begins lookup of the deallocation function's name starting from the point of definition of the final overrider of its virtual destructor. Regardless of which deallocation function would be executed at run time, the statically visible version of `operator delete` must be accessible in order to compile. In other cases, when deleting an array through a pointer to base, or when deleting through pointer to base with non-virtual destructor, the behavior is undefined.
If the single-argument overload  is not provided, but the size-aware overload taking `std::size_t` as the second parameter  is provided, the size-aware form is called for normal deallocation, and the C++ runtime passes the size of the object to be deallocated as the second argument. If both forms are defined, the size-unaware version is called.

### Example

```cpp
#include <cstddef>
#include <iostream>

// sized class-specific deallocation functions
struct X
{
    static void operator delete(void* ptr, std::size_t sz)
    {
        std::cout << "custom delete for size " << sz << '\n';
        ::operator delete(ptr);
    }

    static void operator delete[](void* ptr, std::size_t sz)
    {
        std::cout << "custom delete for size " << sz << '\n';
        ::operator delete[](ptr);
    }
};

int main()
{
    X* p1 = new X;
    delete p1;

    X* p2 = new X[10];
    delete[] p2;
}
```


**Output:**
```
custom delete for size 1
custom delete for size 18
```

Overloads of `operator delete` and `operator delete[]` with additional user-defined parameters ("placement forms", ) may also be defined as class members. When the failed placement `new` expression looks for the corresponding placement `delete` function to call, it begins lookup at class scope before examining the global scope, and looks for the function with the signature matching the placement `new`:

### Example

```cpp
#include <cstddef>
#include <iostream>
#include <stdexcept>

struct X
{
    X() { throw std::runtime_error("X(): std::runtime_error"); }

    // custom placement new
    static void* operator new(std::size_t sz, bool b)
    {
        std::cout << "custom placement new called, b = " << b << '\n';
        return ::operator new(sz);
    }

    // custom placement delete
    static void operator delete(void* ptr, bool b)
    {
        std::cout << "custom placement delete called, b = " << b << '\n';
        ::operator delete(ptr);
    }
};

int main()
{
    try
    {
        [[maybe_unused]] X* p1 = new (true) X;
    }
    catch (const std::exception& ex)
    {
        std::cout << ex.what() << '\n';
    }
}
```


**Output:**
```
custom placement new called, b = 1
custom placement delete called, b = 1
X(): std::runtime_error
```

If class-level `operator delete` is a template function, it must have the return type of `void`, the first argument `void*`, and it must have two or more parameters. In other words, only placement forms can be templates. A template instance is never a usual deallocation function, regardless of its signature. The specialization of the template operator delete is chosen with .

## Notes

The call to the class-specific `T::operator delete` on a polymorphic class is the only case where a static member function is called through dynamic dispatch.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-220 | C++98 | user-defined deallocation functions were permitted to throw | throwing from a deallocation function<br>results in undefined behavior |
| cwg-1438 | C++98 | any use of an invalid pointer value was undefined behavior | only indirection and deallocation are |


## See also


| cpp/coroutine/generator/promise_type/dsc operator delete | (see dedicated page) |
| cpp/memory/new/dsc operator new | (see dedicated page) |
| cpp/memory/dsc return_temporary_buffer | (see dedicated page) |
| cpp/memory/c/dsc free | (see dedicated page) |


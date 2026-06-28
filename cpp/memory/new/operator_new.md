---
title: operators (new[])
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/new/operator_new
---


# small|operator


```cpp
**Header:** `<`new`>`
dcla|num=1|
void* operator new  ( std::size_t count );
dcla|num=2|
void* operator new[]( std::size_t count );
dcla|num=3|since=c++17|
void* operator new  ( std::size_t count, std::align_val_t al );
dcla|num=4|since=c++17|
void* operator new[]( std::size_t count, std::align_val_t al );
dcla|num=5|noexcept=c++11|
void* operator new  ( std::size_t count, const std::nothrow_t& tag );
dcla|num=6|noexcept=c++11|
void* operator new[]( std::size_t count, const std::nothrow_t& tag );
dcla|num=7|since=c++17|
void* operator new  ( std::size_t count, std::align_val_t al,
const std::nothrow_t& tag ) noexcept;
dcla|num=8|since=c++17|
void* operator new[]( std::size_t count, std::align_val_t al,
const std::nothrow_t& tag ) noexcept;
dcla|num=9|noexcept=c++11|constexpr=c++26|
void* operator new  ( std::size_t count, void* ptr );
dcla|num=10|noexcept=c++11|constexpr=c++26|
void* operator new[]( std::size_t count, void* ptr );
dcla|num=11|
void* operator new  ( std::size_t count, /* args... */ );
dcla|num=12|
void* operator new[]( std::size_t count, /* args... */ );
dcla|num=13|since=c++17|
void* operator new  ( std::size_t count,
std::align_val_t al, /* args... */ );
dcla|num=14|since=c++17|
void* operator new[]( std::size_t count,
std::align_val_t al, /* args... */ );
dcla|num=15|
void* T::operator new  ( std::size_t count );
dcla|num=16|
void* T::operator new[]( std::size_t count );
dcla|num=17|since=c++17|
void* T::operator new  ( std::size_t count, std::align_val_t al );
dcla|num=18|since=c++17|
void* T::operator new[]( std::size_t count, std::align_val_t al );
dcla|num=19|
void* T::operator new  ( std::size_t count, /* args... */ );
dcla|num=20|
void* T::operator new[]( std::size_t count, /* args... */ );
dcla|num=21|since=c++17|
void* T::operator new  ( std::size_t count,
std::align_val_t al, /* args... */ );
dcla|num=22|since=c++17|
void* T::operator new[]( std::size_t count,
std::align_val_t al, /* args... */ );
```

Attempts to allocate requested number of bytes, and the allocation request can fail (even if the requested number of bytes is zero). These allocation functions are called by `new` expressions to allocate memory in which new object would then be initialized. They may also be called using regular function call syntax.
@1-8@ Replaceable allocation functions. The standard library provides default implementations for these functions, for the effects of the default implementations, see below.
@9,10@ Called by the standard placement `new` expressions. Performs no action and returns `ptr` unmodified.
@@ If this function is called through placement `new` and `ptr` is a null pointer, the behavior is undefined.
@11-22@ User-defined allocation functions called by `new` expressions.
Overloads  are implicitly declared in each translation unit even if the  header is not included.
See `new` expression for the criteria of selecting overload.

## Parameters


### Parameters

- `count` - number of bytes to allocate
- `ptr` - pointer to a memory area to initialize the object at
- `tag` - disambiguation tag used to select non-throwing overloads
- `al` - alignment to use, invalid value leads to undefined behavior

## Return value

@1-4@ If the allocation succeeds, a non-null pointer `p0` which points to suitably aligned memory of size at least `size` and is different from any previously returned value `p1`, unless that value `p1` was subsequently passed to a replaceable `deallocation function`; if the allocation fails, does not return (an exception is thrown, see below).
@5-8@ Same as , but returns a null pointer if the allocation fails.
@9,10@ `ptr`
@11-22@ Same as  if the function does not return on allocation failure, otherwise same as .

## Exceptions

@1-4@ Throws an exception of a type that would match a handler of type `std::bad_alloc` on failure to allocate memory.
@11-22@ Same as  if the function does not return on allocation failure, otherwise same as .

## Global replacements

Overloads  are replaceable. The effects of the default versions are:
1. Attempts to allocate the requested storage. Whether the attempt involves a call to `std::malloc` or `std::aligned_alloc` is unspecified.
* If the attempt is successful, returns a pointer to the allocated storage, <sup>(until C++17)</sup> the storage is aligned to the fundamental alignment<sup>(since C++17)</sup> the storage is aligned to `__STDCPP_DEFAULT_NEW_ALIGNMENT__`.
* Otherwise, if currently no `new-handler` is installed, throws `std::bad_alloc`.
* Otherwise, calls the currently installed new-handler.
** If the new-handler returns, starts another allocation attempt.
** Otherwise, exits the current invocation.
2. Returns `operator new(count)`.
3. Same as (1), except that the returned storage is aligned to `al`.
4. Returns `operator new(count, al)`.
@5-8@ Calls  respectively with the same arguments except for `tag`.
* If the call returns normally, returns the result of that call.
* Otherwise, returns a null pointer.
rrev|since=c++26|
On freestanding implementations, it is implementation-defined whether the default versions of  satisfy the behaviors required above. Freestanding implementations are recommended that if any of these default versions meet the requirements of a hosted implementation, they all should.
Overloads of `operator new` and `operator new[]` with additional user-defined parameters ("placement forms", versions ) may be declared at global scope as usual, and are called by the matching placement forms of `new` expressions.
The standard library's non-allocating placement forms of `operator new`  cannot be replaced and can only be customized if the placement `new` expression did not use the `::new` syntax, by providing a class-specific placement `new`  with matching signature: `void* T::operator new(std::size_t, void*)` or `void* T::operator new[](std::size_t, void*)`.
rrev|since=c++14|
The placement form `void* operator new(std::size_t, std::size_t)` is not allowed because the matching signature of the deallocation function, `void operator delete(void*, std::size_t)`, is a usual (not placement) deallocation function.

## Class-specific overloads

Both single-object and array allocation functions may be defined as public static member functions of a class (versions ). If defined, these allocation functions are called by `new` expressions to allocate memory for single objects and arrays of this class, unless the `new` expression used the form `::new` which bypasses class-scope lookup. The keyword `cpp/keyword/static` is optional for these functions: whether used or not, the allocation function is a static member function.
The `new` expression looks for appropriate allocation function's name firstly in the class scope, and after that in the global scope. Note, that as per name lookup rules, any allocation functions declared in class scope hides all global allocation functions for the `new` expressions that attempt to allocate objects of this class.
rrev|since=c++17|
When allocating objects and arrays of objects whose alignment exceeds `__STDCPP_DEFAULT_NEW_ALIGNMENT__`, overload resolution is performed twice: first, for alignment-aware function signatures, then for alignment-unaware function signatures. This means that if a class with new-extended alignment has an alignment-unaware class-specific allocation function, it is the function that will be called, not the global alignment-aware allocation function. This is intentional: the class member is expected to know best how to handle that class.
rrev|since=c++20|
When allocating objects and arrays of objects whose alignment does not exceed `__STDCPP_DEFAULT_NEW_ALIGNMENT__`, overload resolution is performed twice: first, for alignment-unaware function signatures, then for alignment-aware function signatures.

### Example

```cpp
#include <cstddef>
#include <iostream>

// class-specific allocation functions
struct X
{
    static void* operator new(std::size_t count)
    {
        std::cout << "custom new for size " << count << '\n';
        return ::operator new(count);
    }

    static void* operator new[](std::size_t count)
    {
        std::cout << "custom new[] for size " << count << '\n';
        return ::operator new[](count);
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
custom new for size 1
custom new[] for size 10
```

Overloads of `operator new` and `operator new[]` with additional user-defined parameters ("placement forms"), may also be defined as class members ). When the placement `new` expression with the matching signature looks for the corresponding allocation function to call, it begins at class scope before examining the global scope, and if the class-specific placement `new` is provided, it is called.
rrev|since=c++17|
When allocating objects and arrays of objects whose alignment exceeds `__STDCPP_DEFAULT_NEW_ALIGNMENT__`, overload resolution for placement forms is performed twice just as for regular forms: first, for alignment-aware function signatures, then for alignment-unaware function signatures.
rrev|since=c++20|
When allocating objects and arrays of objects whose alignment does not exceed `__STDCPP_DEFAULT_NEW_ALIGNMENT__`, overload resolution for placement forms is performed twice just as for regular forms: first, for alignment-unaware function signatures, then for alignment-aware function signatures.

### Example

```cpp
#include <cstddef>
#include <iostream>
#include <stdexcept>

struct X
{
    X() { throw std::runtime_error(""); }

    // custom placement new
    static void* operator new(std::size_t count, bool b)
    {
        std::cout << "custom placement new called, b = " << b << '\n';
        return ::operator new(count);
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
    catch (const std::exception&)
    {}
}
```


**Output:**
```
custom placement new called, b = 1
custom placement delete called, b = 1
```

If class-level `operator new` is a template function, it must have the return type of `void*`, the first argument `std::size_t`, and it must have two or more parameters. In other words, only placement forms can be templates.

## Notes

Even though the non-allocating placement `new`  cannot be replaced, a function with the same signature may be defined at class scope as described above. In addition, global overloads that look like placement `new` but take a non-void pointer type as the second argument are allowed, so the code that wants to ensure that the true placement `new` is called (e.g. `std::allocator::construct`), must use `::new` and also cast the pointer to `void*`.
If the behavior of a deallocation function does not satisfy the default constraints, the behavior is undefined.
It is unspecified whether library versions of `operator new` make any calls to `std::malloc`<sup>(since C++17)</sup>  or `std::aligned_alloc`.
For loading a large file, file mapping via OS-specific functions, e.g.,  on POSIX or `CreateFileMapping`([https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-createfilemappinga `A`]/[https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-createfilemappingw `W`]) along with [https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffile `MapViewOfFile`] on Windows, is preferable to allocating a buffer for file reading.

### Feature Test Macros

| Macro | Value | Std | Description |
|-------|-------|-----|-------------|
| `-` | 0 | C++26 | no freestanding support |
| `__cpp_lib_constexpr_new` | 202406L | C++26 | `constexpr` placement `new` and `new[]` |


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-9 | C++98 | multiple calls for allocating zero<br>bytes could yield the same pointer | only allowed if all such previously<br>yielded pointers have been<br>passed to deallocation functions |
| lwg-206 | C++98 | replacing the replaceable allocation functions did<br>not affect the default behaviors of the corresponding<br>replaceable non-throwing allocation functions | the default behaviors<br>change accordingly |


## References


## See also


| cpp/coroutine/generator/promise_type/dsc operator new | (see dedicated page) |
| cpp/memory/new/dsc operator_delete | (see dedicated page) |
| cpp/memory/new/dsc get_new_handler | (see dedicated page) |
| cpp/memory/new/dsc set_new_handler | (see dedicated page) |
| cpp/memory/dsc get_temporary_buffer | (see dedicated page) |
| cpp/memory/c/dsc malloc | (see dedicated page) |
| cpp/memory/c/dsc aligned_alloc | (see dedicated page) |


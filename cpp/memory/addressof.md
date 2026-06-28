---
title: std::addressof
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/addressof
---


```cpp
**Header:** `<`memory`>`
|
template< class T >
T* addressof( T& arg ) noexcept;
dcl|since=c++11|num=2|1=
template< class T >
const T* addressof( const T&& ) = delete;
```

1. Obtains the actual address of the object or function `arg`, even in presence of overloaded `operator&`.
2. Rvalue overload is deleted to prevent taking the address of `const` rvalues.
rrev|since=c++17|
The expression `std::addressof(e)` is a constant subexpression, if `e` is an lvalue constant subexpression.

## Parameters


### Parameters

- `arg` - lvalue object or function

## Return value

Pointer to `arg`.

## Possible implementation

The implementation below is not `constexpr`, because `reinterpret_cast` is not usable in a constant expression. Compiler support is needed (see below).
eq fun
|1=
template<class T>
typename std::enable_if<std::is_object<T>::value, T*>::type addressof(T& arg) noexcept
{
return reinterpret_cast<T*>(
&const_cast<char&>(
reinterpret_cast<const volatile char&>(arg)));
}
template<class T>
typename std::enable_if<!std::is_object<T>::value, T*>::type addressof(T& arg) noexcept
{
return &arg;
}
Correct implementation of this function requires compiler support: [https://github.com/gcc-mirror/gcc/blob/b8806796ec64585de39ca6ee3b7b30cc08f27d62/libstdc++-v3/include/bits/move.h#L47-L50 GNU libstdc++], [https://github.com/llvm/llvm-project/blob/5146b57b403b3a512dc64e766695b13803ef3b54/libcxx/include/__memory/addressof.h#L21-L28 LLVM libc++], [https://github.com/microsoft/STL/blob/1e312b38db8df1dfbea17adc344454feb8d00dd9/stl/inc/type_traits#L1548-L1551 Microsoft STL].

## Notes

`constexpr` for `addressof` is added by `LWG2296`, and MSVC STL applies the change to C++14 mode as a defect report.
There are some weird cases where use of built-in `operator&` is ill-formed due to argument-dependent lookup even if it is not overloaded, and `std::addressof` can be used instead.

```cpp
template<class T>
struct holder { T t; };

struct incomp;

int main()
{
    holder<holder<incomp>*> x{};
    // &x; // error: argument-dependent lookup attempts to instantiate holder<incomp>
    std::addressof(x); // OK
}
```


## Example


### Example

```cpp
#include <iostream>
#include <memory>

template<class T>
struct Ptr
{
    T* pad; // add pad to show difference between 'this' and 'data'
    T* data;
    Ptr(T* arg) : pad(nullptr), data(arg)
    {
        std::cout << "Ctor this = " << this << '\n';
    }

    ~Ptr() { delete data; }
    T** operator&() { return &data; }
};

template<class T>
void f(Ptr<T>* p)
{
    std::cout << "Ptr   overload called with p = " << p << '\n';
}

void f(int** p)
{
    std::cout << "int** overload called with p = " << p << '\n';
}

int main()
{
    Ptr<int> p(new int(42));
    f(&p);                // calls int** overload
    f(std::addressof(p)); // calls Ptr<int>* overload, (= this)
}
```


**Output:**
```
Ctor this = 0x7fff59ae6e88
int** overload called with p = 0x7fff59ae6e90
Ptr   overload called with p = 0x7fff59ae6e88
```


## Defect reports


## See also


| cpp/memory/dsc allocator | (see dedicated page) |
| cpp/memory/pointer_traits/dsc pointer_to | (see dedicated page) |


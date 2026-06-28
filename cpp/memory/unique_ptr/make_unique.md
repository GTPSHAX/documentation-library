---
title: std::make_unique_for_overwrite
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/unique_ptr/make_unique
---


```cpp
**Header:** `<`memory`>`
dcl rev multi|num=1|anchor=1
|since1=c++14|notes1=|dcl1=
template< class T, class... Args >
unique_ptr<T> make_unique( Args&&... args );
|since2=c++23|notes2=|dcl2=
template< class T, class... Args >
constexpr unique_ptr<T> make_unique( Args&&... args );
dcl rev multi|num=2
|since1=c++14|notes1=|dcl1=
template< class T >
unique_ptr<T> make_unique( std::size_t size );
|since2=c++23|notes2=|dcl2=
template< class T >
constexpr unique_ptr<T> make_unique( std::size_t size );
|1=
template< class T, class... Args >
/* unspecified */ make_unique( Args&&... args ) = delete;
dcl rev multi|num=4|anchor=4
|since1=c++20|notes1=|dcl1=
template< class T >
unique_ptr<T> make_unique_for_overwrite();
|since2=c++23|notes2=|dcl2=
template< class T >
constexpr unique_ptr<T> make_unique_for_overwrite();
dcl rev multi|num=5
|since1=c++20|notes1=|dcl1=
template< class T >
unique_ptr<T> make_unique_for_overwrite( std::size_t size );
|since2=c++23|notes2=|dcl2=
template< class T >
constexpr unique_ptr<T> make_unique_for_overwrite( std::size_t size );
|1=
template< class T, class... Args >
/* unspecified */ make_unique_for_overwrite( Args&&... args ) = delete;
```

Constructs an object of type `T` and wraps it in a `std::unique_ptr`.
1. Constructs a non-array type `T`. The arguments `args` are passed to the constructor of `T`. . The function is equivalent to:

```cpp
unique_ptr<T>(new T(std::forward<Args>(args)...))
```

2. Constructs an array of the given dynamic size. The array elements are value-initialized. . The function is equivalent to:

```cpp
unique_ptr<T>(new std::remove_extent_t<T>[size]())
```

@3,6@ Construction of arrays of known bound is disallowed.
4. Same as , except that the object is default-initialized. . The function is equivalent to:

```cpp
unique_ptr<T>(new T)
```

5. Same as , except that the array is default-initialized. . The function is equivalent to:

```cpp
unique_ptr<T>(new std::remove_extent_t<T>[size])
```


## Parameters


### Parameters

- `args` - list of arguments with which an instance of `T` will be constructed
- `size` - the length of the array to construct

## Return value

`std::unique_ptr` of an instance of type `T`.

## Exceptions

May throw `std::bad_alloc` or any exception thrown by the constructor of `T`. If an exception is thrown, this function has no effect.

## Possible Implementation

eq impl
|title1=make_unique |ver1=1|1=
// C++14 make_unique
namespace detail
{
template<class>
constexpr bool is_unbounded_array_v = false;
template<class T>
constexpr bool is_unbounded_array_v<T[]> = true;
template<class>
constexpr bool is_bounded_array_v = false;
template<class T, std::size_t N>
constexpr bool is_bounded_array_v<T[N]> = true;
} // namespace detail
template<class T, class... Args>
std::enable_if_t<!std::is_array<T>::value, std::unique_ptr<T>>
make_unique(Args&&... args)
{
return std::unique_ptr<T>(new T(std::forward<Args>(args)...));
}
template<class T>
std::enable_if_t<detail::is_unbounded_array_v<T>, std::unique_ptr<T>>
make_unique(std::size_t n)
{
return std::unique_ptr<T>(new std::remove_extent_t<T>[n]());
}
template<class T, class... Args>
std::enable_if_t<detail::is_bounded_array_v<T>> make_unique(Args&&...) = delete;
|title2=make_unique_for_overwrite |ver2=4|2=
// C++20 make_unique_for_overwrite
template<class T>
requires (!std::is_array_v<T>)
std::unique_ptr<T> make_unique_for_overwrite()
{
return std::unique_ptr<T>(new T);
}
template<class T>
requires std::is_unbounded_array_v<T>
std::unique_ptr<T> make_unique_for_overwrite(std::size_t n)
{
return std::unique_ptr<T>(new std::remove_extent_t<T>[n]);
}
template<class T, class... Args>
requires std::is_bounded_array_v<T>
void make_unique_for_overwrite(Args&&...) = delete;

## Notes

Unlike `std::make_shared` (which has `std::allocate_shared`), `std::make_unique` does not have an allocator-aware counterpart. `allocate_unique` proposed in `P0211` would be required to invent the deleter type `D` for the `std::unique_ptr<T,D>` it returns which would contain an allocator object and invoke both `destroy` and `deallocate` in its `operator()`.

## Example

> **TODO:** add more `make_unique_for_overwrite()` demos

### Example

```cpp
#include <cstddef>
#include <iomanip>
#include <iostream>
#include <memory>
#include <utility>

struct Vec3
{
    int x, y, z;

    // Following constructor is no longer needed since C++20.
    Vec3(int x = 0, int y = 0, int z = 0) noexcept : x(x), y(y), z(z) {}

    friend std::ostream& operator<<(std::ostream& os, const Vec3& v)
    {
        return os << "{ x=" << v.x << ", y=" << v.y << ", z=" << v.z << " }";
    }
};

// Output Fibonacci numbers to an output iterator.
template<typename OutputIt>
OutputIt fibonacci(OutputIt first, OutputIt last)
{
    for (int a = 0, b = 1; first != last; ++first)
    {
        *first = b;
        b += std::exchange(a, b);
    }
    return first;
}

int main()
{
    // Use the default constructor.
    std::unique_ptr<Vec3> v1 = std::make_unique<Vec3>();
    // Use the constructor that matches these arguments.
    std::unique_ptr<Vec3> v2 = std::make_unique<Vec3>(0, 1, 2);
    // Create a unique_ptr to an array of 5 elements.
    std::unique_ptr<Vec3[]> v3 = std::make_unique<Vec3[]>(5);

    // Create a unique_ptr to an uninitialized array of 10 integers,
    // then populate it with Fibonacci numbers.
    std::unique_ptr<int[]> i1 = std::make_unique_for_overwrite<int[]>(10);
    fibonacci(i1.get(), i1.get() + 10);

    std::cout << "make_unique<Vec3>():      " << *v1 << '\n'
              << "make_unique<Vec3>(0,1,2): " << *v2 << '\n'
              << "make_unique<Vec3[]>(5):   ";
    for (std::size_t i = 0; i < 5; ++i)
        std::cout << std::setw(i ? 30 : 0) << v3[i] << '\n';
    std::cout << '\n';

    std::cout << "make_unique_for_overwrite<int[]>(10), fibonacci(...): [" << i1[0];
    for (std::size_t i = 1; i < 10; ++i)
        std::cout << ", " << i1[i];
    std::cout << "]\n";
}
```


**Output:**
```
make_unique<Vec3>():      { x=0, y=0, z=0 }
make_unique<Vec3>(0,1,2): { x=0, y=1, z=2 }
make_unique<Vec3[]>(5):   { x=0, y=0, z=0 }
                          { x=0, y=0, z=0 }
                          { x=0, y=0, z=0 }
                          { x=0, y=0, z=0 }
                          { x=0, y=0, z=0 }

make_unique_for_overwrite<int[]>(10), fibonacci(...): [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```


## See also


| cpp/memory/unique_ptr/dsc constructor | (see dedicated page) |
| cpp/memory/shared_ptr/dsc make_shared | (see dedicated page) |


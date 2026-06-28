---
title: std::allocate_shared_for_overwrite
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/shared_ptr/allocate_shared
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++11|constexpr=c++26|
template< class T, class Alloc, class... Args >
shared_ptr<T> allocate_shared( const Alloc& alloc, Args&&... args );
dcla|num=2|since=c++20|constexpr=c++26|
template< class T, class Alloc >
shared_ptr<T> allocate_shared( const Alloc& alloc, std::size_t N );
dcla|num=3|since=c++20|constexpr=c++26|
template< class T, class Alloc >
shared_ptr<T> allocate_shared( const Alloc& alloc );
dcla|num=4|since=c++20|constexpr=c++26|
template< class T, class Alloc >
shared_ptr<T> allocate_shared( const Alloc& alloc, std::size_t N,
const std::remove_extent_t<T>& u );
dcla|num=5|since=c++20|constexpr=c++26|
template< class T, class Alloc >
shared_ptr<T> allocate_shared( const Alloc& alloc,
const std::remove_extent_t<T>& u );
dcla|num=6|since=c++20|constexpr=c++26|
template< class T, class Alloc >
shared_ptr<T> allocate_shared_for_overwrite( const Alloc& alloc );
dcla|num=7|since=c++20|constexpr=c++26|
template< class T, class Alloc >
shared_ptr<T> allocate_shared_for_overwrite( const Alloc& alloc,
std::size_t N );
```

Allocates memory for an object using a copy of `alloc` (rebound for an unspecified `value_type`) and initialize the object with the supplied arguments. Returns a `std::shared_ptr` object managing the newly created object.
1. The object is of type `T`, and is constructed as if by , where `pt` is a `std::remove_cv_t<T>*` pointer to storage suitable to hold an object of type `std::remove_cv_t<T>`. If the object is to be destroyed, it is destroyed as if by `std::allocator_traits<Alloc>::destroy(a, pt)`, where `pt` is a pointer to that object of type `std::remove_cv_t<T>`.
@@ In the description above, `a` is of type `Alloc`, and it is a potentially rebound copy of `alloc`.
rrev|since=c++20|
.
2. The object is of type `std::remove_extent_t<T>[N]`. Each element has a default initial value.
@@ .
3. The object is of type `T`. Each element has a default initial value.
@@ .
4. The object is of type `std::remove_extent_t<T>[N]`. Each element has the initial value `u`.
@@ .
5. The object is of type `T`. Each element has the initial value `u`.
@@ .
6. The object is of type `T`.
* If `T` is not an array type, the object is constructed as if by `::new (pv) T`, where `pv` is a `void*` pointer to storage suitable to hold an object of type `T`. If the object is to be destroyed, it is destroyed as if by `pt->~T()`, where `pt` is a pointer to that object of type `T`.
* If `T` is a bounded array type, the initial value is unspecified for each element.
@@ .
7. The object is of type `std::remove_extent_t<T>[N]`. The initial value is unspecified for each element.
@@ .
rrev|since=c++20|

### Initializing and destroying array elements

In the description below, `a` is of type `Alloc`, and it is a potentially rebound copy of `alloc`.
Array elements of type `U` are initialized in ascending order of their addresses.
* If `U` is not an array type, each element is constructed as if by the following expression, where `pu` is a `std::remove_cv_t<U>*` pointer to storage suitable to hold an object of type `std::remove_cv_t<U>`, and `pv` is a `void*` pointer to storage suitable to hold an object of type `U`:
@2,3@ `std::allocator_traits<Alloc>::construct(a, pu)`
@4,5@ `std::allocator_traits<Alloc>::construct(a, pu, u)`
@6,7@ `::new (pv) U`
* Otherwise, recursively initializes the elements of each element. For the next dimension:
:* `U` becomes `std::remove_extent_t<U>`.
:* For overloads , `u` becomes the corresponding element of `u`.
When the lifetime of the object managed by the return `std::shared_ptr` ends, or when the initialization of an array element throws an exception, the initialized elements are destroyed in the reverse order of their original construction.
For each array element of non-array type `U` to be destroyed, it is destroyed as if by the following expression:
@2-5@ `std::allocator_traits<Alloc>::destroy(a, pu)`, where `pu` is a `U*` pointer to that array element of type `U`
@6,7@ `pu->~U()`, where `pu` is a pointer to that array element of type `U`

## Parameters


### Parameters

- `alloc` - the *Allocator* to use
- `args...` - list of arguments with which an instance of `T` will be constructed
- `N` - array size to use
- `u` - the initial value to initialize every element of the array

## Return value

`std::shared_ptr` to an object of type `T`<sup>(since C++20)</sup>  or `std::remove_extent_t<T>[N]` if `T` is an unbounded array type.
For the returned `std::shared_ptr` `r`, `r.get()` returns a non-null pointer and `r.use_count()` returns `1`.

## Exceptions

Can throw the exceptions thrown from `Alloc::allocate()` or from the constructor of `T`. If an exception is thrown,  has no effect. <sup>(since C++20)</sup> If an exception is thrown during the construction of the array, already-initialized elements are destroyed in reverse order.

## Notes

These functions will typically allocate more memory than `sizeof(T)` to allow for internal bookkeeping structures such as reference counts.
Like `std::make_shared`, this function typically performs only one allocation, and places both the `T` object and the control block in the allocated memory block (the standard recommends but does not require this, all known implementations do this). A copy of `alloc` is stored as part of the control block so that it can be used to deallocate it once both shared and weak reference counts reach zero.
Unlike the `std::shared_ptr` `constructors`, `std::allocate_shared` does not accept a separate custom deleter: the supplied allocator is used for destruction of the control block and the `T` object, and for deallocation of their shared memory block.
rrev|until=c++20|
`std::shared_ptr` supports array types (as of C++17), but `std::allocate_shared` does not. This functionality is supported by [https://www.boost.org/doc/libs/1_66_0/libs/smart_ptr/doc/html/smart_ptr.html#make_shared `boost::allocate_shared`].

## Example


### Example

```cpp
#include <cstddef>
#include <iostream>
#include <memory>
#include <memory_resource>
#include <vector>

class Value
{
    int i;
public:
    Value(int i) : i(i) { std::cout << "Value(), i = " << i << '\n'; }
    ~Value() { std::cout << "~Value(), i = " << i << '\n'; }
    void print() const { std::cout << "i = " << i << '\n'; }
};

int main()
{
    // Create a polymorphic allocator using the monotonic buffer resource
    std::byte buffer[sizeof(Value) * 8];
    std::pmr::monotonic_buffer_resource resource(buffer, sizeof(buffer));
    std::pmr::polymorphic_allocator<Value> allocator(&resource);

    std::vector<std::shared_ptr<Value>> v;

    for (int i{}; i != 4; ++i)
        // Use std::allocate_shared with the custom allocator
        v.emplace_back(std::allocate_shared<Value>(allocator, i));

    for (const auto& sp : v)
        sp->print();
} //< All shared pointers will automatically clean up when they go out of scope.
```


**Output:**
```
Value(), i = 0
Value(), i = 1
Value(), i = 2
Value(), i = 3
i = 0
i = 1
i = 2
i = 3
~Value(), i = 0
~Value(), i = 1
~Value(), i = 2
~Value(), i = 3
```


## Defect reports


## See also


| cpp/memory/shared_ptr/dsc constructor | (see dedicated page) |
| cpp/memory/shared_ptr/dsc make_shared | (see dedicated page) |


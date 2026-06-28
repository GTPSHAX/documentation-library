---
title: std::shared_ptr::shared_ptr
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/shared_ptr/shared_ptr
---


```cpp
dcl|num=1|
constexpr shared_ptr() noexcept;
dcl|num=2|
constexpr shared_ptr( std::nullptr_t ) noexcept;
dcla|num=3|constexpr=c++26|
template< class Y >
explicit shared_ptr( Y* ptr );
dcla|num=4|constexpr=c++26|
template< class Y, class Deleter >
shared_ptr( Y* ptr, Deleter d );
dcla|num=5|constexpr=c++26|
template< class Deleter >
shared_ptr( std::nullptr_t ptr, Deleter d );
dcla|num=6|constexpr=c++26|
template< class Y, class Deleter, class Alloc >
shared_ptr( Y* ptr, Deleter d, Alloc alloc );
dcla|num=7|constexpr=c++26|
template< class Deleter, class Alloc >
shared_ptr( std::nullptr_t ptr, Deleter d, Alloc alloc );
dcla|num=8|constexpr=c++26|
template< class Y >
shared_ptr( const shared_ptr<Y>& r, element_type* ptr ) noexcept;
dcla|num=9|since=c++20|constexpr=c++26|
template< class Y >
shared_ptr( shared_ptr<Y>&& r, element_type* ptr ) noexcept;
dcla|num=10|constexpr=c++26|
shared_ptr( const shared_ptr& r ) noexcept;
dcla|num=11|constexpr=c++26|
template< class Y >
shared_ptr( const shared_ptr<Y>& r ) noexcept;
dcla|num=12|constexpr=c++26|
shared_ptr( shared_ptr&& r ) noexcept;
dcla|num=13|constexpr=c++26|
template< class Y >
shared_ptr( shared_ptr<Y>&& r ) noexcept;
dcla|num=14|constexpr=c++26|
template< class Y >
explicit shared_ptr( const std::weak_ptr<Y>& r );
dcl|num=15|removed=c++17|
template< class Y >
shared_ptr( std::auto_ptr<Y>&& r );
dcla|num=16|constexpr=c++26|
template< class Y, class Deleter >
shared_ptr( std::unique_ptr<Y, Deleter>&& r );
```

Constructs new `shared_ptr` from a variety of pointer types that refer to an object to manage.
rrev|since=c++17|
For the purposes of the description below, a pointer type `Y*` is said to be ''compatible with'' a pointer type `T*` if either `Y*` is convertible to `T*` or `Y` is the array type `U[N]` and `T` is `U cv []` (where cv is some set of cv-qualifiers).
@1,2@ Constructs a `shared_ptr` with no managed object, i.e. empty `shared_ptr`.
@3-7@ Constructs a `shared_ptr` with `ptr` as the pointer to the managed object.
cpp/rev
|until c++17=For , `Y*` must be convertible to `T*`.
|since c++17=If `T` is an array type `U[N]`,  do not participate in overload resolution if `Y(*)[N]` is an invalid type or not convertible to `T*`. If `T` is an array type `U[]`,  do not participate in overload resolution if `Y(*)[]` is an invalid type or not convertible to `T*`. Otherwise,  do not participate in overload resolution if `Y*` is not convertible to `T*`.
:@3@ Uses the `delete` expression `delete ptr` <sup>(since C++17)</sup>  if `T` is not an array type; `delete[] ptr` if `T` is an array type as the deleter. `Y` must be a complete type. The `delete` expression must be well-formed, have well-defined behavior and not throw any exceptions. <sup>(since C++17)</sup> This constructor additionally does not participate in overload resolution if the `delete` expression is not well-formed.
:@4,5@ Uses the specified deleter `d` as the deleter. The expression `d(ptr)` must be well formed, have well-defined behavior and not throw any exceptions. The construction of `d` and of the stored deleter copied from it must not throw exceptions.
cpp/rev
|until c++17=`Deleter` must be *CopyConstructible*.
|since c++17=These constructors additionally do not participate in overload resolution if the expression `d(ptr)` is not well-formed, or if `std::is_move_constructible_v<D>` is `false`.
:@6,7@  Same as , but additionally uses a copy of `alloc` for allocation of data for internal use. `Alloc` must be an *Allocator*.
@8,9@ The ''aliasing constructor'': constructs a `shared_ptr` which shares ownership information with the initial value of `r`, but holds an unrelated and unmanaged pointer `ptr`. If this `shared_ptr` is the last of the group to go out of scope, it will call the stored deleter for the object originally managed by `r`. However, calling `get()` on this `shared_ptr` will always return a copy of `ptr`. It is the responsibility of the programmer to make sure that this `ptr` remains valid as long as this shared_ptr exists, such as in the typical use cases where `ptr` is a member of the object managed by `r` or is an alias (e.g., downcast) of `r.get()`.
:@9@ `r` is empty and `r.get()  after the call.
@10,11@ Constructs a `shared_ptr` which shares ownership of the object managed by `r`. If `r` manages no object, `*this` manages no object either. The template overload doesn't participate in overload resolution if `Y*` is not <sup>(until C++17)</sup> implicitly convertible to<sup>(since C++17)</sup> ''compatible with'' `T*`.
@12,13@ Move-constructs a `shared_ptr` from `r`. After the construction, `*this` contains a copy of the previous state of `r`, `r` is empty and its stored pointer is null. The template overload doesn't participate in overload resolution if `Y*` is not <sup>(until C++17)</sup> implicitly convertible to<sup>(since C++17)</sup> ''compatible with'' `T*`.
14. Constructs a `shared_ptr` which shares ownership of the object managed by `r`. <sup>(until C++17)</sup> `Y*` must be implicitly convertible to `T*`.<sup>(since C++17)</sup>  Note that `r.lock()` may be used for the same purpose: the difference is that this constructor throws an exception if the argument is empty, while `std::weak_ptr<T>::lock()` constructs an empty `std::shared_ptr` in that case.
15. Constructs a `shared_ptr` that stores and owns the object formerly owned by `r`. `Y*` must be convertible to `T*`. After construction, `r` is empty.
16. Constructs a `shared_ptr` which manages the object currently managed by `r`. The deleter associated with `r` is stored for future deletion of the managed object. `r` manages no object after the call. rev|since=c++17|This overload doesn't participate in overload resolution if `std::unique_ptr<Y, Deleter>::pointer` is not ''compatible with'' `T*`.
If `r.get()` is a null pointer, this overload is equivalent to the default constructor . If `Deleter` is a reference type, it is equivalent to `shared_ptr(r.release(), std::ref(r.get_deleter())`. Otherwise, it is equivalent to `shared_ptr(r.release(), std::move(r.get_deleter()))`.
When `T` is not an array type, the overloads  enable `shared_from_this` with `ptr`, and the overload  enables `shared_from_this` with the pointer returned by `r.release()`.

## Parameters


### Parameters

- `ptr` - a pointer to an object to manage
- `d` - a deleter to use to destroy the object
- `alloc` - an allocator to use for allocations of data for internal use
- `r` - another smart pointer to share the ownership to or acquire the ownership from

## Exceptions

3. `std::bad_alloc` if required additional memory could not be obtained. May throw implementation-defined exception for other errors. If an exception occurs, this calls `delete ptr`<sup>(since C++17)</sup>  if `T` is not an array type, and calls `delete[] ptr` otherwise.
@4-7@ `std::bad_alloc` if required additional memory could not be obtained. May throw implementation-defined exception for other errors. `d(ptr)` is called if an exception occurs.
14. `std::bad_weak_ptr` if `r.expired() . The constructor has no effect in this case.
15. `std::bad_alloc` if required additional memory could not be obtained. May throw implementation-defined exception for other errors. This constructor has no effect if an exception occurs.
16. If an exception is thrown, the constructor has no effects.

## Notes

The raw pointer overloads assume ownership of the pointed-to object. Therefore, constructing a `shared_ptr` using the raw pointer overload for an object that is already managed by a `shared_ptr`, such as by `shared_ptr(ptr.get())` is likely to lead to undefined behavior, even if the object is of a type derived from `std::enable_shared_from_this`.
Because the default constructor is `constexpr`, static shared_ptrs are initialized as part of static non-local initialization, before any dynamic non-local initialization begins. This makes it safe to use a shared_ptr in a constructor of any static object.
In C++11 and C++14 it is valid to construct a `std::shared_ptr<T>` from a `std::unique_ptr<T[]>`:

```cpp
std::unique_ptr<int[]> arr(new int[1]);
std::shared_ptr<int> ptr(std::move(arr));
```

Since the `shared_ptr` obtains its deleter (a `std::default_delete<T[]>` object) from the `std::unique_ptr`, the array will be correctly deallocated. This is no longer allowed in C++17. Instead the array form `std::shared_ptr<T[]>` should be used.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

struct Foo
{
    int id{0};
    Foo(int i = 0) : id{i} { std::cout << "Foo::Foo(" << i <<  ")\n"; }
    ~Foo() { std::cout << "Foo::~Foo(), id=" << id << '\n'; }
};

struct D
{
    void operator()(Foo* p) const
    {
        std::cout << "Call delete from function object. Foo::id=" << p->id << '\n';
        delete p;
    }
};

int main()
{
    {
        std::cout << "1) constructor with no managed object\n";
        std::shared_ptr<Foo> sh1;
    }

    {
        std::cout << "2) constructor with object\n";
        std::shared_ptr<Foo> sh2(new Foo{10});
        std::cout << "sh2.use_count(): " << sh2.use_count() << '\n';
        std::shared_ptr<Foo> sh3(sh2);
        std::cout << "sh2.use_count(): " << sh2.use_count() << '\n';
        std::cout << "sh3.use_count(): " << sh3.use_count() << '\n';
    }

    {
        std::cout << "3) constructor with object and deleter\n";
        std::shared_ptr<Foo> sh4(new Foo{11}, D());
        std::shared_ptr<Foo> sh5(new Foo{12}, [](auto p)
        {
            std::cout << "Call delete from lambda... p->id=" << p->id << '\n';
            delete p;
        });
    }
}
```


**Output:**
```
1) constructor with no managed object
2) constructor with object
Foo::Foo(10)
sh2.use_count(): 1
sh2.use_count(): 2
sh3.use_count(): 2
Foo::~Foo(), id=10
3) constructor with object and deleter
Foo::Foo(11)
Foo::Foo(12)
Call delete from lambda... p->id=12
Foo::~Foo(), id=12
Call delete from function object. Foo::id=11
Foo::~Foo(), id=11
```


## Defect reports


## See also


| cpp/memory/shared_ptr/dsc make_shared | (see dedicated page) |
| cpp/memory/shared_ptr/dsc allocate_shared | (see dedicated page) |
| cpp/memory/dsc enable_shared_from_this | (see dedicated page) |


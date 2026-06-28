---
title: std::make_shared_for_overwrite
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/shared_ptr/make_shared
---


```cpp
**Header:** `<`memory`>`
dcla|num=1|since=c++11|constexpr=c++26|
template< class T, class... Args >
shared_ptr<T> make_shared( Args&&... args );
dcla|num=2|since=c++20|constexpr=c++26|
template< class T >
shared_ptr<T> make_shared( std::size_t N );
dcla|num=3|since=c++20|constexpr=c++26|
template< class T >
shared_ptr<T> make_shared();
dcla|num=4|since=c++20|constexpr=c++26|
template< class T >
shared_ptr<T> make_shared( std::size_t N, const std::remove_extent_t<T>& u );
dcla|num=5|since=c++20|constexpr=c++26|
template< class T >
shared_ptr<T> make_shared( const std::remove_extent_t<T>& u );
dcla|num=6|since=c++20|constexpr=c++26|
template< class T >
shared_ptr<T> make_shared_for_overwrite();
dcla|num=7|since=c++20|constexpr=c++26|
template< class T >
shared_ptr<T> make_shared_for_overwrite( std::size_t N );
```

Allocates memory for an object and initialize the object with the supplied arguments. Returns a `std::shared_ptr` object managing the newly created object.
1. The object is of type `T`, and is constructed as if by `::new (pv) T(std::forward<Args>(args)...)`, where `pv` is a `void*` pointer to storage suitable to hold an object of type `T`. If the object is to be destroyed, it is destroyed as if by `pt->~T()`, where `pt` is a pointer to that object of type `T`.
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

Array elements of type `U` are initialized in ascending order of their addresses.
* If `U` is not an array type, each element is constructed as if by the following expression, where `pv` is a `void*` pointer to storage suitable to hold an object of type `U`:
@2,3@ `::new (pv) U()`
@4,5@ `::new (pv) U(u)`
@6,7@ `::new (pv) U`
* Otherwise, recursively initializes the elements of each element. For the next dimension:
:* `U` becomes `std::remove_extent_t<U>`.
:* For overloads , `u` becomes the corresponding element of `u`.
When the lifetime of the object managed by the return `std::shared_ptr` ends, or when the initialization of an array element throws an exception, the initialized elements are destroyed in the reverse order of their original construction.
For each array element of non-array type `U` to be destroyed, it is destroyed as if by `pu->~U()`, where `pu` is a pointer to that array element of type `U`.

## Parameters


### Parameters

- `args` - list of arguments with which an object of `T` will be constructed
- `N` - array size to use
- `u` - the initial value to initialize every element of the array

## Return value

`std::shared_ptr` to an object of type `T`<sup>(since C++20)</sup>  or `std::remove_extent_t<T>[N]` if `T` is an unbounded array type.
For the returned `std::shared_ptr` `r`, `r.get()` returns a non-null pointer and `r.use_count()` returns `1`.

## Exceptions

May throw `std::bad_alloc` or any exception thrown by the constructor of `T`. If an exception is thrown, the functions have no effect.<sup>(since C++20)</sup>  If an exception is thrown during the construction of the array, already-initialized elements are destroyed in reverse order.

## Notes

These functions will typically allocate more memory than `sizeof(T)` to allow for internal bookkeeping structures such as reference counts.
These functions may be used as an alternative to `std::shared_ptr<T>(new T(args...))`. The trade-offs are:
* `std::shared_ptr<T>(new T(args...))` performs at least two allocations (one for the object `T` and one for the control block of the shared pointer), while `std::make_shared<T>` typically performs only one allocation (the standard recommends, but does not require this; all known implementations do this).
* If any `std::weak_ptr` references the control block created by `std::make_shared` after the lifetime of all shared owners ended, the memory occupied by `T` persists until all weak owners get destroyed as well, which may be undesirable if `sizeof(T)` is large.
* `std::shared_ptr<T>(new T(args...))` may call a non-public constructor of `T` if executed in context where it is accessible, while `std::make_shared` requires public access to the selected constructor.
* Unlike the `std::shared_ptr` constructors, `std::make_shared` does not allow a custom deleter.
* `std::make_shared` uses `::new`, so if any special behavior has been set up using a class-specific `cpp/memory/new/operator new`, it will differ from `std::shared_ptr<T>(new T(args...))`.
rrev|until=c++20|* `std::shared_ptr` supports array types (as of C++17), but `std::make_shared` does not. This functionality is supported by [https://www.boost.org/doc/libs/1_66_0/libs/smart_ptr/doc/html/smart_ptr.html#make_shared `boost::make_shared`].

## Example


### Example

```cpp
#include <iostream>
#include <memory>
#include <type_traits>
#include <vector>

struct C
{
    // constructors needed (until C++20)
    C(int i) : i(i) {}
    C(int i, float f) : i(i), f(f) {}
    int i;
    float f{};
};

int main()
{
    // using “auto” for the type of “sp1”
    auto sp1 = std::make_shared<C>(1); // overload (1)
    static_assert(std::is_same_v<decltype(sp1), std::shared_ptr<C>>);
    std::cout << "sp1->{ i:" << sp1->i << ", f:" << sp1->f << " }\n";

    // being explicit with the type of “sp2”
    std::shared_ptr<C> sp2 = std::make_shared<C>(2, 3.0f); // overload (1)
    static_assert(std::is_same_v<decltype(sp2), std::shared_ptr<C>>);
    static_assert(std::is_same_v<decltype(sp1), decltype(sp2)>);
    std::cout << "sp2->{ i:" << sp2->i << ", f:" << sp2->f << " }\n";

    // shared_ptr to a value-initialized float[64]; overload (2):
    std::shared_ptr<float[]> sp3 = std::make_shared<float[]>(64);

    // shared_ptr to a value-initialized long[5][3][4]; overload (2):
    std::shared_ptr<long[][3][4]> sp4 = std::make_shared<long[][3][4]>(5);

    // shared_ptr to a value-initialized short[128]; overload (3):
    std::shared_ptr<short[128]> sp5 = std::make_shared<short[128]>();

    // shared_ptr to a value-initialized int[7][6][5]; overload (3):
    std::shared_ptr<int[7][6][5]> sp6 = std::make_shared<int[7][6][5]>();

    // shared_ptr to a double[256], where each element is 2.0; overload (4):
    std::shared_ptr<double[]> sp7 = std::make_shared<double[]>(256, 2.0);

    // shared_ptr to a double[7][2], where each double[2]
    // element is {3.0, 4.0}; overload (4):
    std::shared_ptr<double[][2]> sp8 = std::make_shared<double[][2]>(7, {3.0, 4.0});

    // shared_ptr to a vector<int>[4], where each vector
    // has contents {5, 6}; overload (4):
    std::shared_ptr<std::vector<int>[]> sp9 =
        std::make_shared<std::vector<int>[]>(4, {5, 6});

    // shared_ptr to a float[512], where each element is 1.0; overload (5):
    std::shared_ptr<float[512]> spA = std::make_shared<float[512]>(1.0);

    // shared_ptr to a double[6][2], where each double[2] element
    // is {1.0, 2.0}; overload (5):
    std::shared_ptr<double[6][2]> spB = std::make_shared<double[6][2]>({1.0, 2.0});

    // shared_ptr to a vector<int>[4], where each vector
    // has contents {5, 6}; overload (5):
    std::shared_ptr<std::vector<int>[4]> spC =
        std::make_shared<std::vector<int>[4]>({5, 6});
}
```


**Output:**
```
sp1->{ i:1, f:0 }
sp2->{ i:2, f:3 }
```


## Defect reports


## See also


| cpp/memory/shared_ptr/dsc constructor | (see dedicated page) |
| cpp/memory/shared_ptr/dsc allocate_shared | (see dedicated page) |
| cpp/memory/dsc enable_shared_from_this | (see dedicated page) |
| cpp/memory/unique_ptr/dsc make_unique | (see dedicated page) |
| cpp/memory/new/dsc operator_new | (see dedicated page) |


---
title: std::unique_ptr
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/unique_ptr
---


```cpp
**Header:** `<`memory`>`
dcl|since=c++11|num=1|1=
template<
class T,
class Deleter = std::default_delete<T>
> class unique_ptr;
dcl|since=c++11|num=2|1=
template <
class T,
class Deleter
> class unique_ptr<T[], Deleter>;
```

`std::unique_ptr` is a smart pointer that owns (is responsible for) and manages another object via a pointer and subsequently disposes of that object when the `unique_ptr` goes out of scope.
The object is disposed of, using the associated deleter, when either of the following happens:
* the managing `unique_ptr` object is destroyed.
* the managing `unique_ptr` object is assigned another pointer via `1=operator=` or `reset()`.
The object is disposed of, using a potentially user-supplied deleter, by calling `get_deleter()(ptr)`. The default deleter (`std::default_delete`) uses the `delete` operator, which destroys the object and deallocates the memory.
A `unique_ptr` may alternatively own no object, in which case it is described as ''empty''.
There are two versions of `unique_ptr`:
# Manages a single object (e.g., allocated with `new`).
# Manages a dynamically-allocated array of objects (e.g., allocated with `new[]`).
The class satisfies the requirements of *MoveConstructible* and *MoveAssignable*, but of neither *CopyConstructible* nor *CopyAssignable*.
If `T*` was not a valid type (e.g., `T` is a reference type), a program that instantiates the definition of `std::unique_ptr<T, Deleter>` is ill-formed.

### Parameters


**Type requirements:**


## Notes

Only non-const `unique_ptr` can transfer the ownership of the managed object to another `unique_ptr`. If an object's lifetime is managed by a `const std::unique_ptr`, it is limited to the scope in which the pointer was created.
`unique_ptr` is commonly used to manage the lifetime of objects, including:
* providing exception safety to classes and functions that handle objects with dynamic lifetime, by guaranteeing deletion on both normal exit and exit through exception.
* passing ownership of uniquely-owned objects with dynamic lifetime into functions.
* acquiring ownership of uniquely-owned objects with dynamic lifetime from functions.
* as the element type in move-aware containers, such as `std::vector`, which hold pointers to dynamically-allocated objects (e.g. if polymorphic behavior is desired).
`unique_ptr` may be constructed for an  `T`, such as to facilitate the use as a handle in the pImpl idiom. If the default deleter is used, `T` must be complete at the point in code where the deleter is invoked, which happens in the destructor, move assignment operator, and `reset` member function of `unique_ptr`. (In contrast, `std::shared_ptr` cannot be constructed from a raw pointer to incomplete type, but can be destroyed where `T` is incomplete). Note that if `T` is a class template specialization, use of `unique_ptr` as an operand, e.g. `!p` requires `T`'s parameters to be complete due to ADL.
If `T` is a  of some base `B`, then `unique_ptr<T>` is  to `unique_ptr<B>`. The default deleter of the resulting `unique_ptr<B>` will use `cpp/memory/new/operator delete` for `B`, leading to undefined behavior unless the destructor of `B` is . Note that `std::shared_ptr` behaves differently: `std::shared_ptr<B>` will use the `cpp/memory/new/operator delete` for the type `T` and the owned object will be deleted correctly even if the destructor of `B` is not .
Unlike `std::shared_ptr`, `unique_ptr` may manage an object through any custom handle type that satisfies *NullablePointer*. This allows, for example, managing objects located in shared memory, by supplying a `Deleter` that defines `typedef [https://www.boost.org/doc/libs/release/doc/html/boost/interprocess/offset_ptr.html boost::offset_ptr] pointer;` or another fancy pointer.

## Nested types


| Item | Description |
|------|-------------|
| **Type** | Definition |


## Member functions


| cpp/memory/unique_ptr/dsc constructor | (see dedicated page) |
| cpp/memory/unique_ptr/dsc destructor | (see dedicated page) |
| cpp/memory/unique_ptr/dsc operator{{= | (see dedicated page) |

#### Modifiers

| cpp/memory/unique_ptr/dsc release | (see dedicated page) |
| cpp/memory/unique_ptr/dsc reset | (see dedicated page) |
| cpp/memory/unique_ptr/dsc swap | (see dedicated page) |

#### Observers

| cpp/memory/unique_ptr/dsc get | (see dedicated page) |
| cpp/memory/unique_ptr/dsc get_deleter | (see dedicated page) |
| cpp/memory/unique_ptr/dsc operator bool | (see dedicated page) |

#### Single-object version, {{tt|unique_ptr<T>

| cpp/memory/unique_ptr/dsc operator* | (see dedicated page) |

#### Array version, {{tt|unique_ptr<T[]>

| cpp/memory/unique_ptr/dsc operator at | (see dedicated page) |


## Non-member functions


| cpp/memory/unique_ptr/dsc make_unique | (see dedicated page) |
| cpp/memory/unique_ptr/dsc operator cmp | (see dedicated page) |
| cpp/memory/unique_ptr/dsc operator ltlt | (see dedicated page) |
| cpp/memory/unique_ptr/dsc swap2 | (see dedicated page) |


## Helper classes


| cpp/memory/unique_ptr/dsc hash | (see dedicated page) |


## Example


### Example

```cpp
#include <cassert>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <locale>
#include <memory>
#include <stdexcept>

// helper class for runtime polymorphism demo below
struct B
{
    virtual ~B() = default;

    virtual void bar() { std::cout << "B::bar\n"; }
};

struct D : B
{
    D() { std::cout << "D::D\n"; }
    ~D() { std::cout << "D::~D\n"; }

    void bar() override { std::cout << "D::bar\n"; }
};

// a function consuming a unique_ptr can take it by value or by rvalue reference
std::unique_ptr<D> pass_through(std::unique_ptr<D> p)
{
    p->bar();
    return p;
}

// helper function for the custom deleter demo below
void close_file(std::FILE* fp)
{
    std::fclose(fp);
}

// unique_ptr-based linked list demo
struct List
{
    struct Node
    {
        int data;
        std::unique_ptr<Node> next;
    };

    std::unique_ptr<Node> head;

    ~List()
    {
        // destroy list nodes sequentially in a loop, the default destructor
        // would have invoked its “next”'s destructor recursively, which would
        // cause stack overflow for sufficiently large lists.
        while (head)
        {
            auto next = std::move(head->next);
            head = std::move(next);
        }
    }

    void push(int data)
    {
        head = std::unique_ptr<Node>(new Node{data, std::move(head)});
    }
};

int main()
{
    std::cout << "1) Unique ownership semantics demo\n";
    {
        // Create a (uniquely owned) resource
        std::unique_ptr<D> p = std::make_unique<D>();

        // Transfer ownership to “pass_through”,
        // which in turn transfers ownership back through the return value
        std::unique_ptr<D> q = pass_through(std::move(p));

        // “p” is now in a moved-from 'empty' state, equal to nullptr
        assert(!p);
    }

    std::cout << "\n" "2) Runtime polymorphism demo\n";
    {
        // Create a derived resource and point to it via base type
        std::unique_ptr<B> p = std::make_unique<D>();

        // Dynamic dispatch works as expected
        p->bar();
    }

    std::cout << "\n" "3) Custom deleter demo\n";
    std::ofstream("demo.txt") << 'x'; // prepare the file to read
    {
        using unique_file_t = std::unique_ptr<std::FILE, decltype(&close_file)>;
        unique_file_t fp(std::fopen("demo.txt", "r"), &close_file);
        if (fp)
            std::cout << char(std::fgetc(fp.get())) << '\n';
    } // “close_file()” called here (if “fp” is not null)

    std::cout << "\n" "4) Custom lambda expression deleter and exception safety demo\n";
    try
    {
        std::unique_ptr<D, void(*)(D*)> p(new D, [](D* ptr)
        {
            std::cout << "destroying from a custom deleter...\n";
            delete ptr;
        });

        throw std::runtime_error(""); // “p” would leak here if it were a plain pointer
    }
    catch (const std::exception&)
    {
        std::cout << "Caught exception\n";
    }

    std::cout << "\n" "5) Array form of unique_ptr demo\n";
    {
        std::unique_ptr<D[]> p(new D[3]);
    } // “D::~D()” is called 3 times

    std::cout << "\n" "6) Linked list demo\n";
    {
        List wall;
        const int enough{1'000'000};
        for (int beer = 0; beer != enough; ++beer)
            wall.push(beer);

        std::cout.imbue(std::locale("en_US.UTF-8"));
        std::cout << enough << " bottles of beer on the wall...\n";
    } // destroys all the beers
}
```


**Output:**
```
1) Unique ownership semantics demo
D::D
D::bar
D::~D

2) Runtime polymorphism demo
D::D
D::bar
D::~D

3) Custom deleter demo
x

4) Custom lambda-expression deleter and exception safety demo
D::D
destroying from a custom deleter...
D::~D
Caught exception

5) Array form of unique_ptr demo
D::D
D::D
D::D
D::~D
D::~D
D::~D

6) Linked list demo
1,000,000 bottles of beer on the wall...
```


## Defect reports


## See also


| cpp/memory/dsc shared_ptr | (see dedicated page) |
| cpp/memory/dsc weak_ptr | (see dedicated page) |
| cpp/memory/dsc indirect | (see dedicated page) |
| cpp/utility/dsc any | (see dedicated page) |


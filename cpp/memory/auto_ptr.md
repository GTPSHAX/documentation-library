---
title: std::auto_ptr
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/auto_ptr
---


```cpp
**Header:** `<`memory`>`
dcl|until=c++17|deprecated=c++11|num=1|1=
template< class T > class auto_ptr;
dcl|until=c++17|deprecated=c++11|num=2|1=
template<> class auto_ptr<void>;
```

`auto_ptr` is a smart pointer that manages an object obtained via new expression and deletes that object when `auto_ptr` itself is destroyed. It may be used to provide exception safety for dynamically allocated objects, for passing ownership of dynamically allocated objects into functions and for returning dynamically allocated objects from functions.
Copying an `auto_ptr` copies the pointer and transfers ownership to the destination: both copy construction and copy assignment of `auto_ptr` modify their right-hand arguments, and the "copy" is not equal to the original. Because of these unusual copy semantics, `auto_ptr` may not be placed in standard containers. <sup>(since C++11)</sup> `std::unique_ptr` is preferred for this and other uses.
2. Specialization for type `void` is provided, it declares the typedef `element_type`, but no member functions.
An additional class template `auto_ptr_ref` is referred to throughout the documentation. It is an implementation-defined type that holds a reference to `auto_ptr`. The implementation is allowed to provide the template with a different name or implement the functions returning it or accepting it as parameter in other ways.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |


## Member functions


| cpp/memory/auto_ptr/dsc auto_ptr | (see dedicated page) |
| cpp/memory/auto_ptr/dsc ~auto_ptr | (see dedicated page) |
| cpp/memory/auto_ptr/dsc operator{{= | (see dedicated page) |
| cpp/memory/auto_ptr/dsc operator_auto_ptr | (see dedicated page) |

#### Observers

| cpp/memory/auto_ptr/dsc get | (see dedicated page) |
| cpp/memory/auto_ptr/dsc operator* | (see dedicated page) |

#### Modifiers

| cpp/memory/auto_ptr/dsc reset | (see dedicated page) |
| cpp/memory/auto_ptr/dsc release | (see dedicated page) |


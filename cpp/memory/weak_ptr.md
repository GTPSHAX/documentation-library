---
title: std::weak_ptr
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/weak_ptr
---

ddcl|header=memory|since=c++11|1=
template< class T > class weak_ptr;
`std::weak_ptr` is a smart pointer that holds a non-owning ("weak") reference to an object that is managed by `std::shared_ptr`. It must be converted to `std::shared_ptr` in order to access the referenced object.
`std::weak_ptr` models temporary ownership: when an object needs to be accessed only if it exists, and it may be deleted at any time by someone else, `std::weak_ptr` is used to track the object, and it is converted to `std::shared_ptr` to acquire temporary ownership. If the original `std::shared_ptr` is destroyed at this time, the object's lifetime is extended until the temporary `std::shared_ptr` is destroyed as well.
Another use for `std::weak_ptr` is to break reference cycles formed by objects managed by `std::shared_ptr`. If such cycle is orphaned (i.e., there are no outside shared pointers into the cycle), the `shared_ptr` reference counts cannot reach zero and the memory is leaked. To prevent this, one of the pointers in the cycle can be made weak.

## Member types


| Item | Description |
|------|-------------|
| **Member type** | Definition |
| dsc|`element_type`|rrev multi | |
| |rev1= | |
| `T` | |
| |since2=c++17|rev2= | |
| `std::remove_extent_t<T>` | |


## Member functions


| cpp/memory/weak_ptr/dsc constructor | (see dedicated page) |
| cpp/memory/weak_ptr/dsc destructor | (see dedicated page) |
| cpp/memory/weak_ptr/dsc operator{{= | (see dedicated page) |

#### Modifiers

| cpp/memory/weak_ptr/dsc reset | (see dedicated page) |
| cpp/memory/weak_ptr/dsc swap | (see dedicated page) |

#### Observers

| cpp/memory/weak_ptr/dsc use_count | (see dedicated page) |
| cpp/memory/weak_ptr/dsc expired | (see dedicated page) |
| cpp/memory/weak_ptr/dsc lock | (see dedicated page) |
| cpp/memory/weak_ptr/dsc owner_before | (see dedicated page) |
| cpp/memory/weak_ptr/dsc owner_hash | (see dedicated page) |
| cpp/memory/weak_ptr/dsc owner_equal | (see dedicated page) |


## Non-member functions


| cpp/memory/weak_ptr/dsc swap2 | (see dedicated page) |


## Helper classes


| cpp/memory/weak_ptr/dsc atomic2 | (see dedicated page) |


## <sup>(C++17)</sup>


## Notes

Like `std::shared_ptr`, a typical implementation of `weak_ptr` stores two pointers:
* a pointer to the control block; and
* the stored pointer of the `shared_ptr` it was constructed from.
A separate stored pointer is necessary to ensure that converting a `shared_ptr` to `weak_ptr` and then back works correctly, even for aliased `shared_ptr`s. It is not possible to access the stored pointer in a `weak_ptr` without locking it into a `shared_ptr`.

## Example


### Example

```cpp
#include <iostream>
#include <memory>

std::weak_ptr<int> gw;

void observe()
{
    std::cout << "gw.use_count() == " << gw.use_count() << "; ";
    // we have to make a copy of shared pointer before usage:
    if (std::shared_ptr<int> spt = gw.lock())
        std::cout << "*spt == " << *spt << '\n';
    else
        std::cout << "gw is expired\n";
}

int main()
{
    {
        auto sp = std::make_shared<int>(42);
        gw = sp;

        observe();
    }

    observe();
}
```


**Output:**
```
gw.use_count() == 1; *spt == 42
gw.use_count() == 0; gw is expired
```


## Defect reports


## See also


| cpp/memory/dsc unique_ptr | (see dedicated page) |
| cpp/memory/dsc shared_ptr | (see dedicated page) |


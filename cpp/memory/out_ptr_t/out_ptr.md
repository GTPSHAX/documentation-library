---
title: std::out_ptr
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/out_ptr_t/out_ptr
---

ddcla|header=memory|since=c++23|constexpr=c++26|1=
template< class Pointer = void, class Smart, class... Args >
auto out_ptr( Smart& s, Args&&... args );
Returns an  with deduced template arguments that captures arguments for resetting by reference.
.

## Parameters


### Parameters

- `s` - the object (typically a smart pointer) to adapt
- `args` - the arguments for resetting to capture

## Return value

`std::out_ptr_t<Smart, P, Args&&>(s, std::forward<Args>(args)...)`, where `P` is
* `Pointer`, if `Pointer` is not same as `void`. Otherwise,
* `Smart::pointer`, if it is valid and denotes a type. Otherwise,
* `Smart::element_type*`, if `Smart::element_type` is valid and denotes a type. Otherwise,
* `std::pointer_traits<Smart>::element_type*`.

## Notes

Users may specify the template argument for the template parameter `Pointer`, in order to interoperate with foreign functions that take a `Pointer*`.
As all arguments for resetting are captured by reference, the returned `out_ptr_t` should be a temporary object destroyed at the end of the full-expression containing the call to the foreign function, in order to avoid dangling references.

## Example

Uses `std::out_ptr` to adapt a smart pointer for [https://www.sqlite.org/c3ref/open.html `sqlite3_open`], which expects an `sqlite3**` as an out parameter.

```cpp
#include <memory>
#include <sqlite3.h>

int main()
{
    auto close_db = [](sqlite3* db) { sqlite3_close(db); };

    {
        // open an in-memory database, and manage its lifetime with std::unique_ptr
        std::unique_ptr<sqlite3, decltype(close_db)> up;
        sqlite3_open(":memory:", std::out_ptr(up));

        sqlite3* db = up.get();
        // do something with db ...
    }
    {
        // same as above, but use a std::shared_ptr
        std::shared_ptr<sqlite3> sp;
        sqlite3_open(":memory:", std::out_ptr(sp, close_db));

        sqlite3* db = sp.get();
        // do something with db ...
    }
}
```


## See also


| cpp/memory/inout_ptr_t/dsc inout_ptr | (see dedicated page) |
| cpp/memory/unique_ptr/dsc make_unique | (see dedicated page) |
| cpp/memory/shared_ptr/dsc make_shared | (see dedicated page) |


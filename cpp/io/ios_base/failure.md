---
title: std::ios_base::failure
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ios_base/failure
---

ddcl|header=ios|
class failure;
The class `std::ios_base::failure` defines an exception object that is thrown on failure by the functions in the Input/Output library.
rrev|since=c++17|
`std::ios_base::failure` may be defined either as a member class of `std::ios_base` or as a synonym (typedef) for another class with equivalent functionality.
rrev multi|until1=c++11
|rev1=
|rev2=

## Member functions

member|failure|

```cpp
dcl rev multi|num=1|until1=c++11
|dcl1=
explicit failure( const std::string& message );
|dcl2=
explicit failure( const std::string& message,
const std::error_code& ec = std::io_errc::stream );
dcl|num=2|since=c++11|1=
explicit failure( const char* message,
const std::error_code& ec = std::io_errc::stream );
dcl rev multi|num=3|until1=c++11
|dcl1=
failure( const failure& other );
|dcl2=
failure( const failure& other ) noexcept;
```

@1,2@ Constructs the exception object using `message` as explanation string which can later be retrieved using . <sup>(since C++11)</sup> `ec` is used to identify the specific reason for the failure.
3. Copy constructor. Initialize the contents with those of `other`. <sup>(since C++11)</sup> If `*this` and `other` both have dynamic type `std::ios_base::failure` then `1=std::strcmp(what(), other.what()) == 0`.

## Parameters


### Parameters

- `message` - explanatory string
- `ec` - error code to identify the specific reason for the failure
- `other` - another `failure` to copy

## Notes

Because copying `std::ios_base::failure` is not permitted to throw exceptions, this message is typically stored internally as a separately-allocated reference-counted string. This is also why there is no constructor taking `std::string&&`: it would have to copy the content anyway.

## Notes

Before the resolution of , `std::ios_base::failure` declared a destructor without `throw()`, where `cpp/error/exception/~exception|std::exception::~exception()` was declared with `throw()`. This means the `std::ios_base::failure::~failure()` had a weaker exception specification. The resolution is to remove that declaration so that the non-throwing exception specification is kept.
targets the same defect and its resolution is to add `throw()` to the declaration of `std::ios_base::failure::~failure()`. That resolution was not applied due to the conflict between the two resolutions.

## Example


### Example

```cpp
#include <fstream>
#include <iostream>

int main()
{
    std::ifstream f("doesn't exist");

    try
    {
        f.exceptions(f.failbit);
    }
    catch (const std::ios_base::failure& e)
    {
        std::cout << "Caught an ios_base::failure.\n"
                  << "Explanatory string: " << e.what() << '\n'
                  << "Error code: " << e.code() << '\n';
    }
}
```


**Output:**
```
Caught an ios_base::failure.
Explanatory string: ios_base::clear: unspecified iostream_category error
Error code: iostream:1
```


## Defect reports


## See also


| cpp/io/dsc io_errc | (see dedicated page) |


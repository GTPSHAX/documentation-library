---
title: Value-initialization
type: Language
source: https://en.cppreference.com/w/cpp/language/value_initialization
---


# Value-initialization

This is the initialization performed when an object is constructed with an empty initializer.

## Syntax


**Syntax:**

- `**`()`**`
- `*T* **`()`**`
- `**`::`***Class***`(`***...***`)`** **`:`** *member* **`()`** **`{`** *...* }`
- `*object* }|notes=<sup>(C++11)</sup>`
- `}|notes=<sup>(C++11)</sup>`
- `*T* }|notes=<sup>(C++11)</sup>`
- `**`::`***Class***`(`***...***`)`** **`:`** *member* } **`{`** *...* }|notes=<sup>(C++11)</sup>`

## Explanation

Value-initialization is performed in these situations:
@1,5@ when a nameless temporary object is created with the initializer consisting of an empty pair of parentheses<sup>(since C++11)</sup>  or braces;
@2,6@ when an object with dynamic storage duration is created by a ``new` expression` with the initializer consisting of an empty pair of parentheses<sup>(since C++11)</sup>  or braces;
@3,7@ when a non-static data member or a base class is initialized using a `member initializer` with an empty pair of parentheses <sup>(since C++11)</sup> or braces;
4. when a named object (automatic, static, or thread-local) is declared with the initializer consisting of a pair of braces.
In all cases, if the empty pair of braces } is used and `T` is an aggregate type, `aggregate initialization` is performed instead of value-initialization.
rrev|since=c++11|
If `T` is a class type that has no default constructor but has a constructor taking `std::initializer_list`, `list-initialization` is performed.
The effects of value-initialization are:
* If `T` is a (possibly cv-qualified) class type:
:* If the default-initialization for `T` selects a `constructor`, and the constructor is not <sup>(until C++11)</sup> user-declared<sup>(since C++11)</sup> `user-provided`, the object is first `zero-initialized`.
:* In any case, the object is `default-initialized`.
* Otherwise, if `T` is an array type, each element of the array is value-initialized.
* Otherwise, the object is zero-initialized.

## Notes

The syntax `T object();` does not initialize an object; it declares a function that takes no arguments and returns `T`. The way to value-initialize a named variable before C++11 was `1=T object = T();`, which value-initializes a temporary and then copy-initializes the object: most compilers `optimize out the copy` in this case.
References cannot be value-initialized.
As described in `function-style cast`, the syntax `T()`  is prohibited if `T` names an array type, while }  is allowed.
All standard containers (`std::vector`, `std::list`, etc.) value-initialize their elements when constructed with a single `size_type` argument or when grown by a call to `resize()`, unless their allocator customizes the behavior of `construct`.

## Example


### Example

```cpp
#include <cassert>
#include <iostream>
#include <string>
#include <vector>

struct T1
{
    int mem1;
    std::string mem2;
    virtual void foo() {} // make sure T1 is not an aggregate
}; // implicit default constructor

struct T2
{
    int mem1;
    std::string mem2;
    T2(const T2&) {} // user-provided copy constructor
};                   // no default constructor

struct T3
{
    int mem1;
    std::string mem2;
    T3() {} // user-provided default constructor
};

std::string s{}; // class => default-initialization, the value is ""

int main()
{
    int n{};                // scalar => zero-initialization, the value is 0
    assert(n == 0);
    double f = double();    // scalar => zero-initialization, the value is 0.0
    assert(f == 0.0);
    int* a = new int[10](); // array => value-initialization of each element
    assert(a[9] == 0);      //          the value of each element is 0
    T1 t1{};                // class with implicit default constructor =>
    assert(t1.mem1 == 0);   //     t1.mem1 is zero-initialized, the value is 0
    assert(t1.mem2 == "");  //     t1.mem2 is default-initialized, the value is ""
//  T2 t2{};                // error: class with no default constructor
    T3 t3{};                // class with user-provided default constructor =>
    std::cout << t3.mem1;   //     t3.mem1 is default-initialized to indeterminate value
    assert(t3.mem2 == "");  //     t3.mem2 is default-initialized, the value is ""
    std::vector<int> v(3);  // value-initialization of each element
    assert(v[2] == 0);      // the value of each element is 0
    std::cout << '\n';
    delete[] a;
}
```


**Output:**
```
42
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-543 | C++98 | value-initialization for a class object without any<br>user-provided constructors was equivalent to value-<br>initializing each subobject (which need not zero-<br>initialize a member with user-provided default constructor) | zero-initializes<br>the entire object,<br>then calls the<br>default constructor |
| cwg-1301 | C++11 | value-initialization of unions with deleted<br>default constructors led to zero-initialization | they are<br>default-initialized |
| cwg-1368 | C++98 | any user-provided constructor caused<br>zero-initialization to be skipped | only a user-provided<br>default constructor<br>skips zero-initialization |
| cwg-1502 | C++11 | value-initializing a union without a user-provided<br>default constructor only zero-initialized the<br>object, despite default member initializers | performs default-<br>initialization after<br>zero-initialization |
| cwg-1507 | C++98 | value-initialization for a class object without any<br>user-provided constructors did not check the validity<br>of the default constructor when the latter is trivial | the validity of trivial<br>default constructor<br>is checked |
| cwg-2820 | C++98 | the default-initialization following the zero-<br>initialization required a non-trivial constructor | not required |
| cwg-2859 | C++98 | value-initialization for a class object might involve<br>zero-initialization even if the default-initialization<br>does not actually select a user-provided constructor | there is no<br>zero-initialization<br>in this case |


## See also

* `default constructor`
* `explicit`
* `aggregate initialization`
* `list-initialization`

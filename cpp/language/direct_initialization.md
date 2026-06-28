---
title: Direct-initialization
type: Language
source: https://en.cppreference.com/w/cpp/language/direct_initialization
---


# Direct-initialization

Initializes an object from explicit set of constructor arguments.

## Syntax


**Syntax:**

- `*object* **`(`** *arg* **`);`**`
- `*T* *object* **`(`** *arg1, arg2, ...* **`);`**`
- `* object* **`{`** *arg* ttb|};`
- `|notes=<sup>(C++11)</sup>`
- `**`(`** *other* **`)`**`
- `*T* **`(`** *arg1, arg2, ...* **`)`**`
- `*T* **`>(`** *other* **`)`**`
- `*T***`(`** *args, ...* **`)`**`
- `**`::`***Class***`()`** **`:`** *member***`(`** *args, ...* **`)`** **`{`** *...* }`
- `*arg***`]() {`** *...* }|notes=<sup>(C++11)</sup>`

## Explanation

Direct-initialization is performed in the following situations:
1. Initialization with a nonempty parenthesized list of expressions <sup>(since C++11)</sup> or braced-init-lists.
2. Initialization of an object of non-class type with a single brace-enclosed initializer <sup>(since C++11)</sup> (note: for class types and other uses of braced-init-list, see `list-initialization)`.
3. Initialization of <sup>(until C++17)</sup> a prvalue temporary<sup>(since C++17)</sup> the result object of a prvalue by `function-style cast` or with a parenthesized expression list.
4. Initialization of <sup>(until C++17)</sup> a prvalue temporary<sup>(since C++17)</sup> the result object of a prvalue by a `static_cast` expression.
5. Initialization of an object with dynamic storage duration by a new-expression with an initializer.
6. Initialization of a base or a non-static member by constructor `initializer list`.
7. Initialization of closure object members from the variables caught by copy in a lambda-expression.
The effects of direct-initialization are:
* If `T` is an array type,
rev|until=c++20|
:* the program is ill-formed.
rev|since=c++20|
:* the array is initialized as in `aggregate initialization`, except that narrowing conversions are allowed and any elements without an initializer are `value-initialized`.

```cpp
struct A
{
    explicit A(int i = 0) {}
};

A a[2](A(1)); // OK: initializes a[0] with A(1) and a[1] with A()
A b[2]{A(1)}; // error: implicit copy-list-initialization of b[1]
              //        from {} selected explicit constructor
```

* If `T` is a class type,
rev|since=c++17|
:* if the initializer is a `prvalue` expression whose type is the same class as `T` (ignoring cv-qualification), the initializer expression itself, rather than a temporary materialized from it, is used to initialize the destination object.<br>(Before C++17, the compiler may elide the construction from the prvalue temporary in this case, but the appropriate constructor must still be accessible: see `copy elision`)
:* the constructors of `T` are examined and the best match is selected by overload resolution. The constructor is then called to initialize the object.
rrev|since=c++20|
:* otherwise, if the destination type is a (possibly cv-qualified) aggregate class, it is initialized as described in `aggregate initialization` except that narrowing conversions are permitted, designated initializers are not allowed, a temporary bound to a reference does not have its lifetime extended, there is no brace elision, and any elements without an initializer are `value-initialized`.

```cpp
<!--example from p0960r3-->
struct B
{
    int a;
    int&& r;
};

int f();
int n = 10;

B b1{1, f()};            // OK, lifetime is extended
B b2(1, f());            // well-formed, but dangling reference
B b3{1.0, 1};            // error: narrowing conversion
B b4(1.0, 1);            // well-formed, but dangling reference
B b5(1.0, std::move(n)); // OK
```

* Otherwise, if `T` is a non-class type but the source type is a class type, the conversion functions of the source type and its base classes, if any, are examined and the best match is selected by overload resolution. The selected user-defined conversion is then used to convert the initializer expression into the object being initialized.
* Otherwise, if `T` is `bool` and the source type is `std::nullptr_t`, the value of the initialized object is `false`.
* Otherwise, `standard conversions` are used, if necessary, to convert the value of *other* to the cv-unqualified version of `T`, and the initial value of the object being initialized is the (possibly converted) value.

## Notes

Direct-initialization is more permissive than copy-initialization: copy-initialization only considers non-`explicit` constructors and non-explicit user-defined `conversion functions`, while direct-initialization considers all constructors and all user-defined conversion functions.
In case of ambiguity between a variable declaration using the direct-initialization syntax  (with round parentheses) and a `function declaration`, the compiler always chooses function declaration. This disambiguation rule is sometimes counter-intuitive and has been called the [most vexing parse](https://en.wikipedia.org/wiki/most vexing parse).

## Example


### Example

```cpp
#include <iostream>
#include <memory>
#include <string>

struct Foo
{
    int mem;
    explicit Foo(int n) : mem(n) {}
};

int main()
{
    std::string s1("test"); // constructor from const char*
    std::string s2(10, 'a');

    std::unique_ptr<int> p(new int(1));  // OK: explicit constructors allowed
//  std::unique_ptr<int> p = new int(1); // error: constructor is explicit

    Foo f(2); // f is direct-initialized:
              // constructor parameter n is copy-initialized from the rvalue 2
              // f.mem is direct-initialized from the parameter n
//  Foo f2 = 2; // error: constructor is explicit

    std::cout << s1 << ' ' << s2 << ' ' << *p << ' ' << f.mem  << '\n';
}
```


**Output:**
```
test aaaaaaaaaa 1 2
```


## See also

* `copy elision`
* `converting constructor`
* `copy assignment`
* `copy constructor`
* `default constructor`
* `destructor`
* `explicit`
* `initialization`
** `aggregate initialization`
** `constant initialization`
** `copy initialization`
** `default initialization`
** `initializer list`
** `list initialization`
** `reference initialization`
** `value initialization`
** `zero initialization`
* `move assignment`
* `move constructor`
* `new`

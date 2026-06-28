---
title: Constructors and member initializer lists
type: Language
source: https://en.cppreference.com/w/cpp/language/constructor
---


# Constructors and member initializer lists

''Constructors'' are non-static `member functions` declared with a special declarator syntax, they are used to initialize objects of their class types.
rev|since=c++20|
A constructor cannot be a `coroutine`.
rev|since=c++23|
A constructor cannot have an .

## Syntax

Constructors are declared using member `function declarators` of the following form:

**Syntax:**

- `**`(`** *parameter-list* (optional) **`)`** *except* (optional) *attr* (optional)`

### Parameters

- `{{spar` - class-name|an `identifier expression`,<sup>(since C++11)</sup>  possibly followed by a list of `attributes, and` possibly enclosed by a pair parentheses
- `{{spar` - parameter-list|
- `{{spar` - except|
- `{{spar` - attr|<sup>(C++11)</sup> a list of `attributes`
The only specifiers allowed in the `declaration specifiers` of a constructor declaration are `friend`, `inline`<sup>(since C++11)</sup> , `constexpr`<sup>(since C++20)</sup> , `consteval`, and `explicit` (in particular, no return type is allowed). Note that `cv- and ref-qualifiers` are not allowed either: const and volatile semantics of an object under construction only kick in after the most-derived constructor completes.
The identifier expression of *class-name* must have one of the following forms:
* In a `friend declaration`, the identifier expression is a `qualified identifier` that `names a constructor`.
* Otherwise, in a member declaration that belongs to the  of a class or class template:
:* For classes, the identifier expression is the `injected-class-name` of the immediately-enclosing class.
:* For class templates, the identifier expression is <sup>(until C++20)</sup> a class name that names the <sup>(since C++20)</sup> the injected-class-name of the immediately-enclosing class template.
* Otherwise, the identifier expression is a qualified identifier whose terminal unqualified identifier is the injected-class-name of its `lookup` context.

## Member initializer list

The body of a `function definition` of any constructor, before the opening brace of the compound statement, may include the ''member initializer list'', whose syntax is the colon character **`:`**, followed by the comma-separated list of one or more member-initializers, each of which has the following syntax:

**Syntax:**

- `**`(`** *expression-list* (optional) **`)`**`
- `|*class-or-identifier* *braced-init-list*`
- `|*parameter-pack* **`...`**`
1. Initializes the base or member named by *class-or-identifier* using `direct-initialization` or, if *expression-list* is empty, `value-initialization`
2. Initializes the base or member named by *class-or-identifier* using `list-initialization` (which becomes `value-initialization` if the list is empty and `aggregate-initialization` when initializing an aggregate)
3. Initializes multiple bases using a `pack expansion`

### Parameters

- `{{spar` - class-or-identifier|any identifier that names a non-static data member or any type name which names either the class itself (for delegating constructors) or a direct or virtual base. 
- `{{spar` - expression-list|possibly empty, comma-separated list of the arguments to pass to the constructor of the base or member
- `{{spar` - braced-init-list|`brace-enclosed initializer list`
- `{{spar` - parameter-pack|name of a variadic template `parameter pack`

## Explanation

Constructors have no names and cannot be called directly. They are invoked when `initialization` takes place, and they are selected according to the rules of initialization. The constructors without `explicit` specifier are `converting constructor`s. The constructors with a `constexpr` specifier make their type a . Constructors that may be called without any argument are `default constructor`s. Constructors that take another object of the same type as the argument are `copy constructor`s and `move constructor`s.
Before the compound statement that forms the function body of the constructor begins executing, initialization of all direct bases, virtual bases, and non-static data members is finished. The member initializer list is the place where non-default initialization of these subobjects can be specified. For bases that cannot be default-initialized and for non-static data members that cannot be initialized by default-initialization <sup>(since C++11)</sup> or by their `default member initializer, if any`, such as members of reference and const-qualified types, member initializers must be specified. <sup>(since C++11)</sup> (Note that default member initializers for non-static data members of class template instantiations may be invalid if the member type or initializer is dependent.) No initialization is performed for `anonymous unions` or `variant members` that do not have a member initializer <sup>(since C++11)</sup> or default member initializer.
The initializers where *class-or-identifier* names a `virtual base class` are ignored during construction of any class that is not the most derived class of the object that's being constructed.
Names that appear in *expression-list* or *braced-init-list* are evaluated in scope of the constructor:

```cpp
class X
{
    int a, b, i, j;
public:
    const int& r;
    X(int i)
      : r(a) // initializes X::r to refer to X::a
      , b{i} // initializes X::b to the value of the parameter i
      , i(i) // initializes X::i to the value of the parameter i
      , j(this->i) // initializes X::j to the value of X::i
    {}
};
```

Exceptions that are thrown from member initializers may be handled by a `function `try` block`.
rrev|since=c++11|
If a non-static data member has a `default member initializer` and also appears in a member initializer list, then the member initializer is used and the default member initializer is ignored:

```cpp
struct S
{
    int n = 42;   // default member initializer
    S() : n(7) {} // will set n to 7, not 42
};
```

Reference members cannot be bound to temporaries in a member initializer list:

```cpp
struct A
{
    A() : v(42) {} // Error
    const int& v;
};
```

Note: same applies to `default member initializer`.

### Operations during construction and destruction

Member functions (including `virtual member functions`) can be called for an object under construction or destruction. Similarly, an object under construction or destruction can be the operand of `typeid` or `dynamic_cast`.
However, if these operations are performed during any of the following evaluations, the behavior is undefined:
rrev|since=c++26|
* an evaluation of a `precondition assertion` of a constructor
* an evaluation of a `postcondition assertion` of a `destructor`
* an evaluation of a member initializer list before all the member-initializers for base classes have completed
rrev|since=c++11|

### Delegating constructor

If the name of the class itself appears as *class-or-identifier* in the member initializer list, then the list must consist of that one member initializer only; such a constructor is known as the ''delegating constructor'', and the constructor selected by the only member of the initializer list is the ''target constructor''.
In this case, the target constructor is selected by overload resolution and executed first, then the control returns to the delegating constructor and its body is executed.
Delegating constructors cannot be recursive.

```cpp
class Foo
{
public: 
    Foo(char x, int y) {}
    Foo(int y) : Foo('a', y) {} // Foo(int) delegates to Foo(char, int)
};
```


### Inheriting constructors

See ``using` declaration`.

### Initialization order

The order of member initializers in the list is irrelevant, the actual order of initialization is as follows:
1. If the constructor is for the most-derived class, virtual bases are initialized in the order in which they appear in depth-first left-to-right traversal of the base class declarations (left-to-right refers to the appearance in base-specifier lists).
2. Then, direct bases are initialized in left-to-right order as they appear in this class's base-specifier list.
3. Then, non-static data member are initialized in order of declaration in the class definition.
4. Finally, the body of the constructor is executed.
(Note: if initialization order was controlled by the appearance in the member initializer lists of different constructors, then the `destructor` wouldn't be able to ensure that the order of destruction is the reverse of the order of construction.)

## Notes


## Example


### Example

```cpp
#include <fstream>
#include <string>
#include <mutex>

struct Base
{
    int n;
};   

struct Class : public Base
{
    unsigned char x;
    unsigned char y;
    std::mutex m;
    std::lock_guard<std::mutex> lg;
    std::fstream f;
    std::string s;

    Class(int x) : Base{123}, // initialize base class
        x(x),     // x (member) is initialized with x (parameter)
        y{0},     // y initialized to 0
        f{"test.cc", std::ios::app}, // this takes place after m and lg are initialized
        s(__func__), // __func__ is available because init-list is a part of constructor
        lg(m),    // lg uses m, which is already initialized
        m{}       // m is initialized before lg even though it appears last here
    {}            // empty compound statement

    Class(double a) : y(a + 1),
        x(y), // x will be initialized before y, its value here is indeterminate
        lg(m)
    {} // base class initializer does not appear in the list, it is
       // default-initialized (not the same as if Base() were used, which is value-init)

    Class()
    try // function try block begins before the function body, which includes init list
      : Class(0.0) // delegate constructor
    {
        // ...
    }
    catch (...)
    {
        // exception occurred on initialization
    }
};

int main()
{
    Class c;
    Class c1(1);
    Class c2(0.1);
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-257 | C++98 | it was unspecified whether an abstract class should<br>provide member initializers for its virtual base classes | specified as not required<br>and such member initializers<br>are ignored during execution |
| cwg-263 | C++98 | the declarator syntax of constructor<br>prohibited constructors from being friends | allowed constructors<br>to be friends |
| cwg-1345 | C++98 | anonymous union members without default<br>member initializers were default-initialized | they are not initialized |
| cwg-1435 | C++98 | the meaning of “class name” in the<br>declarator syntax of constructor was unclear | changed the syntax to a specialized<br>function declarator syntax |
| cwg-1696 | C++98 | reference members could be initialized to temporaries<br>(whose lifetime would end at the end of constructor) | such initialization<br>is ill-formed |


## References


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
** `direct initialization`
** `list initialization`
** `reference initialization`
** `value initialization`
** `zero initialization`
* `move assignment`
* `move constructor`
* `new`

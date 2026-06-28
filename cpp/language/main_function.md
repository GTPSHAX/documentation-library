---
title: Main function
type: Language
source: https://en.cppreference.com/w/cpp/language/main_function
---


# Main function

A program shall contain a global function named `main`, which is the designated start of the program in hosted environment. It shall have one of the following forms:

**Syntax:**

- `sdsc|num=1|1=`
- ``int`**` main() {`** *body* }`
- `sdsc|num=2|1=`
- ``int`**` main(`**`int` *argc***`,`** `char*` *argv*`[]`**`) {`** *body* }`
- `sdsc|num=3|1=`
- ``int`**` main(`**`/* implementation-defined */`**`) {`** *body* }`
1. A `main` function running independently of environment-provided arguments.
2. A `main` function accepting environment-provided arguments.
@@ The names of *argc* and *argv* are arbitrary, as well as the representation of the types of the parameters: `int main(int ac, char** av)` is equally valid.
3. A `main` function of implement-defined type, returning `int`.
@@ The C++ standard recommends implementation-defined `main` functions to place the extra (optional) parameters after argv.

### Parameters

- `{{spar` - argc|Non-negative value representing the number of arguments passed to the program from the environment in which the program is run.
- `{{spar` - argv|Pointer to the first element of an array of `argc + 1` pointers, of which the last one is null and the previous ones, if any, point to null-terminated multibyte strings that represent the arguments passed to the program from the execution environment. If `argv[0]` is not a null pointer (or, equivalently, if `argc > 0`), it points to a string that represents the name used to invoke the program, or to an empty string.
- `{{spar` - body|The body of the `main` function.

## Explanation

The `main` function is called at program startup after `initialization` of the non-local objects with static `storage duration`. It is the designated entry point to a program that is executed in hosted environment (that is, with an operating system). The entry points to  programs (boot loaders, OS kernels, etc) are implementation-defined.
The parameters of the two-parameter form of the `main` function allow arbitrary multibyte character strings to be passed from the execution environment (these are typically known as ''command line arguments''), the pointers  point at the first characters in each of these strings. `argv[0]` (if non-null) is the pointer to the initial character of a null-terminated multibyte string that represents the name used to invoke the program itself (or an empty string `""` if this is not supported by the execution environment). The strings are modifiable, although these modifications do not propagate back to the execution environment: they can be used, for example, with `std::strtok`. The size of the array pointed to by `argv` is at least `argc + 1`, and the last element, `argv[argc]`, is guaranteed to be a null pointer.
The `main` function has the following several special properties:
1. The body of the `main` function does not need to contain the ``return` statement`: if control reaches the end of `main` without encountering a return statement, the effect is that of executing `return 0;`.
2. Execution of the return (or the implicit return upon reaching the end of `main`) is equivalent to first leaving the function normally (which destroys the objects with automatic storage duration<sup>(since C++26)</sup>  and evaluates any ) and then calling `std::exit` with the same argument as the argument of the `return` (`std::exit` then destroys static objects and terminates the program).
The `main` function has several restrictions (violation of which renders the program ill-formed):
1. It cannot be `named` anywhere in the program:
:@a@ In particular, it cannot be called recursively.
:@b@ Its address cannot be taken.
:@c@ It cannot be used in a `typeid` expression <sup>(since C++11)</sup> or a `decltype specifier`.
2. It cannot be predefined and cannot be overloaded: effectively, the name `main` in the global namespace is reserved for functions (although it can be used to name classes, namespaces, enumerations, and any entity in a non-global namespace, except that an entity named `main` cannot be declared with C `language linkage` in any namespace.
3. It cannot be declared with any language linkage other than `"C++"`, or
rev|since=c++11|
* `constexpr`
rev|since=c++20|
* `consteval`
* `inline`
* `static`
rev|since=c++11|
4. It cannot be `defined as deleted`.
rev|since=c++14|
5. The return type of the `main` function cannot be deduced (} is not allowed).
rev|since=c++20|
6. The `main` function cannot be a `coroutine`.
7. The `main` function cannot attach to a named `module`.

## Notes

If the `main` function is defined with a `function `try` block`, the exceptions thrown by the destructors of static objects (which are destroyed by the implied `std::exit`) are not `caught` by it.
The manner in which the arguments given at the OS command line are converted into the multibyte character arrays referenced by `argv` may involve implementation-defined processing:
* [https://docs.microsoft.com/en-us/cpp/cpp/main-function-command-line-args Parsing C++ Command-Line Arguments] MSDN
* [https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_01 Shell Introduction] POSIX
A very common implementation-defined form of `main()` has a third argument (in addition to `argc` and `argv`), of type `char**`, pointing at [https://pubs.opengroup.org/onlinepubs/9699919799/functions/exec.html an array of pointers to the execution environment variables].

## Example

|code=
#include <cstdlib>
#include <iomanip>
#include <iostream>
int main(int argc, char *argv[])
{
std::cout << "argc == " << argc << '\n';
for (int ndx{}; ndx != argc; ++ndx)
std::cout << "argv[" << ndx << "] == " << std::quoted(argv[ndx]) << '\n';
std::cout << "argv[" << argc << "] == "
<< static_cast<void*>(argv[argc]) << '\n';
/* ... */
return argc == 3 ? EXIT_SUCCESS : EXIT_FAILURE; // optional return value
}
|p=true
|output=
argc == 3
argv[0] == "./convert"
argv[1] == "table_in.dat"
argv[2] == "table_out.dat"
argv[3] == 0

## References


## Defect reports


## See also


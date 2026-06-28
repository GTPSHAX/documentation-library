---
title: std::strerror
type: Strings
source: https://en.cppreference.com/w/cpp/string/byte/strerror
---

ddcl|header=cstring|
char* strerror( int errnum );
Returns a pointer to the textual description of the system error code `errnum`, identical to the description that would be printed by `std::perror()`.
`errnum` is usually acquired from the `errno` variable, however the function accepts any value of type `int`. The contents of the string are locale-specific.
The returned string must not be modified by the program, but may be overwritten by a subsequent call to the `strerror` function. `strerror` is not required to be thread-safe. Implementations may be returning different pointers to static read-only string literals or may be returning the same pointer over and over, pointing at a static buffer in which `strerror` places the string.

## Parameters


### Parameters

- `errnum` - integer value referring to an error code

## Return value

Pointer to a null-terminated byte string corresponding to the `errno` error code `errnum`.

## Notes

[https://pubs.opengroup.org/onlinepubs/9699919799/functions/strerror.html POSIX] allows subsequent calls to `strerror` to invalidate the pointer value returned by an earlier call. It also specifies that it is the `cpp/locale/LC_categories|LC_MESSAGES` locale facet that controls the contents of these messages.
POSIX has a thread-safe version called `strerror_r` defined. Glibc [https://www.club.cc.cmu.edu/~cmccabe/blog_strerror.html defines an incompatible version].

## Example


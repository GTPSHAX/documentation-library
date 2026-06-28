---
title: std::getenv
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/program/getenv
---

ddcl|header=cstdlib|
char* getenv( const char* env_var );
Searches the ''environment list'' provided by the host environment (the OS), for a string that matches the C string pointed to by `env_var` and returns a pointer to the C string that is associated with the matched environment list member.
rev|until=c++11|
This function is not required to be thread-safe. Another call to `getenv`, as well as a call to the POSIX functions [https://pubs.opengroup.org/onlinepubs/9699919799/functions/setenv.html `setenv()`], [https://pubs.opengroup.org/onlinepubs/9699919799/functions/unsetenv.html `unsetenv()`], and [https://pubs.opengroup.org/onlinepubs/9699919799/functions/putenv.html `putenv()`] may invalidate the pointer returned by a previous call or modify the string obtained from a previous call.
rev|since=c++11|
This function is thread-safe (calling it from multiple threads does not introduce a data race) as long as no other function modifies the host environment. In particular, the POSIX functions [https://pubs.opengroup.org/onlinepubs/9699919799/functions/setenv.html `setenv()`], [https://pubs.opengroup.org/onlinepubs/9699919799/functions/unsetenv.html `unsetenv()`], and [https://pubs.opengroup.org/onlinepubs/9699919799/functions/putenv.html `putenv()`] would introduce a data race if called without synchronization.
Modifying the string returned by `getenv` invokes undefined behavior.

## Parameters


### Parameters

- `env_var` - null-terminated character string identifying the name of the environmental variable to look for

## Return value

Character string identifying the value of the environmental variable or null pointer if such variable is not found.

## Notes

On POSIX systems, the [https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap08.html#tag_08 environment variables] are also accessible through the global variable `environ`, declared as `extern char** environ;` in , and through the optional third argument, `envp`, of the main function.

## Example


### Example

```cpp
#include <cstdlib>
#include <iostream>

int main()
{
    if (const char* env_p = std::getenv("PATH"))
        std::cout << "Your PATH is: " << env_p << '\n';
}
```


**Output:**
```
Your PATH is: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
```


## See also


---
title: std::is_debugger_present
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/is_debugger_present
---

ddcl|header=debugging|since=c++26|
bool is_debugger_present() noexcept;
Attempts to determine if the program is being executed with debugger present.
This function is replaceable.

## Return value

The default version returns an implementation-defined value, which usually represents whether the program is executed under a debugger.

## Notes

The intent of this function is allowing printing out extra output to help diagnose problems, executing extra test code, displaying an extra user interface to help in debugging, etc.

## Example


## External links

`is_debugger_present` standardizes many similar existing facilities, e.g.:

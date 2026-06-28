---
title: std::breakpoint_if_debugging
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/breakpoint_if_debugging
---

ddcl|header=debugging|since=c++26|
void breakpoint_if_debugging() noexcept;
Conditional breakpoint: attempts to temporarily halt the execution of the program and transfer control to the debugger if it were able to determine that the debugger is present. Acts as a no-op otherwise.
Formally, the behavior of this function is completely implementation-defined. Equivalent to
c multi|
if (std::is_debugger_present())|
std::breakpoint();
.

## Notes


## Example


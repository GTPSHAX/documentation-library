---
title: std::errc
type: Utilities
source: https://en.cppreference.com/w/cpp/error/errc
---

ddcl|header=system_error|since=c++11|
enum class errc;
The scoped enumeration `std::errc` defines the values of portable error conditions that correspond to the POSIX error codes.

## Member constants


| Item | Description |
|------|-------------|
| **Name** | Equivalent POSIX Error |


## Non-member functions


| cpp/error/errc/dsc make_error_code | (see dedicated page) |
| cpp/error/errc/dsc make_error_condition | (see dedicated page) |


## Helper classes


| cpp/error/errc/dsc is_error_condition_enum | (see dedicated page) |


## Example


### Example

```cpp
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <system_error>
#include <thread>

void print_error(const std::string& details, std::error_code error_code)
{
    std::string value_name;
    if (error_code == std::errc::invalid_argument)
        value_name = "std::errc::invalid_argument";
    if (error_code == std::errc::no_such_file_or_directory)
        value_name = "std::errc::no_such_file_or_directory";
    if (error_code == std::errc::is_a_directory)
        value_name = "std::errc::is_a_directory";
    if (error_code == std::errc::permission_denied)
        value_name = "std::errc::permission_denied";

    std::cout << details << ":\n  "
              << std::quoted(error_code.message())
              << " (" << value_name << ")\n\n";
}

void print_errno(const std::string& details, int errno_value = errno)
{
    print_error(details, std::make_error_code(std::errc(errno_value)));
}

int main()
{
    std::cout << "Detaching a not-a-thread...\n";
    try
    {
        std::thread().detach();
    }
    catch (const std::system_error& e)
    {
        print_error("Error detaching empty thread", e.code());
    }

    std::cout << "Opening nonexistent file...\n";
    std::ifstream nofile{"nonexistent-file"};
    if (!nofile.is_open())
        print_errno("Error opening nonexistent file for reading");

    std::cout << "Reading from directory as a file...\n";
    std::filesystem::create_directory("dir");
    std::ifstream dir_stream{"dir"};
    [[maybe_unused]] char c = dir_stream.get();
    if (!dir_stream.good())
        print_errno("Error reading data from directory");

    std::cout << "Open read-only file for writing...\n";
    std::fstream{"readonly-file", std::ios::out};
    std::filesystem::permissions("readonly-file", std::filesystem::perms::owner_read);
    std::fstream write_readonly("readonly-file", std::ios::out);
    if (!write_readonly.is_open())
        print_errno("Error opening read-only file for writing");
}
```


**Output:**
```
Detaching a not-a-thread...
Error detaching empty thread:
  "Invalid argument" (std::errc::invalid_argument)

Opening nonexistent file...
Error opening nonexistent file for reading:
  "No such file or directory" (std::errc::no_such_file_or_directory)

Reading from directory as a file...
Error reading data from directory:
  "Is a directory" (std::errc::is_a_directory)

Open read-only file for writing...
Error opening read-only file for writing:
  "Permission denied" (std::errc::permission_denied)
```


## Defect reports


## See also


| cpp/error/dsc error_code | (see dedicated page) |
| cpp/error/dsc error_condition | (see dedicated page) |


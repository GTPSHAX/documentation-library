---
title: C-style file input/output
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c
---


# C-style file input/output

The C I/O subset of the C++ standard library implements C-style stream input/output operations. The  header provides generic file operation support and supplies functions with narrow and multibyte character input/output capabilities, and the  header provides functions with wide character input/output capabilities.
C streams are denoted by objects of type `std::FILE` that can only be accessed and manipulated through pointers of type `std::FILE*`. Each C stream is associated with an external physical device (file, standard input stream, printer, serial port, etc).

## Types


| cstdio | |
| cpp/io/c/dsc FILE | (see dedicated page) |
| cpp/io/c/dsc fpos_t | (see dedicated page) |


## Predefined standard streams


| cstdio | |
| cpp/io/c/dsc std streams | (see dedicated page) |


## Functions


| cstdio | |

#### File access

| cpp/io/c/dsc fopen | (see dedicated page) |
| cpp/io/c/dsc freopen | (see dedicated page) |
| cpp/io/c/dsc fclose | (see dedicated page) |
| cpp/io/c/dsc fflush | (see dedicated page) |
| cpp/io/c/dsc fwide | (see dedicated page) |
| cpp/io/c/dsc setbuf | (see dedicated page) |
| cpp/io/c/dsc setvbuf | (see dedicated page) |

#### Direct input/output

| cpp/io/c/dsc fread | (see dedicated page) |
| cpp/io/c/dsc fwrite | (see dedicated page) |

#### Unformatted input/output

| cpp/io/c/dsc fgetc | (see dedicated page) |
| cpp/io/c/dsc fgets | (see dedicated page) |
| cpp/io/c/dsc fputc | (see dedicated page) |
| cpp/io/c/dsc fputs | (see dedicated page) |
| cpp/io/c/dsc getchar | (see dedicated page) |
| cpp/io/c/dsc gets | (see dedicated page) |
| cpp/io/c/dsc putchar | (see dedicated page) |
| cpp/io/c/dsc puts | (see dedicated page) |
| cpp/io/c/dsc ungetc | (see dedicated page) |
| cpp/io/c/dsc fgetwc | (see dedicated page) |
| cpp/io/c/dsc fgetws | (see dedicated page) |
| cpp/io/c/dsc fputwc | (see dedicated page) |
| cpp/io/c/dsc fputws | (see dedicated page) |
| cpp/io/c/dsc getwchar | (see dedicated page) |
| cpp/io/c/dsc putwchar | (see dedicated page) |
| cpp/io/c/dsc ungetwc | (see dedicated page) |

#### Formatted input/output

| cpp/io/c/dsc fscanf | (see dedicated page) |
| cpp/io/c/dsc vfscanf | (see dedicated page) |
| cpp/io/c/dsc fprintf | (see dedicated page) |
| cpp/io/c/dsc vfprintf | (see dedicated page) |
| cpp/io/c/dsc fwscanf | (see dedicated page) |
| cpp/io/c/dsc vfwscanf | (see dedicated page) |
| cpp/io/c/dsc fwprintf | (see dedicated page) |
| cpp/io/c/dsc vfwprintf | (see dedicated page) |

#### File positioning

| cpp/io/c/dsc ftell | (see dedicated page) |
| cpp/io/c/dsc fgetpos | (see dedicated page) |
| cpp/io/c/dsc fseek | (see dedicated page) |
| cpp/io/c/dsc fsetpos | (see dedicated page) |
| cpp/io/c/dsc rewind | (see dedicated page) |

#### Error handling

| cpp/io/c/dsc clearerr | (see dedicated page) |
| cpp/io/c/dsc feof | (see dedicated page) |
| cpp/io/c/dsc ferror | (see dedicated page) |
| cpp/io/c/dsc perror | (see dedicated page) |

#### Operations on files

| cpp/io/c/dsc remove | (see dedicated page) |
| cpp/io/c/dsc rename | (see dedicated page) |
| cpp/io/c/dsc tmpfile | (see dedicated page) |
| cpp/io/c/dsc tmpnam | (see dedicated page) |


## Macro constants


| cstdio | |


## See also


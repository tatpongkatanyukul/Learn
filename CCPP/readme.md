# C/C++

## Create C Library

Steps
  * write a header file
  * write library functions
    * also, include the header file
  * write a main file
    * have the header file
  * compile
    * compile the library ```gcc -c -g <lib.c>```
    * compile the main file ```gcc -c -g <main.c>```
    * link ```gcc -o <main.exe> <main.o> <lib.o>```
    * the object file is ready for execution ```main.exe```

See [example](https://github.com/tatpongkatanyukul/Learn/blob/main/CCPP/clib.rar)


## Create C++ Library

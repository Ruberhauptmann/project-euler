cmake_minimum_required(VERSION 3.10)

project(project-euler)

set(CMAKE_CXX_STANDARD 20)
enable_language(Fortran)

add_executable(1_Multiples_of_3_or_5_fortran 1_Multiples_of_3_or_5.f90)

add_executable(1_Multiples_of_3_or_5_cpp 1_Multiples_of_3_or_5.cpp)

add_executable(2_Even_Fibonacci_Numbers_cpp 2_Even_Fibonacci_Numbers.cpp)

add_executable(2_Even_Fibonacci_Numbers_fortran 2_Even_Fibonacci_Numbers.f90)

cmake_minimum_required(VERSION 3.27)
project(cpp)

set(CMAKE_CXX_STANDARD 23)

include(FetchContent)
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG v1.14.0
)
FetchContent_MakeAvailable(googletest)

# Main application executable
add_executable(cpp main.cpp day1.cpp)

# Test executable - include day1.cpp here
add_executable(day1_test day1_test.cpp day1.cpp)
target_link_libraries(day1_test gtest_main)

# Enable testing and declare a test
enable_testing()
add_test(NAME day1_test COMMAND day1_test)

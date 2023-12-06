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


add_executable(day1_test day1_test.cpp day1.cpp utils.cpp)
add_executable(day2_test day2_test.cpp day2.cpp utils.cpp)
add_executable(day3_test day3_test.cpp day3.cpp utils.cpp)
add_executable(day4_test day4_test.cpp day4.cpp utils.cpp)

target_link_libraries(day1_test gtest_main)
target_link_libraries(day2_test gtest_main)
target_link_libraries(day3_test gtest_main)
target_link_libraries(day4_test gtest_main)

enable_testing()
add_test(NAME day1_test COMMAND day1_test)
add_test(NAME day2_test COMMAND day2_test)
add_test(NAME day3_test COMMAND day3_test)
add_test(NAME day4_test COMMAND day4_test)

cmake_minimum_required(VERSION 3.15)
project(c_serial)

set(CMAKE_CXX_STANDARD 14)

find_package(Boost 1.55.0 REQUIRED COMPONENTS system filesystem)
include_directories(c_serial ${Boost_INCLUDE_DIRS})



add_executable(c_serial main.cpp)
link_directories(c_serial ${Boost_LIBRARY_DIRS})
target_link_libraries(c_serial ${Boost_LIBRARIES})

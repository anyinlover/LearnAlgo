cmake_minimum_required(VERSION 3.16)
project(LearnAlgo VERSION 0.1.0
                DESCRIPTION "Learn Algorithms"
                LANGUAGES CXX)

#set (CMAKE_CXX_STANDARD 20)
#set (CMAKE_CXX_STANDARD_REQUIRED ON)
set (CMAKE_EXPORT_COMPILE_COMMANDS ON)

#add_library(project_options INTERFACE)
#target_compile_features(project_options INTERFACE cxx_std_20)
#target_compile_options(project_options INTERFACE $<$<CXX_COMPILER_ID:Clang>:-stdlib=libc++ -fexperimental-library>)
#target_compile_options(project_options INTERFACE -stdlib=libc++ -fexperimental-library)

#add_compile_options(-stdlib=libc++ -fexperimental-library)
set(CMAKE_CXX_FLAGS "-std=c++20 -stdlib=libc++ -fexperimental-library")
#set(CMAKE_EXE_LINKER_FLAGS_INIT "-fuse-ld=lld")
add_subdirectory(src)

include(CTest)
enable_testing()

add_executable(main main.cpp)
#target_compile_features(main INTERFACE cxx_std_20)
#target_compile_options(main INTERFACE -stdlib=libc++)
#target_link_libraries(main INTERFACE project_options)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)

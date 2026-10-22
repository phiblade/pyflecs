cmake_minimum_required(VERSION 3.20)
project(pyflecs LANGUAGES C)

# This first distribution targets the 64-bit Unix ABI used by our bindings.
if(NOT CMAKE_SYSTEM_NAME MATCHES "^(Darwin|Linux)$" OR NOT CMAKE_SIZEOF_VOID_P EQUAL 8)
  message(FATAL_ERROR "pyflecs currently supports 64-bit macOS and Linux. Other platforms need binding validation before they can be enabled.")
endif()

# Upstream's amalgamated header defaults to a static build. Change only the
# build-directory copy, preserving the downloaded source and its checksums.
file(READ "${CMAKE_CURRENT_SOURCE_DIR}/vendor/flecs/flecs.h" FLECS_HEADER)
string(REPLACE "#define flecs_STATIC\n" "/* Shared library build. */\n" FLECS_HEADER "${FLECS_HEADER}")
file(MAKE_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/native")
file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/native/flecs.h" "${FLECS_HEADER}")
configure_file(vendor/flecs/flecs.c native/flecs.c COPYONLY)
add_library(flecs SHARED "${CMAKE_CURRENT_BINARY_DIR}/native/flecs.c")
target_compile_features(flecs PRIVATE c_std_99)
target_compile_definitions(flecs PRIVATE flecs_EXPORTS FLECS_NDEBUG)
set_target_properties(flecs PROPERTIES C_VISIBILITY_PRESET hidden)
if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
  find_package(Threads REQUIRED)
  target_link_libraries(flecs PRIVATE Threads::Threads m ${CMAKE_DL_LIBS})
endif()
install(TARGETS flecs LIBRARY DESTINATION pyflecs RUNTIME DESTINATION pyflecs)
install(FILES vendor/flecs/LICENSE DESTINATION pyflecs/licenses RENAME flecs-LICENSE)

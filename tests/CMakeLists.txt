cmake_minimum_required(VERSION 3.8)
add_library(rotor_test_lib STATIC
    access.cpp
    actor_test.cpp
    supervisor_test.cpp
    test-main.cpp
)
target_link_libraries(rotor_test_lib rotor::core)
add_library(rotor::test ALIAS rotor_test_lib)
set(rotor_TEST_LIBS rotor::core rotor::test)

add_executable(007-plugins 007-plugins.cpp)
target_link_libraries(007-plugins ${rotor_TEST_LIBS})
add_test(007-plugins "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/007-plugins")

add_executable(008-config-builder 008-config-builder.cpp)
target_link_libraries(008-config-builder ${rotor_TEST_LIBS})
add_test(008-config-builder "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/008-config-builder")

add_executable(009-system-context 009-system-context.cpp)
target_link_libraries(009-system-context ${rotor_TEST_LIBS})
add_test(009-system-context "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/009-system-context")

add_executable(010-sup-start_stop 010-sup-start_stop.cpp)
target_link_libraries(010-sup-start_stop ${rotor_TEST_LIBS})
add_test(010-sup-start_stop "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/010-sup-start_stop")

add_executable(011-ping_pong 011-ping_pong.cpp)
target_link_libraries(011-ping_pong ${rotor_TEST_LIBS})
add_test(011-ping_pong "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/011-ping_pong")

add_executable(012-actor-lifetime 012-actor-lifetime.cpp)
target_link_libraries(012-actor-lifetime ${rotor_TEST_LIBS})
add_test(012-actor-lifetime "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/012-actor-lifetime")

add_executable(013-observer 013-observer.cpp)
target_link_libraries(013-observer ${rotor_TEST_LIBS})
add_test(013-observer "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/013-observer")

add_executable(014-lifetime-observer 014-lifetime-observer.cpp)
target_link_libraries(014-lifetime-observer ${rotor_TEST_LIBS})
add_test(014-lifetime-observer "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/014-lifetime-observer")

add_executable(015-resources 015-resources.cpp)
target_link_libraries(015-resources ${rotor_TEST_LIBS})
add_test(015-resources "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/015-resources")

add_executable(016-pub_sub 016-pub_sub.cpp)
target_link_libraries(016-pub_sub ${rotor_TEST_LIBS})
add_test(016-pub_sub "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/016-pub_sub")

add_executable(017-req-res 017-req-res.cpp)
target_link_libraries(017-req-res ${rotor_TEST_LIBS})
add_test(017-req-res "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/017-req-res")

add_executable(018-lambda-handlers 018-lambda-handlers.cpp)
target_link_libraries(018-lambda-handlers ${rotor_TEST_LIBS})
add_test(018-lambda-handlers "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/018-lambda-handlers")

add_executable(019-link-unlink 019-link-unlink.cpp)
target_link_libraries(019-link-unlink ${rotor_TEST_LIBS})
add_test(019-link-unlink "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/019-link-unlink")

add_executable(020-two-supervisors 020-two-supervisors.cpp)
target_link_libraries(020-two-supervisors ${rotor_TEST_LIBS})
add_test(020-two-supervisors "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/020-two-supervisors")

add_executable(021-ping_pong-external 021-ping_pong-external.cpp)
target_link_libraries(021-ping_pong-external ${rotor_TEST_LIBS})
add_test(021-ping_pong-external "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/021-ping_pong-external")

add_executable(022-supervisor-tree 022-supervisor-tree.cpp)
target_link_libraries(022-supervisor-tree ${rotor_TEST_LIBS})
add_test(022-supervisor-tree "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/022-supervisor-tree")

add_executable(023-supervisor-children 023-supervisor-children.cpp)
target_link_libraries(023-supervisor-children ${rotor_TEST_LIBS})
add_test(023-supervisor-children "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/023-supervisor-children")

add_executable(024-supervisor-spawner 024-supervisor-spawner.cpp)
target_link_libraries(024-supervisor-spawner ${rotor_TEST_LIBS})
add_test(024-supervisor-spawner "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/024-supervisor-spawner")

add_executable(030-registry 030-registry.cpp)
target_link_libraries(030-registry ${rotor_TEST_LIBS})
add_test(030-registry "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/030-registry")

add_executable(099-misc 099-misc.cpp)
target_link_libraries(099-misc ${rotor_TEST_LIBS})
add_test(099-misc "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/099-misc")

if (BUILD_BOOST_ASIO)
    set(rotor_BOOTS_TEST_LIBS rotor::test rotor::asio)

    if (WIN32)
        add_compile_definitions(
            _SILENCE_CXX17_ALLOCATOR_VOID_DEPRECATION_WARNING
            _WIN32_WINNT=0x600
        )
    endif()

    add_executable(101-asio_ping-pong-1-strand 101-asio_ping-pong-1-strand.cpp)
    target_link_libraries(101-asio_ping-pong-1-strand ${rotor_BOOTS_TEST_LIBS})
    add_test(101-asio_ping-pong-1-strand "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/101-asio_ping-pong-1-strand")

    add_executable(102-asio_ping-pong-2-strands 102-asio_ping-pong-2-strands.cpp)
    target_link_libraries(102-asio_ping-pong-2-strands ${rotor_BOOTS_TEST_LIBS})
    add_test(102-asio_ping-pong-2-strands "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/102-asio_ping-pong-2-strands")

    if (NOT BUILD_THREAD_UNSAFE)
        add_executable(103-asio_ping-pong-2-threads 103-asio_ping-pong-2-threads.cpp)
        target_link_libraries(103-asio_ping-pong-2-threads ${rotor_BOOTS_TEST_LIBS})
        add_test(103-asio_ping-pong-2-threads "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/103-asio_ping-pong-2-threads")
    endif()

    add_executable(104-asio_timer 104-asio_timer.cpp)
    target_link_libraries(104-asio_timer ${rotor_BOOTS_TEST_LIBS})
    add_test(104-asio_timer "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/104-asio_timer")
endif()


if (BUILD_WX)
    find_package(wxWidgets COMPONENTS base core REQUIRED)
    include(${wxWidgets_USE_FILE})

    add_executable(121-wx_ping_ping 121-wx_ping_ping.cpp)
    target_link_libraries(121-wx_ping_ping rotor::test rotor::wx ${wxWidgets_LIBRARIES})
    add_test(121-wx_ping_ping "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/121-wx_ping_ping")

    add_executable(122-wx_timer 122-wx_timer.cpp)
    target_link_libraries(122-wx_timer rotor::test rotor::wx ${wxWidgets_LIBRARIES})
    add_test(122-wx_timer "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/122-wx_timer")
endif()


if (BUILD_EV)
    add_executable(131-ev_ping-pong 131-ev_ping-pong.cpp)
    target_link_libraries(131-ev_ping-pong rotor::test rotor::ev)
    add_test(131-ev_ping-pong "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/131-ev_ping-pong")

    add_executable(132-ev_timer 132-ev_timer.cpp)
    target_link_libraries(132-ev_timer rotor::test rotor::ev)
    add_test(132-ev_timer "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/132-ev_timer")
endif()

if (BUILD_THREAD)
    add_executable(141-thread_ping-pong 141-thread_ping-pong.cpp)
    target_link_libraries(141-thread_ping-pong rotor::test rotor::thread)
    add_test(141-thread_ping-pong "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/141-thread_ping-pong")

    add_executable(142-thread_timer 142-thread_timer.cpp)
    target_link_libraries(142-thread_timer rotor::test rotor::thread)
    add_test(142-thread_timer "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/142-thread_timer")

    add_executable(143-thread-shutdown_flag 143-thread-shutdown_flag.cpp)
    target_link_libraries(143-thread-shutdown_flag rotor::test rotor::thread)
    add_test(143-thread-shutdown_flag "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/143-thread-shutdown_flag")
endif()

execute_process(COMMAND "/home/king/catkin_ws/build/hexaurdf10/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/king/catkin_ws/build/hexaurdf10/catkin_generated/python_distutils_install.sh) returned error code ")
endif()

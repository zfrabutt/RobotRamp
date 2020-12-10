rosservice call gazebo/delete_model bb_8
rosservice call gazebo/delete_model dd_robot
rosrun gazebo_ros spawn_model -file model.sdf -sdf -model dd_robot -y 0 -x 0 -z 1.0

rosservice call gazebo/delete_model final_setup
rosrun gazebo_ros spawn_model -file final/final.sdf -sdf -model final_setup -y -0.0 -x -0.0 -z 0.0

python robotMovement.py &
python keyboardInput.py
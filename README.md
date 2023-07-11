## test trimesh/trimesh collision gazebo-classic

The issue is the trimesh/trimesh collision unstable with ode/bullet physics.

## How to run

Start the launch with a physics engine and spawn trimeshes.

### ODE

    roslaunch trimesh_collision_gazebo empty_world_ode.launch 

    rosrun trimesh_collision_gazebo spawn_trimesh.py 2

### BULLET

    roslaunch trimesh_collision_gazebo empty_world_bullet.launch

    rosrun trimesh_collision_gazebo spawn_trimesh.py 2

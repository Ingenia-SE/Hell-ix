# Drone Simulation

This repository contains all simulation files needed to simulate the Crazyflie 2.1 using ROS Noetic and Gazebo 11. The simulation environment is containerized in docker to ensure portability among devices.

## Prerequisites

1. Use Ubuntu 20.04
2. Install docker: https://docs.docker.com/engine/install/ubuntu/
3. If using an Nvidia GPU, follow steps 1 and 2 of this guide: https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_common/blob/main/docs/dev-env-setup.md

## Installation

1. Clone the git repo:

    ```bash
    gh repo clone Ingenia-SE/Hell-ix
    cd Hell-ix/software/simulation/base
    ```

2. Build the image:

    ```bash
    docker build -t crazy_noetic .
    ```

3. Open ~/.bashrc or ~/.zshrc and add the following line at the end. In the case of not using an Nvidia, remove ```--gpus all``` as well as ```--env="NVIDIA_DRIVER_CAPABILITIES=all"```.

    ```bash
    alias crazy-noetic='xhost + && docker run -it --rm --cap-add=ALL --privileged --net=host --gpus all --env="NVIDIA_DRIVER_CAPABILITIES=all" --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --volume="/home/$USER:/home/$USER" --volume="/lib/modules:/lib/modules" --workdir="/home/$USER" crazy_noetic'
    ```

4. Now open a terminal and type ```crazy-noetic```. The container should open without errors. To test the installation, run the following line. If everything is OK, gazebo will open and the drone will appear flying:
   
   ```bash
    roslaunch rotors_gazebo crazyflie2_hovering_example.launch
    ```
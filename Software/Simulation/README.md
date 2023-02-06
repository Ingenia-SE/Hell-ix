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
2. Create a volume to hold the installation. All installation related files should be found in ```/home/ros```.

    ```bash
    docker volume create ros-noetic-volume
    ```

3. Build the image:

    ```bash
    docker build -t crazy_noetic .
    ```

4. Open ~/.bashrc or ~/.zshrc and add the following line at the end. In the case of not using an Nvidia, remove ```--gpus all``` as well as ```--env="NVIDIA_DRIVER_CAPABILITIES=all"```.

    ```bash
    alias crazy-noetic='xhost + && docker run -it --rm --cap-add=ALL --privileged --net=host --gpus all --env="NVIDIA_DRIVER_CAPABILITIES=all" --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --volume="/home/$USER:/home/$USER" --volume="/lib/modules:/lib/modules" --workdir="/home/$USER" crazy_noetic'
    ```

5. Now open a terminal and type ```crazy-noetic```. The container should open without errors. To test the installation, run the following line. If everything is OK, gazebo will open and the drone will appear flying:
   
   ```bash
    roslaunch rotors_gazebo crazyflie2_hovering_example.launch
    ```

## Next steps

Once inside the container, the usage is exactly the same as if working in a terminal. The /home/user folder is shared with the host computer, so changes there will be permanent. Changes in other folders will not persist when docker is closed ```ctrl+D```. 

Installed programmes will not persist either. In order to install a program inside the container, the best procedure is to add the installation to the Dockerfile and rebuild the image (Step 2). For example, if you need to use ```neofetch```, add the following line at the end of the Dockerfile:

```Dockerfile
RUN apt-get install neofetch -y
```

Development should be performed inside the /home/user folder, creating a workspace as explained here: https://industrial-training-master.readthedocs.io/en/melodic/_source/session1/Create-Catkin-Workspace.html. Once a package is completed, it can be uploaded to the repository, and then it should be included in the Dockerfile so that everyone can install it in their container.
% ========================================================================
% RACE TRAJECTORY PLANNER
% ========================================================================
% - Project: INGENIA-SE Autonomous Drone Racing Challenge 2022-2023
% - Author: Hell-ix. https://ingenia-se.github.io/Hell-ix/
% - Date: 23rd May 2023
% ========================================================================
% DESCRIPTION:
%
% This file enables the  generation of a .csv file with the 3D coordinates
% of the  optimal trajectory that  the drone must follow in  order to pass
% through  a set of  given  gates. The  program enables  to  determine the
% optimal trajectory by defining the center points through which the drone
% should pass, as well as other parameters such as  the direction in which
% it should pass  each of the gates. The trajectory can also be  optimized
% as  a function of the  ratio power to  weight  of the drone,  that  will 
% define  how  sharp  these  trajectories corners  can be. This is done by 
% modifying what's called the "tension" on each of the gates.
%
% The   program  uses  the  function  hobbysplines.m  developped  by  Will 
% Robertson and The University of Adelaide. This  function employs Hobby's
% algorithm for choosing  control points based on curvature and tension in
% order to draw 3D Bezier curves.
%
% ========================================================================

% Create a global variable to store the 3D coordinates list
global trajectory;

% Specify the number of gates to pass:
N = 4;
trajectory = zeros(50 * N, 3);

% Create a figure to plot the obtained trajectories and the gates
fig = figure(1);
    set(fig, 'color', [0 0 0], 'name', '3D spline example');
    clf; 
    hold on;
    axis equal;
    ax = gca;
    ax.Color = 'black';
    ax.XColor = 'white';
    ax.YColor = 'white';
    ax.ZColor = 'white';
    ax.XLim = [-1, inf];
    ax.YLim = [-3, inf];
    ax.ZLim = [0, inf];
    view(3);

% Specification of the four points where the gates' centers are located. 
% They can be modified if the points do not define a circle.

R = 3; 

gate_loc = [[  -R*cos(deg2rad(0))+R,   R*sin(deg2rad(0)), 1.5]; ...
            [ -R*cos(deg2rad(60))+R,  R*sin(deg2rad(60)), 3]; ...
            [-R*cos(deg2rad(120))+R, R*sin(deg2rad(120)), 1]; ...
            [-R*cos(deg2rad(180))+R, R*sin(deg2rad(180)), 1.5]];

% Specification of the velocity vectors of the drone when passing through
% the center of the gates
vel_vec = [[0, 1, 0]; [sqrt(3)/2, 0.5, 0]; [sqrt(3)/2, -0.5, 0];
           [0, -1, 0]];

% Specification of the tension (ratio power-to-weight) of the drone
tension = 1;

% Specification of the dimensions of the side of the square gate
side = 1.4;

specs = cell(1, N);

if (length(gate_loc) == N) && (length(vel_vec) == N)
    for i = 1:N
        specs{i} = {gate_loc(i, :), vel_vec(i, :), tension};
        % Plot the gates through which the drone has to pass
        plotGate(gate_loc(i, :), vel_vec(i, :), side);
    end
else
    error("Revise that you have correctly defined positions and velocities for all the gates.");
end

% Plot the trajectory according to the given specifications
hobbysplines(specs, 'debug', true, 'cycle', true, 'color', 'red');

x = trajectory(:, 1);
y = trajectory(:, 2);
trajectory(:, 4) = zeros(1, length(x));
for i = 2:length(x) - 1
    dx = x(i + 1) - x(i - 1);
    dy = y(i + 1) - y(i - 1);
    trajectory(i, 4) = -rad2deg(atan2(dx, dy));
end

writematrix(trajectory,'trajectory.csv')

function plotGate(center, vector, side)
% ========================================================================
% - Project: INGENIA-SE Autonomous Drone Racing Challenge 2022-2023
% - Author: Hell-ix. https://ingenia-se.github.io/Hell-ix/
% - Date: 23rd May 2023
% ========================================================================
% Description:
%
% The following  function  allows to  plot the gate in 3D depending  given
% the  values  for the position of  the  center of  the gate,  the  vector 
% normal to the surface of the gate and the  side of it. Take into account
% that this code plots square gates.
% ========================================================================

% Normalize the vector in case it is not already normalized
vector_2D = [vector(1), vector(2)];
normal_vector = vector_2D/norm(vector_2D);

% Calculate the perpendicular vector to the one normal to the surface
perp_vector = [-normal_vector(2), normal_vector(1)];

% Calculate the four corners of the square gate
corners = [[center(1:2) + side/2*perp_vector, center(3) - side/2];
           [center(1:2) - side/2*perp_vector, center(3) - side/2];
           [center(1:2) - side/2*perp_vector, center(3) + side/2];
           [center(1:2) + side/2*perp_vector, center(3) + side/2]];

% Plot the four corners, as well as the union of the gate to the ground
for i=1:4
    plot3([corners(i, 1), corners(mod(i, 4) + 1, 1)], ...
          [corners(i, 2), corners(mod(i, 4) + 1, 2)], ...
          [corners(i, 3), corners(mod(i, 4) + 1, 3)], 'w-', ...
          'LineWidth', 2);
end

union = [mean([corners(1,1), corners(2,1)]), ...
         mean([corners(1,2), corners(2,2)]), corners(1, 3)];

plot3([union(1), union(1)], [union(2), union(2)], [union(3), 0], ...
      'w-', 'LineWidth', 2);

end

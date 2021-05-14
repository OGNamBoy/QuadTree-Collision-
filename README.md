# QuadTree-Collision

This visualization of quadTree collissions constantly updates the quadTree, showing the subdivisions with green lines. Each point starts off red, and when they collide, they turn blue.

init.py and collisions.py are the same except for slightly different particle behavior. In collisions.py, the particles migrate to one end of the screen, which may help visualize the subdivisions of the quadTree

testing.py takes mouse input from the user and adds a point to the quadTree. Note that even though the max amount of points the quadTree will hold before it subdivides is 4, visually it may look like it takes more than 4 points for the quadTree to subdivide. This is because some points that visually appear to be in a certain quadTree are instead held by one of the parent quadTrees.

classes.py simply holds all the classes used in the main files.

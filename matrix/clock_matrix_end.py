import pymel.core as pm
import math

pm.newFile(force=True)
hand = pm.polyCube()[0]
frame = 1

# we're going to create 4 matrices
# S, T1, R, T2
# pymel has a special "Matrix" datatype for working with matrices
# So far we only used built in datatypes (strings, ints, floats...)
# We define a matrix by passing 16 floats!

for frame in range(200):
    pm.currentTime(frame)
    # scale it down skinny in both sx and sz
    S = pm.dt.Matrix(
        0.1, 0.0, 0.0, 0.0,
        0.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 0.1, 0.0,
        0.0, 0.0, 0.0, 1.0
        )
    # raise it up ty so it sits on the origin
    T1 = pm.dt.Matrix(
        1.0, 0.0, 0.0, 0.0,
        0.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0,
        0.0, 0.5, 0.0, 1.0
        )
    # rotate it around the origin in rz
    # work out how far a second hand moves in 1/24th of a second
    a = math.radians(360/60/24.0*frame) * -1
    R = pm.dt.Matrix(
        math.cos(a), math.sin(a), 0.0, 0.0,
        -math.sin(a), math.cos(a), 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 1.0
        )
    # move it into position in the scene
    # worldspace (say, (9, 11, -6))
    T2 = pm.dt.Matrix(
        1.0, 0.0, 0.0, 0.0,
        0.0, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0,
        9.0, 11.0, -6.0, 1.0
        )

    # maya uses row vectors rather than column vectors
    # which means we need to pre-multiply rather
    # than post-multiply the matrices. In most 
    # maths books the order of multiplication
    # would be reversed (column major)
    pm.currentTime(frame)
    hand.setMatrix(S*T1*R*T2)
    pm.setKeyframe(hand)


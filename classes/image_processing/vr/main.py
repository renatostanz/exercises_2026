from alligator import Alligator, dance
import pyvista as pv

if __name__ == "__main__":
    plotter = pv.Plotter()

    hostigator = Alligator()
    core = hostigator.create_core()
    right_leg, left_leg = hostigator.create_legs()
    right_arm, left_arm = hostigator.create_arms()
    tail = hostigator.create_tail()
    back = hostigator.create_back()
    mouth = hostigator.create_mouth()

    blue = [0, 0, 230]
    yellow = [250, 250, 30]

    plotter.add_mesh(core, color = yellow, label = "Body")
    plotter.add_mesh(left_leg, color = blue, label = "Left Foot")
    plotter.add_mesh(right_leg, color = blue, label = "Right Foot")
    plotter.add_mesh(left_arm, color = blue, label = "Left Arm")
    plotter.add_mesh(right_arm, color = blue, label = "Right Arm")
    plotter.add_mesh(tail, color = blue, label = "Tail")
    plotter.add_mesh(back, color = blue, label = "Back")
    plotter.add_mesh(mouth, color = yellow, label = "Back")

    plotter.add_axes(interactive=True, line_width=3)
    #plotter.show_grid()

    plotter.enable_point_picking(
        callback=dance,
        show_point=False,
        left_clicking=True,
        show_message="Click in the Hostigator to make it dance!"
    )

    plotter.show()

import pyvista as pv

class Alligator:
    def __init__(self):
        self.core_dimensions: tuple[float, float, float] = (4.0, 3.0, 6.0)

        self.thigh_height: float = 2.0
        self.thigh_radius: float = 1.0
        self.foot_height: float = 0.25
        self.foot_radius: float = self.thigh_radius * 1.05

        self.foot_center = (self.foot_radius / 2, self.foot_radius / 2, self.foot_height / 2)

        self.tail_height: float = 3.0
        self.tail_radius: float = 0.5

        self.arm_height: float = 2.5
        self.arm_radius: float = 1.25

    def create_core(self) -> pv.PolyData:
        center = tuple(i/2 for i in self.core_dimensions)
        body = pv.Cube(
            center = center, 
            x_length = self.core_dimensions[0], 
            y_length = self.core_dimensions[1], 
            z_length = self.core_dimensions[2]
        )
        body.translate(center, inplace=True)
        return body


    def place_limb(
        self,
        geometry: pv.PolyData, 
        rot_deg_xyz: tuple[float, float, float] = (0, 0, 0), 
        translation=(0, 0, 0)
    ) -> pv.PolyData:

        if rot_deg_xyz[0] != 0:
            geometry.rotate_x(rot_deg_xyz[0], inplace=True)
        if rot_deg_xyz[1] != 0:
            geometry.rotate_y(rot_deg_xyz[1], inplace=True)
        if rot_deg_xyz[2] != 0:
            geometry.rotate_z(rot_deg_xyz[2], inplace=True)
        
        geometry.translate(translation, inplace=True)
        return geometry


    def create_legs(self) -> tuple[pv.PolyData, pv.PolyData]:
        cone_center = (self.thigh_radius / 2, self.thigh_radius / 2, 2 * self.thigh_height / 3)
        leg = pv.Cone(
            height = self.thigh_height, 
            radius = self.thigh_radius, 
            center = cone_center, 
            direction = (0, 0, 1)
        )


        foot = pv.Cylinder(
            center = self.foot_center, 
            direction = [0, 0, 1],
            radius = self.foot_radius, height=self.foot_height
        )

        leg = pv.merge([foot, leg])

        delta_z = 3*self.core_dimensions[2] / 5 - (self.foot_height + self.thigh_height)
        delta_y = 5*self.core_dimensions[1]/4
        left_translation = (4*self.core_dimensions[0]/3, delta_y, delta_z)
        right_translation = (2*self.core_dimensions[0]/5, delta_y, delta_z)

        return (
            self.place_limb(translation=left_translation, rot_deg_xyz=(15, 0, -15), geometry=leg.copy()),
            self.place_limb(translation=right_translation, rot_deg_xyz=(15, 0, 15), geometry=leg),
        )


    def create_arms(self) -> tuple[pv.PolyData, pv.PolyData]:
        cone_center = (0, 0, 0)
        arm = pv.Cone(
            height = self.arm_height, 
            radius = self.arm_radius, 
            center = cone_center, 
            direction = (0, 0, 1)
        )

        delta_z = 3 * self.core_dimensions[2] / 2 - self.arm_radius 
        delta_y = self.core_dimensions[1] + self.arm_radius / 2
        left_translation = (7*self.core_dimensions[0]/4, delta_y, delta_z)
        right_translation = (2*self.core_dimensions[0]/7, delta_y, delta_z)
        return (
            self.place_limb(translation=left_translation, rot_deg_xyz=(0, -90, 0), geometry=arm.copy()),
            self.place_limb(translation=right_translation, rot_deg_xyz=(0, 90, 0), geometry=arm),
        )


    def create_tail(self) -> pv.PolyData:
        cone_center = (self.tail_radius / 2, self.tail_radius / 2, 3 * self.tail_height / 2)
        tail = pv.Cone(
            height = self.tail_height, 
            radius = self.tail_radius, 
            center = cone_center, 
            direction = (0, 0, 1)
        )

        delta_x = self.core_dimensions[0] - self.tail_radius
        translation = (delta_x, 3 * self.core_dimensions[1] / 2,  3 * self.core_dimensions[2] / 4)
        return self.place_limb(translation=translation, rot_deg_xyz=(120, 0, 00), geometry=tail)



plotter = pv.Plotter()

hostigator = Alligator()
core = hostigator.create_core()
right_leg, left_leg = hostigator.create_legs()
right_arm, left_arm = hostigator.create_arms()
tail = hostigator.create_tail()

plotter.add_mesh(core, color=[250, 250, 30], label="Body")
plotter.add_mesh(left_leg, color=[0, 0, 230], label="Left Foot")
plotter.add_mesh(right_leg, color=[0, 0, 230], label="Right Foot")
plotter.add_mesh(left_arm, color=[0, 0, 230], label="Left Arm")
plotter.add_mesh(right_arm, color=[0, 0, 230], label="Right Arm")
plotter.add_mesh(tail, color=[0, 0, 230], label="Tail")

plotter.add_axes(interactive=True, line_width=3)
plotter.show_grid()

plotter.show()

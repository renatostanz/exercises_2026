from numpy import ndarray
from time import sleep

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
        center = (self.core_dimensions[0] / 2, self.core_dimensions[1] / 6, self.core_dimensions[2] / 2)
        body = pv.Cube(
            center = center, 
            x_length = self.core_dimensions[0], 
            y_length = self.core_dimensions[1] / 3, 
            z_length = self.core_dimensions[2]
        )
        translation = (center[0], 7 * self.core_dimensions[1] / 6, center[2])
        body.translate(translation, inplace=True)
        return body


    def place_limb(
        self,
        limb: pv.PolyData, 
        rot_deg_xyz: tuple[float, float, float] = (0, 0, 0), 
        translation=(0, 0, 0)
    ) -> pv.PolyData:

        if rot_deg_xyz[0] != 0:
            limb.rotate_x(rot_deg_xyz[0], inplace=True)
        if rot_deg_xyz[1] != 0:
            limb.rotate_y(rot_deg_xyz[1], inplace=True)
        if rot_deg_xyz[2] != 0:
            limb.rotate_z(rot_deg_xyz[2], inplace=True)
        
        limb.translate(translation, inplace=True)
        return limb


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

        delta_z = self.core_dimensions[2] / 2 - (self.foot_height + self.thigh_height)
        delta_y = 5 * self.core_dimensions[1] / 4
        right_translation = (4 * self.core_dimensions[0] / 3, delta_y, delta_z)
        left_translation = (2 * self.core_dimensions[0] / 5, delta_y, delta_z)

        return (
            self.place_limb(translation=right_translation, rot_deg_xyz=(15, 0, -15), limb=leg.copy()),
            self.place_limb(translation=left_translation, rot_deg_xyz=(15, 0, 15), limb=leg),
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
        right_delta_x = 3 * self.core_dimensions[0] / 2 + self.arm_height / 3
        left_delta_x = self.core_dimensions[0] / 2 - self.arm_height / 3

        right_translation = (right_delta_x, delta_y, delta_z)
        left_translation = (left_delta_x, delta_y, delta_z)

        return (
            self.place_limb(translation=right_translation, rot_deg_xyz=(0, -90, 45), limb=arm.copy()),
            self.place_limb(translation=left_translation, rot_deg_xyz=(0, 90, -45), limb=arm),
        )


    def create_tail(self) -> pv.PolyData:
        cone_center = (self.tail_radius / 2, self.tail_radius / 2, self.tail_height / 2)
        tail = pv.Cone(
            height = self.tail_height, 
            radius = self.tail_radius, 
            center = cone_center, 
            direction = (0, 0, 1)
        )

        delta_x = self.core_dimensions[0] - self.tail_radius
        translation = (delta_x, 4 * self.core_dimensions[1] / 7,  self.core_dimensions[2] / 2 + self.tail_radius)
        return self.place_limb(translation=translation, rot_deg_xyz=(120, 0, 00), limb=tail)


    def create_back(self) -> pv.PolyData:
        
        center = (self.core_dimensions[0] / 2, self.core_dimensions[1] / 3, 3 * self.core_dimensions[2] / 4)
        back = pv.Cube(
            center = center, 
            x_length = self.core_dimensions[0], 
            y_length = 2 * self.core_dimensions[1] / 3, 
            z_length = 3 * self.core_dimensions[2] / 2
        )

        traslation = (self.core_dimensions[0] / 2, self.core_dimensions[1] / 2, self.core_dimensions[2] / 2)
        back.translate(traslation, inplace=True)

        return back


    def create_mouth(self) -> pv.PolyData:
        center = (self.core_dimensions[0] / 2, self.core_dimensions[1] / 3, self.core_dimensions[2] / 12)
        chin = pv.Cube(
            center = center, 
            x_length = self.core_dimensions[0], 
            y_length = 2 * self.core_dimensions[1] / 3, 
            z_length = self.core_dimensions[2] / 6
        )

        center = (self.core_dimensions[0] / 2, self.core_dimensions[1] / 3 + self.core_dimensions[2] / 6, self.core_dimensions[2] / 12)
        nose = pv.Cube(
            center = center, 
            x_length = self.core_dimensions[0], 
            y_length = 2 * self.core_dimensions[1] / 3 + self.core_dimensions[2] / 3, 
            z_length = self.core_dimensions[2] / 6
        )
        nose.rotate_x(45, inplace=True)

        mouth = pv.merge([chin, nose])

        traslation = (self.core_dimensions[0] / 2, 7 * self.core_dimensions[1] / 6, 3 * self.core_dimensions[2] / 2 - self.core_dimensions[2] / 12)
        mouth.translate(traslation, inplace=True)

        return mouth

def dance(point: ndarray) -> None:
    number_of_frames = 30

    for f in range(number_of_frames):
        i = 1
        if f < number_of_frames // 2:
            i *= -1

        left_arm.rotate_x(i, inplace=True)
        right_arm.rotate_z(-i, inplace=True)

        if f < 10 or f >= number_of_frames - 11:
            right_leg.rotate_z(-i, inplace=True)
        left_leg.rotate_z(i, inplace=True)

        tail.rotate_z(-i, inplace=True)

        plotter.render()
        sleep(0.02)



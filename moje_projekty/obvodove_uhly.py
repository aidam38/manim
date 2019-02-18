from big_ol_pile_of_manim_imports import *


class a(Scene):
    def construct(self):
        title = TextMobject("Obvodové a středové úhly", tex_to_color_map={
                            "Obvodové": YELLOW, "středové": RED})
        title.scale(1.5)
        title.to_edge(UP)
        self.add(title)
        self.title = title

        alpha = 35/360*TAU
        circle1 = Arc(color=WHITE, angle=TAU-2*alpha,
                      start_angle=alpha-TAU/4, radius=2)
        circle2 = Arc(color=YELLOW, angle=2*alpha,
                      start_angle=alpha-TAU/4-2*alpha, radius=2)
        center_dot = Dot(circle1.get_center(), color=WHITE)

        A = Dot(circle1.point_from_proportion(0), color=RED)
        B = Dot(circle1.point_from_proportion(1), color=RED)
        C = Dot(circle1.point_from_proportion(0.75), color=YELLOW)
        line1 = Line(A, C)
        line2 = Line(B, C)

        self.play(ShowCreation(circle1), ShowCreation(
            circle2), ShowCreation(center_dot))
        self.play(ShowCreation(A), ShowCreation(B), ShowCreation(
            C), ShowCreation(line1), ShowCreation(line2))

        print(str(circle1.point_from_proportion(0.5)))
        self.play(C.move_to, circle1.point_from_proportion(0.5))

        self.wait(5)

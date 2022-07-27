from cmath import e
from manim import *
from numpy import arccos 

class PointMovingOnShapes(Scene):
    
    def grid(self):
        for i in range(-10,10):
            l1 = Line(ORIGIN + i * RIGHT - 10 * UP, ORIGIN + i * RIGHT + 10 * UP, color=BLUE)
            self.add(l1)
            l1 = Line(ORIGIN -10 * RIGHT + i * UP, ORIGIN +10 * RIGHT + i * UP, color=BLUE)
            self.add(l1)
    
    def intro(self):
        photo = ImageMobject("resources/Pythagoras.png").scale(0.9).shift(ORIGIN+2.67*DOWN)
        self.play(GrowFromPoint(photo, ORIGIN) )

        pyt = Text('Pythagoras').shift(ORIGIN+1*DOWN).scale(2)
        theorem = Text('Teorema').shift(ORIGIN+1*UP).scale(2)
        self.play(Write(pyt))
        self.play(Write(theorem))
        self.remove(theorem,pyt)
        self.play((photo).animate.scale(15,about_point=ORIGIN))
        self.play(FadeOut(photo))

        



    def construct(self):

        self.intro()
        
        recenter = 1.5 * DOWN
        equation = MathTex("x^2+y^2", "=", "z^2").scale(2)
        self.play(Write(equation))
        self.wait()
        self.remove(equation)

        #self.grid()

        l1 = Line(ORIGIN - 2 * RIGHT + recenter, ORIGIN + 2 * RIGHT + recenter, color=BLUE)
        l2 = Line(ORIGIN + 2 * RIGHT + recenter, ORIGIN - 2 * RIGHT + 3 * UP + recenter, color=BLUE)
        l3 = Line(ORIGIN - 2 * RIGHT + 3 * UP + recenter, ORIGIN - 2 * RIGHT + recenter, color=BLUE)
        self.play(GrowFromPoint(l1, l1.start))
        self.play(GrowFromPoint(l2, l2.start))
        self.play(GrowFromPoint(l3, l3.start))
        self.wait()

        sq1 = Square(4).shift(DOWN*2 + recenter)
        self.play(GrowFromEdge(sq1, edge=UP))
        sq2 = Square(3).shift(LEFT*1.5+LEFT*2+ UP * 1.5 + recenter)
        self.play(GrowFromEdge(sq2, edge=RIGHT))
        l3angle = (-180+l2.get_angle()*180/PI)*DEGREES
        sq3 = Square(5).shift(ORIGIN+0.5*LEFT+2.5*UP + recenter).rotate(l3angle,about_point=l2.start)
        self.play(GrowFromEdge(sq3, edge=DOWN))
        self.wait()
        equationx = MathTex("x^2").shift(ORIGIN+sq1.get_center())
        self.play(Write(equationx))
        equationy = MathTex("y^2").shift(ORIGIN+sq2.get_center())
        self.play(Write(equationy))
        equationz = MathTex("z^2").shift(ORIGIN+sq3.get_center())
        self.play(Write(equationz))
        self.wait()
        self.remove(l1)
        self.remove(l2)
        self.remove(l3)
        
        gx = VGroup(sq1,equationx)
        self.play((gx).animate.shift(-sq1.get_center()+5*LEFT))

        gy = VGroup(sq2,equationy)
        self.play((gy).animate.shift(-sq2.get_center()+0.5*LEFT))

        self.play((sq3).animate.rotate(-l3angle))
        gz = VGroup(sq3,equationz)
        self.play((gz).animate.shift(-sq3.get_center()+4.5*RIGHT))

        equationp = MathTex("+").shift(ORIGIN - 2.5 * RIGHT)
        self.play(Write(equationp))
        equatione = MathTex("=").shift(ORIGIN + 1.5 * RIGHT)
        self.play(Write(equatione))

        self.play((sq1).animate.set_fill(YELLOW, opacity=0.5))
        self.play((sq2).animate.set_fill(BLUE, opacity=0.5))
        self.play((sq3).animate.set_fill(RED, opacity=0.5))
        self.remove(equationp)
        self.remove(equatione)

        self.play((gx).animate.shift(-sq1.get_center()+5*LEFT + 2 * UP))
        self.play((gy).animate.shift(-sq2.get_center()+5*LEFT + 2 * DOWN))
        self.play((gz).animate.shift(-sq3.get_center()))

        self.remove(equationx)
        self.remove(equationz)

        self.play((gx).animate.shift(-sq1.get_center()+0.5*LEFT + 0.5 * DOWN))

        sq2_1 = Rectangle(height=3,width=1).shift(sq2.get_center()+1*LEFT)
        sq2_2 = Rectangle(height=3,width=1).shift(sq2.get_center()+0*LEFT)
        sq2_3 = Rectangle(height=2,width=1).shift(sq2.get_center()+1*RIGHT+0.5*DOWN)
        sq2_4 = Rectangle(height=1,width=1).shift(sq2.get_center()+1*RIGHT+1*UP)
        self.play(GrowFromEdge(sq2_1, edge=LEFT))
        self.play(GrowFromEdge(sq2_2, edge=LEFT))
        self.play(GrowFromEdge(sq2_3, edge=DOWN))
        self.add(sq2_4)
        self.play((sq2).animate.set_fill(BLUE, opacity=0.0),
            sq2_1.animate.set_fill(BLUE, opacity=0.5),
            sq2_2.animate.set_fill(BLUE, opacity=0.5),
            sq2_3.animate.set_fill(BLUE, opacity=0.5),
            sq2_4.animate.set_fill(BLUE, opacity=0.5) )
        self.remove(sq2)
        self.remove(equationx)
        self.remove(equationy)
        self.remove(equationz)

        self.play((sq2_1).animate.shift(-sq2_1.get_center()+2*RIGHT + 1 * DOWN),
            (sq2_2).animate.rotate(90*DEGREES).shift(-sq2_2.get_center()+1*LEFT + 2 * UP),
            (sq2_3).animate.shift(-sq2_3.get_center()+2*RIGHT + 1.5 * UP),
            (sq2_4).animate.shift(-sq2_4.get_center()+1*RIGHT + 2 * UP))

        self.wait(4)

        equationy = equationy.shift(-equationy.get_center()-0.5*RIGHT)

        self.play((gx).animate.shift(-sq1.get_center()+5*LEFT),
            (gz).animate.shift(-sq3.get_center()+4.5*RIGHT),
            (sq2_1).animate.shift(-sq2_1.get_center()+1.5*LEFT + 0 * DOWN),
            (sq2_2).animate.rotate(-90*DEGREES).shift(-sq2_2.get_center()+0.5*LEFT + 0 * DOWN),
            (sq2_3).animate.shift(-sq2_3.get_center()+0.5*RIGHT + 0.5 * DOWN),
            (sq2_4).animate.shift(-sq2_4.get_center()+0.5*RIGHT + 1 * UP),
            (equationy).animate,
            (equationp).animate, (equatione).animate)

        self.wait(10)

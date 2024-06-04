
"""
The SOLID principles are
- Single Responsibility Principle
- Open/Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle

in this example we will see the Open/Closed Principle
this principle encourages us to write classes that are open for extension but closed for modification
in this case we have a class called Form that have a method called render, this method will return a string
so if we need something like a triangle or a square we can create a class that inherits from Form and override
instead to modify the Form class
"""


class Form:
    def render_form(self):
        return "This a form"

    def is_this_a_geometry_form(self):
        return True


class Triangle(Form):
    def render_form(self):
        return 'This is a triangle'


class Square(Form):
    def render_form(self):
        return 'This is a square'


if __name__ == '__main__':
    form = Form()
    print(form.render_form())
    print(form.is_this_a_geometry_form())

    triangle = Triangle()
    print(triangle.render_form())
    print(triangle.is_this_a_geometry_form())

    square = Square()
    print(square.render_form())
    print(square.is_this_a_geometry_form())
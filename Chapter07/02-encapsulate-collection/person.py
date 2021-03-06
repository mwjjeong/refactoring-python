class Person:
    def __init__(self, name) -> None:
        self._name = name
        self._courses = []

    @property
    def name(self):
        return self._name

    @property
    def courses(self):
        return list(self._courses)

    @courses.setter
    def courses(self, new_courses):
        self._courses = list(new_courses)

    def add_course(self, course):
        self._courses.append(course)

    def remove_course(self, course):
        idx = self._courses.index(course)
        del self._courses[idx]

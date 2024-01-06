classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]


def add_student(name, email=None):
    if email is None:
        email = f"{name.lower()}@example.com"
    student = {'name': name, 'email': email, 'grades': []}
    classroom.append(student)


def delete_student(name):
    index = index_student(name)
    if index != -1:
        del classroom[index]


def set_email(name, email):
    index = index_student(name)
    if index != -1:
        classroom[index]['email'] = email


def add_grade(name, profession, grade):
    index = index_student(name)
    if index != -1:
        classroom[index]['grades'].append((profession, grade))


def avg_grade(name, profession):
    total_grades = 0
    count = 0
    index = index_student(name)
    if index != -1:
        for subject, grade in classroom[index]['grades']:
            if subject == profession:
                total_grades += grade
                count += 1
        if count != 0:
            return total_grades / count
        return None


def get_professions(student_name):
    professions = set(),
    for student in classroom:
        if student['name'] == student_name:
            for profession, _ in student['grades']:
                professions.add(profession)
    return professions


def index_student(name):
    for index, student in enumerate(classroom):
        if student['name'] == name:
            return index
    return -1

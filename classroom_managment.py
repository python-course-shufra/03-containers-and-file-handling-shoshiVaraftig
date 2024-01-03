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
    pass

def delete_student(name):
    """Delete a student from the classroom"""
    index=index_student(name)
    del classroom[index]
    pass


def set_email(name, email):
    """Sets the email of the student"""
    index=index_student(name)
    classroom[index]['email']=email
    pass

def add_grade(name, profession, grade):

    index=index_student(name)
    classroom[index]['grades'].append({'profession': profession, 'grade': grade})
    pass
def avg_grade(name, profession):
   avg=0
   count=0
   index=index_student(name)
   for item in classroom[index]['grades']:
       if item['profession'] == profession:
           avg+=item['grade']
           count+=1
   return avg/count
       pass

def get_professions(student_name):
    professions = set()
    
    for student in classroom:
        if student['name'] == student_name:
            for grade in student['grades']:
                subject = grade[0]
                professions.add(subject)
    
    return professions

            pass
def index_student(name):
    count=-1
    for name in classroom:
        count+=1
        if name==name:
            return count
    return -1
        pass

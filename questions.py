SETS = {

    # ============================================================
    # SET 1
    # ============================================================
    1: {
        "name": "Set 1",
        "password": "123",
        "questions": [
            {'id': 4,
 'title': 'Student Result & Grade Analyzer',
 'difficulty': 'Medium',
 'marks': 10,
 'description': '\n'
                'Debug the student result and grade analyzer.\n'
                '\n'
                'A student fails if ANY subject mark is below 40.\n'
                '\n'
                'Grade rules:\n'
                'A -> Average >= 75 and student passed all subjects\n'
                'B -> Average >= 60 and student passed all subjects\n'
                'C -> Average >= 50 and student passed all subjects\n'
                'F -> Otherwise\n'
                '\n'
                'Find and correct all the errors in the program.\n',
 'code': 'students = {\n'
         '    "Arun": [85, 76, 92],\n'
         '    "Bala": [45, 55, 48],\n'
         '    "Charan": [90, 88, 95]\n'
         '    "Divya": [35, 42, 39]\n'
         '}\n'
         '\n'
         'PASS_MARK = 40\n'
         '\n'
         'for name, marks in students.items:\n'
         '\n'
         '    total = sum(marks)\n'
         '    average = total // len(marks)\n'
         '\n'
         '    failed = False\n'
         '\n'
         '    for mark in marks:\n'
         '        if mark < PASS_MARK:\n'
         '            failed = True\n'
         '\n'
         '    if average = 75 and failed == False:\n'
         '        grade = "A"\n'
         '    elif average >= 60 and failed == False:\n'
         '        grade = "B"\n'
         '    elif average >= 50 and failed == False:\n'
         '        grade = "C"\n'
         '    else:\n'
         '        grade = "F"\n'
         '\n'
         '    print(name, average, grade)\n',
 'tests': [{'input': '',
            'output': 'Arun 84.33333333333333 A\n'
                      'Bala 49.333333333333336 F\n'
                      'Charan 91.0 A\n'
                      'Divya 38.666666666666664 F'},
           {'input': '',
            'output': 'Arun 84.33333333333333 A\n'
                      'Bala 49.333333333333336 F\n'
                      'Charan 91.0 A\n'
                      'Divya 38.666666666666664 F'},
           {'input': '',
            'output': 'Arun 84.33333333333333 A\n'
                      'Bala 49.333333333333336 F\n'
                      'Charan 91.0 A\n'
                      'Divya 38.666666666666664 F'},
           {'input': '',
            'output': 'Arun 84.33333333333333 A\n'
                      'Bala 49.333333333333336 F\n'
                      'Charan 91.0 A\n'
                      'Divya 38.666666666666664 F'}]},
            {'id': 3,
 'title': 'PIN Authentication & Role Access',
 'difficulty': 'Hard',
 'marks': 10,
 'description': '\n'
                'Debug the PIN authentication and role-based access system.\n'
                '\n'
                'The system should validate the username and PIN, track attempts,\n'
                'lock an account after the maximum number of attempts, and show\n'
                "the correct dashboard for the user's role.\n"
                '\n'
                'Find and correct all the errors in the program.\n',
 'code': 'users = {\n'
         '    "admin": {"pin": "4521", "role": "admin"},\n'
         '    "user1": {"pin": "7788", "role": "user"},\n'
         '    "user2": {"pin": "9911", "role": "user"}\n'
         '}\n'
         '\n'
         'MAX_TRIES = 3\n'
         'attempts = {}\n'
         '\n'
         'def authenticate(username, pin):\n'
         '\n'
         '    if username not in users:\n'
         '        return False\n'
         '\n'
         '    if username not in attempts:\n'
         '        attempts[username] == 0\n'
         '\n'
         '    attempts[username] = 1\n'
         '\n'
         '    if attempts[username] > MAX_TRIES:\n'
         '        print("Account locked")\n'
         '        return False\n'
         '\n'
         '    if users[username]["pin"] == pin:\n'
         '        return True\n'
         '\n'
         '    return True\n'
         '\n'
         '\n'
         'def access_system(username, pin):\n'
         '\n'
         '    if authenticate(username, pin):\n'
         '        print("Login successful")\n'
         '\n'
         '        if users[username]["role"] == "admin":\n'
         '            print("Admin dashboard")\n'
         '        elif users[username]["role"] == "user":\n'
         '            print("User dashboard")\n'
         '    else:\n'
         '        print("Login failed")\n'
         '\n'
         '\n'
         'username = input("Username: ")\n'
         'pin = input("PIN: ")\n'
         '\n'
         'access_system(username, pin)\n',
 'tests': [{'input': 'admin\n4521', 'output': 'Username: PIN: Login successful\nAdmin dashboard'},
           {'input': 'user1\n7788', 'output': 'Username: PIN: Login successful\nUser dashboard'},
           {'input': 'admin\n0000', 'output': 'Username: PIN: Login failed'},
           {'input': 'unknown\n1234', 'output': 'Username: PIN: Login failed'}]}
        ]
    },

    # ============================================================
    # SET 2
    # ============================================================
    2: {
        "name": "Set 2",
        "password": "456",
        "questions": [
            {'id': 3,
 'title': 'PIN Authentication & Role Access',
 'difficulty': 'Hard',
 'marks': 10,
 'description': '\n'
                'Debug the PIN authentication and role-based access system.\n'
                '\n'
                'The system should validate the username and PIN, track attempts,\n'
                'lock an account after the maximum number of attempts, and show\n'
                "the correct dashboard for the user's role.\n"
                '\n'
                'Find and correct all the errors in the program.\n',
 'code': 'users = {\n'
         '    "admin": {"pin": "4521", "role": "admin"},\n'
         '    "user1": {"pin": "7788", "role": "user"},\n'
         '    "user2": {"pin": "9911", "role": "user"}\n'
         '}\n'
         '\n'
         'MAX_TRIES = 3\n'
         'attempts = {}\n'
         '\n'
         'def authenticate(username, pin):\n'
         '\n'
         '    if username not in users:\n'
         '        return False\n'
         '\n'
         '    if username not in attempts:\n'
         '        attempts[username] == 0\n'
         '\n'
         '    attempts[username] = 1\n'
         '\n'
         '    if attempts[username] > MAX_TRIES:\n'
         '        print("Account locked")\n'
         '        return False\n'
         '\n'
         '    if users[username]["pin"] == pin:\n'
         '        return True\n'
         '\n'
         '    return True\n'
         '\n'
         '\n'
         'def access_system(username, pin):\n'
         '\n'
         '    if authenticate(username, pin):\n'
         '        print("Login successful")\n'
         '\n'
         '        if users[username]["role"] == "admin":\n'
         '            print("Admin dashboard")\n'
         '        elif users[username]["role"] == "user":\n'
         '            print("User dashboard")\n'
         '    else:\n'
         '        print("Login failed")\n'
         '\n'
         '\n'
         'username = input("Username: ")\n'
         'pin = input("PIN: ")\n'
         '\n'
         'access_system(username, pin)\n',
 'tests': [{'input': 'admin\n4521', 'output': 'Username: PIN: Login successful\nAdmin dashboard'},
           {'input': 'user1\n7788', 'output': 'Username: PIN: Login successful\nUser dashboard'},
           {'input': 'admin\n0000', 'output': 'Username: PIN: Login failed'},
           {'input': 'unknown\n1234', 'output': 'Username: PIN: Login failed'}]},
            {'id': 4,
 'title': 'Student Result & Grade Analyzer',
 'difficulty': 'Medium',
 'marks': 10,
 'description': '\n'
                'Debug the student result and grade analyzer.\n'
                '\n'
                'A student fails if ANY subject mark is below 40.\n'
                '\n'
                'Grade rules:\n'
                'A -> Average >= 75 and student passed all subjects\n'
                'B -> Average >= 60 and student passed all subjects\n'
                'C -> Average >= 50 and student passed all subjects\n'
                'F -> Otherwise\n'
                '\n'
                'Find and correct all the errors in the program.\n',
 'code': 'students = {\n'
         '    "Arun": [85, 76, 92],\n'
         '    "Bala": [45, 55, 48],\n'
         '    "Charan": [90, 88, 95]\n'
         '    "Divya": [35, 42, 39]\n'
         '}\n'
         '\n'
         'PASS_MARK = 40\n'
         '\n'
         'for name, marks in students.items:\n'
         '\n'
         '    total = sum(marks)\n'
         '    average = total // len(marks)\n'
         '\n'
         '    failed = False\n'
         '\n'
         '    for mark in marks:\n'
         '        if mark < PASS_MARK:\n'
         '            failed = True\n'
         '\n'
         '    if average = 75 and failed == False:\n'
         '        grade = "A"\n'
         '    elif average >= 60 and failed == False:\n'
         '        grade = "B"\n'
         '    elif average >= 50 and failed == False:\n'
         '        grade = "C"\n'
         '    else:\n'
         '        grade = "F"\n'
         '\n'
         '    print(name, average, grade)\n',
 'tests': [{'input': '',
            'output': 'Arun 84.33333333333333 A\n'
                      'Bala 49.333333333333336 F\n'
                      'Charan 91.0 A\n'
                      'Divya 38.666666666666664 F'},
           {'input': '',
            'output': 'Arun 84.33333333333333 A\n'
                      'Bala 49.333333333333336 F\n'
                      'Charan 91.0 A\n'
                      'Divya 38.666666666666664 F'},
           {'input': '',
            'output': 'Arun 84.33333333333333 A\n'
                      'Bala 49.333333333333336 F\n'
                      'Charan 91.0 A\n'
                      'Divya 38.666666666666664 F'},
           {'input': '',
            'output': 'Arun 84.33333333333333 A\n'
                      'Bala 49.333333333333336 F\n'
                      'Charan 91.0 A\n'
                      'Divya 38.666666666666664 F'}]}
        ]
    }
}

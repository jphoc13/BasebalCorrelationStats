from pybaseball import statcast
"DOCS: https://pypi.org/project/pybaseball/"


if __name__ == '__main__':
    "FIX: https://stackoverflow.com/questions/15900366/all-example-concurrent-futures-code-is-failing-with-brokenprocesspool"
    data = statcast(start_dt='2017-06-24', end_dt='2017-06-27')
    data.head(2)
    print(data)

# A line of code wiht the pound sign at the beginning, removes the code form being run
# in the program.  This is called a comment.

# This is a class, very much like a house blueprint
class Person:

    name = ""
    age = ""

def print_meeting_attendees():

    person1 = Person()  # This is an object, very similar to the home built from the blueprint
    person1.name = "Tim"
    person1.age = '42?'

    person2 = Person()
    person2.name = "JP"
    person2.age = '42'

    print(f"in this meeting: {person1.name} and {person2.name}")

# print_meeting_attendees()
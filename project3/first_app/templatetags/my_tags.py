from django import template
from django.template.loader import get_template

register = template.Library()

def my_template(value, arg):
    if arg == 'change':
        value = 'abdul matin'
        return value
    
    if arg == 'title':
        return value.upper()
    
def show_courses():
    courses = [
        {
            'id': 101,
            'name': 'C',
            'teacher': 'Rakib'
        },
        {
            'id': 102,
            'name': 'C++',
            'teacher': 'Sakib'
        },
        {
            'id': 103,
            'name': 'C#',
            'teacher': 'Jakib'
        }
    ]
    return {'courses':courses}

courses_template = get_template('courses_template.html')
register.inclusion_tag(courses_template)(show_courses)    
register.filter('change_name', my_template)
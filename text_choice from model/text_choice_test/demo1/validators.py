from django.core.exceptions import ValidationError

def validate_demo_choice(value):
    if value not in ['test1','test2','test3','test4']:
        raise ValidationError(f'Invalid choice')
    else:
        return value

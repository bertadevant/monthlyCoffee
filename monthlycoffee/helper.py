from django.core.exceptions import ObjectDoesNotExist

def get_object_or_none(klass, *args, **kwargs):
    try:
        return klass.objects.get(*args, **kwargs)
    except ObjectDoesNotExist:
        return None
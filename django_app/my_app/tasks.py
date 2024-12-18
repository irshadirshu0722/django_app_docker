from celery import shared_task
@shared_task
def incrementModal():
    from .models import TestModal
    instance,created  = TestModal.objects.get_or_create(id=1,defaults={'count':1})
    if not created:
      instance.count+=1
      instance.save()
    return "Done"

@shared_task
def scheduledIncrementModal():
  from .models import TestModal
  instance,created  = TestModal.objects.get_or_create(id=1,defaults={'count':1})
  if not created:
    instance.count+=1
    instance.save()
  return "Done"
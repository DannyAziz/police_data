from django.db import models


# Why all the blank=True and null=True?
# The police API returns null for a lot of these things
class StopAndSearch(models.Model):
    force = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    involved_person = models.BooleanField(default=True)
    datetime = models.DateTimeField(blank=True, null=True)
    operation = models.BooleanField(default=False)
    operation_name = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    age_range = models.TextField(blank=True, null=True)
    self_defined_ethnicity = models.TextField(blank=True, null=True)
    officer_defined_ethnicity = models.TextField(blank=True, null=True)
    legislation = models.TextField(blank=True, null=True)
    object_of_search = models.TextField(blank=True, null=True)
    outcome = models.TextField(blank=True, null=True)
    outcome_linked_to_object_of_search = models.TextField(blank=True, null=True)
    removal_of_more_than_outer_clothing = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Stop and Search - {force}, {type}".format(force=self.force, type=self.type)


class StopAndSearchLocation(models.Model):
    stop_and_search = models.OneToOneField(StopAndSearch, related_name="location")
    latitude = models.TextField()
    longitude = models.TextField()
    street_text = models.TextField()

    def __str__(self):
        return "Stop and Search {id} - Location".format(id=self.stop_and_search.id)

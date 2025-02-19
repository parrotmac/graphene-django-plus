from django.db import models

from graphene_django_plus.models import GuardedModel


class Project(models.Model):

    name = models.CharField(
        max_length=255,
    )
    due_date = models.DateField(
        null=True,
        blank=True,
        default=None,
    )
    cost = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        null=True,
        blank=True,
        default=None,
    )


class Milestone(models.Model):

    name = models.CharField(
        max_length=255,
    )
    due_date = models.DateField(
        null=True,
        blank=True,
        default=None,
    )
    project = models.ForeignKey(
        Project,
        related_name="milestones",
        related_query_name="milestone",
        on_delete=models.CASCADE,
    )


class Issue(GuardedModel):
    class Meta:
        permissions = [
            ("can_read", "Can read the issue's information."),
            ("can_write", "Can update the issue's information."),
        ]

    kinds = {
        "b": "Bug",
        "f": "Feature",
    }

    name = models.CharField(
        max_length=255,
    )
    kind = models.CharField(
        verbose_name="kind",
        help_text="the kind of the issue",
        max_length=max(len(t) for t in kinds),
        choices=list(kinds.items()),
        default=None,
        blank=True,
        null=True,
    )
    priority = models.IntegerField(
        default=0,
    )
    milestone = models.ForeignKey(
        Milestone,
        related_name="issues",
        related_query_name="issue",
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL,
    )


class MilestoneComment(models.Model):

    text = models.CharField(
        max_length=255,
    )
    milestone = models.ForeignKey(
        Milestone,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

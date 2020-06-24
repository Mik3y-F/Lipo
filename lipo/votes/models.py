import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PsvReviewVote(models.Model):

    id = models.UUIDField(_("Review Vote Id"), primary_key=True, default=uuid.uuid4,
                          editable=False)
    author = models.ForeignKey("users.User", verbose_name=_("Review Vote Author"),
                               on_delete=models.CASCADE)
    review = models.ForeignKey("reviews.PsvReview", verbose_name=_("Review being voted for"),
                               on_delete=models.CASCADE)
    type = models.ForeignKey("votes.VoteType", verbose_name=_("Type of Review Vote"),
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Review Vote")
        verbose_name_plural = _("Review Votes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("review_vote:detail", kwargs={"pk": self.pk})


class VoteType(models.Model):

    DOWN_VOTE = 'down'
    UP_VOTE = 'up'
    VOTE_TYPE = [
        (DOWN_VOTE, _('Vote is a down vote')),
        (UP_VOTE, _('Vote is an up vote')),
    ]

    name = models.CharField(
        max_length=32,
        choices=VOTE_TYPE,
    )psvcollections

    class Meta:
        verbose_name = _("VoteType")
        verbose_name_plural = _("VoteTypes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vote_type:detail", kwargs={"pk": self.pk})

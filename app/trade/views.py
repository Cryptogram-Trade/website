from django.views.generic.base import TemplateView
from .models import ShrimpyLeader


class LeadersView(TemplateView):
    template_name = "trade/leaders.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["leaders"] = ShrimpyLeader.objects.order_by("-followers_count")
        return ctx

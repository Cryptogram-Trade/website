from django.views.generic import TemplateView


class Article:
  def __init__(self, title, body, image, slug):
    self.title = title
    self.body = body
    self.slug = slug
    self.image = image


class ListView(TemplateView):
    template_name = "blog/list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["articles"] = [
          Article(
            title="Shrimpy with Binance for US citizens",
            image="https://mlnjwsydcfjh.i.optimole.com/lv2uaCs-tc4l_59X/w:300/h:200/q:auto/https://news.trijo.co/wp-content/uploads/2019/09/binance-i-usa-oppnar-for-registrering-nasta-vecka.jpg",
            body="Binance clients based in the US have a special Binance platform that is hosted on Binance.us. If you're a US citizen, you must register on Binance.us. Binance.com is reserved for non US citizens.",
            slug="shrimpy-for-binance-us-users"
          )
        ]
        return ctx


class ArticleView(TemplateView):
    def get_template_names(self):
        slug = self.kwargs.get("slug")
        return f"blog/{slug}.html"

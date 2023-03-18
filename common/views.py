class TitleMixin:  # делаем миксин что бы использовать во всех context['title']
    title = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context

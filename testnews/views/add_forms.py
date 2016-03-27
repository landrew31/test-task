from django.forms import ModelForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView


from ..models import News, Comments

class NewsCreateForm(ModelForm):
	class Meta:
		model = News
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(NewsCreateForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper(self)

		# set form tag attributes

		self.helper.form_action = reverse('add_news')
		self.helper.form_method = 'POST'

		# set form field properties
		self.helper.help_text_inline = True
		self.helper.html5_required = False
		self.helper.label_class = ''
		self.helper.field_class = ''

		# add buttons
		self.helper.layout.append(FormActions(
			Submit('add_button', 'Save News', css_class="waves-effect waves-light btn right green darken-2"),
			Submit('cancel_button', 'Cancel', css_class="waves-effect waves-light btn right red darken-2"),
		))

class NewsCreateView(SuccessMessageMixin, CreateView):
	"""docstring for NewsCreateForm"""

	model = News
	template_name = 'testnews/add_news.html'
	form_class = NewsCreateForm
	success_url = reverse_lazy("home")

	def get_context_data(self, **kwargs):
		context = super(NewsCreateView, self).get_context_data(**kwargs)
		context['page_title'] = 'Add News'
		return context

	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button') is not None:

			return HttpResponseRedirect(self.success_url)
		else:
			return super(NewsCreateView, self).post(request, *args, **kwargs)




def add_comment(request, pk):

	news = get_object_or_404(News, pk=pk)
	if request.method == "POST":

		if request.POST.get('add_comment') is not None:

			commented_by = request.POST.get('commented_by', '').strip()

			comment_content = request.POST.get('comment_content')

			data = {'commented_by': commented_by,
			    'comment_content': comment_content,
				'news_commented': news}

			comment = Comments(**data)
			comment.save()

			return redirect(reverse('one_news_show', kwargs={'pk': news.pk}))

		else:
			return HttpResponseRedirect(reverse('one_news_show', kwargs={'pk': news.pk}))
	else:
		return render(request, reverse_lazy('one_news_show', kwargs={'pk': news.pk}))

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from .models import Question, Choice, Private_Message
from django.views import generic
from .forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

def MessagesView(request):
    latest_message_list = Private_Message.objects.order_by('-sent_date')[:2]
    context = {'latest_message_list': latest_message_list}
    return render(request, 'polls/message_list.html', context)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
                      'question': p,
                      'error_message': "You didn't select a choice.",
                      })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def create_message(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MessageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            pm = Private_Message(sender_id = form.cleaned_data['sender_id'],
                                 receiver_id = form.cleaned_data['receiver_id'],
                                 message_text = form.cleaned_data['message_text'],
                                 sent_date = timezone.now())
            pm.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/messages/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MessageForm()
    
    return render(request, 'polls/message_pane.html', {'form': form})
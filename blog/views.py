from django.shortcuts import render, get_object_or_404
from .models import Category, Trending, Hotnews, Editor, Tech, Article, Suggested, Sets
from .forms import FeedbackForm

 
def contact(request):
    variable = 'Mysterious Science'
    trending = []
    for i in range(1,5):
        trending.append(Trending.objects.get(trending_id=i))

    all_hotnews = []
    hotnews = []
    hotnews.append(Hotnews.objects.get(hotnews_id=1))
    for j in range(2,6):
        all_hotnews.append(Hotnews.objects.get(hotnews_id=j))
    
    all_category = Category.objects.all()
    all_trending = Trending.objects.all()
    all_editor = Editor.objects.all()
    all_tech = Tech.objects.all()
    
    context = {
        'all_category' : all_category,
        'all_trending' : all_trending,
        'trending' : trending,
        'hotnews' : hotnews,
        'all_hotnews' : all_hotnews,
        'all_editor' : all_editor,
        'all_tech' : all_tech,
        'variable' : variable,
        
    }
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'blog/thanks.html', context)
    else:
        form = FeedbackForm()
    return render(request, 'blog/contact.html', {'form': form})


def index(request):
    variable = 'Mysterious Science'

    trending = []
    for i in range(1,5):
        trending.append(Trending.objects.get(trending_id=i))

    all_hotnews = []
    hotnews = []
    hotnews.append(Hotnews.objects.get(hotnews_id=1))
    for j in range(2,6):
        all_hotnews.append(Hotnews.objects.get(hotnews_id=j))
    
    all_category = Category.objects.all()
    all_trending = Trending.objects.all()
    all_editor = Editor.objects.all()
    all_tech = Tech.objects.all()
    
    context = {
        'all_category' : all_category,
        'all_trending' : all_trending,
        'trending' : trending,
        'hotnews' : hotnews,
        'all_hotnews' : all_hotnews,
        'all_editor' : all_editor,
        'all_tech' : all_tech,
        'variable' : variable
    }
    return render(request, 'blog/index.html', context )


def category(request):
    variable = 'Mysterious SCience'
    all_hotnews = []
    hotnews = []
    hotnews.append(Hotnews.objects.get(hotnews_id=1))
    for j in range(2,6):
        all_hotnews.append(Hotnews.objects.get(hotnews_id=j))
    
    article1 = []
    for a in range(1,2*Category.objects.all().count(),2):
        category = Category.objects.get(category_id=(a+1)/2)
        article1.append((category.catlist_set.all().get(catlist_id=a),category.catlist_set.all().get(catlist_id=a+1)))
       
    all_category = Category.objects.all()
    all_editor = Editor.objects.all()
    all_tech = Tech.objects.all()
    all_article = Article.objects.all()
    
    context = {
        'all_category' : all_category,
        'hotnews' : hotnews,
        'all_hotnews' : all_hotnews,
        'all_editor' : all_editor,
        'all_tech' : all_tech,
        'all_article' : all_article,
        'article1' : article1,
        'variable' : variable
    }
    return render(request, 'blog/category.html', context )



def detail(request, category_id):
    category = Category.objects.get(category_id=category_id)
    variable = 'Mysterious Science | ' + category.category_name
    
    all_hotnews = []
    hotnews = []
    hotnews.append(Hotnews.objects.get(hotnews_id=1))
    for j in range(2,6):
        all_hotnews.append(Hotnews.objects.get(hotnews_id=j))
    
    all_category = Category.objects.all()
    all_trending = Trending.objects.all()
    all_editor = Editor.objects.all()
    all_tech = Tech.objects.all()
    
    
    context = {
        'all_category' : all_category,
        'hotnews' : hotnews,
        'all_hotnews' : all_hotnews,
        'all_editor' : all_editor,
        'all_tech' : all_tech,
        'category': category,
        'variable' : variable
        
    }

    return render(request, 'blog/detail.html', context)

def article(request, article_title):
    article = Article.objects.get(article_title=article_title)
    variable = article.article_title + ' | Mysterious Science'

    if article.article_id == 1:
        nid = 7
        pid = 6
    elif article.article_id == 2:
        nid = 9
        pid = 8
    else:
        nid = article.article_id -1
        pid = article.article_id -2
    next_article = Article.objects.get(article_id = nid)
    previous_article = Article.objects.get(article_id = pid)

    all_hotnews = []
    hotnews = []
    hotnews.append(Hotnews.objects.get(hotnews_id=1))
    for j in range(2,6):
        all_hotnews.append(Hotnews.objects.get(hotnews_id=j))
   
    all_tech = Tech.objects.all()
    all_suggested = Suggested.objects.all()

    context = {
        'article' : article,
        'next_article' : next_article,
        'previous_article' : previous_article,
        'hotnews' : hotnews,
        'all_hotnews' : all_hotnews,
        'all_tech' : all_tech,
        'all_suggested' : all_suggested,
        'variable' : variable
    }
    return render(request, 'blog/article.html', context )

    
def quizcat(request):
    variable = 'Mysterious Science - Quizzes'

    all_category = Category.objects.all()
    
    context = {
        'all_category' : all_category,  
        'variable' : variable      
    }
    return render(request, 'blog/quizcat.html', context )

    
def sets(request,category_name):
    category = Category.objects.get(category_name=category_name)
    all_category = Category.objects.all()
    all_set = Sets.objects.all()

    variable = 'Mysterious Science - Quizzes | '+category.category_name
    
    context = {
        'all_category' : all_category,
        'category' : category,    
        'all_set' : all_set, 
        'variable' : variable  
    }
    return render(request, 'blog/sets.html', context )

    
def quiz(request,set_id):
    all_category = Category.objects.all()
    set_info = Sets.objects.get(set_id = set_id)
    variable = 'Mysterious Science | Quiz on ' + set_info.set_topic

    if set_id == Sets.objects.all().count():
        next_id = 1
    else:
        next_id = set_id+ 1
    
    context = {
        'all_category' : all_category,
        'set_info' : set_info, 
        'next_id' : next_id, 
        'variable' : variable  
    }
    return render(request, 'blog/quiz.html', context )

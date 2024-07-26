from django.shortcuts import render
from rest_framework import viewsets
from portfolio.models import GeneralInfo
from .models import Post, Comment, PostCategory
from .forms import CommentForm
from django.views.decorators.cache import cache_page
from .serializers import PostSerializer, CategorySerializer, CommentSerializer

# Create your views here.
def index(request):
    
    general_info = GeneralInfo.objects.all()
    
    context = {
        'company_name': 'general_info.company_name',
        'company_logo': 'general_info.company_logo',
        'company_address': 'general_info.company_address',
        'company_phone': 'general_info.company_phone',
        'company_email': 'general_info.company_email',
        'company_website': 'general_info.company_website',
        'company_facebook': 'general_info.company_facebook',
        'company_twitter': 'general_info.company_twitter',
        'company_linkedin': 'general_info.company_linkedin',
        'company_instagram': 'general_info.company_instagram',
        'company_youtube': 'general_info.company_youtube',
        'company_tiktok': 'general_info.company_tiktok',
        'company_about': 'general_info.company_about',
        'company_mission': 'general_info.company_mission',
        'company_vision': 'general_info.company_vision',
    }
    
    return render(request, 'index.html', context)



@cache_page(60 * 10)
def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 10) # 10 posts in each page
    page = request.GET.get('page')
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
        
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
        
    return render(request,'post_list.html',{'posts':posts, page:'pages','tag':tag})


@cache_page(60 * 10)
def post_detail(request, post):
    post=get_object_or_404(Post,slug=post,status='published')

    # List of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            # redirect to same page and focus on that comment
            return redirect(post.get_absolute_url()+'#'+str(new_comment.id))
        else:
            comment_form = CommentForm()

    return render(request, 'post_detail.html',{'post':post,'comments': comments,'comment_form':comment_form})


@cache_page(60 * 10)
def reply_page(request):
    if request.method == "POST":

        form = CommentForm(request.POST)

        if form.is_valid():
            post_id = request.POST.get('post_id')  # from hidden input
            parent_id = request.POST.get('parent')  # from hidden input
            post_url = request.POST.get('post_url')  # from hidden input

            reply = form.save(commit=False)
    
            reply.post = Post(id=post_id)
            reply.parent = Comment(id=parent_id)
            reply.save()

            return redirect(post_url+'#'+str(reply.id))

    return redirect("/")



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = PostCategory.objects.all()
    serializer_class = CategorySerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
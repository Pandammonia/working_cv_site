from django.shortcuts import render
from .models import Post, Reply

def index(request):
	posts = Post.objects.order_by('added')
	context = {'posts':posts}
	return render(request, 'board/index.html', context)

def postdetail(request, post_id):
	post = Post.objects.get(id=post_id)
	replies = post.reply_set.order_by('added')
	context = {'post':post, 'replies':replies}
	return render(request, 'board/detail.html', context)
# Create your views here.

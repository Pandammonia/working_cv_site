from django.shortcuts import render, redirect
from .models import Post, Reply
from .forms import PostForm, ReplyForm

def index(request):
	posts = Post.objects.order_by('added')
	context = {'posts':posts}
	return render(request, 'board/index.html', context)

def postdetail(request, slug):
	post = Post.objects.get(slug=slug)
	replies = post.reply_set.order_by('added')
	context = {'post':post, 'replies':replies}
	return render(request, 'board/detail.html', context)

def newmsg(request):
	if request.method != "POST":
		form = PostForm()
	else:
		form = PostForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('board:index')
	context = {'form': form}
	return render(request, 'board/newmsg.html', context)

def newreply(request, post_id):
	post = Post.objects.get(id=post_id)
	if request.method != "POST":
		form = ReplyForm()
	else:
		form = ReplyForm(data=request.POST)
		if form.is_valid():
			newreply= form.save(commit=False)
			newreply.post = post
			newreply.save()
			return redirect('board:index')
	context = {'form':form, 'post':post }
	return render(request, 'board/newreply.html', context)



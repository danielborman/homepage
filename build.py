top = open('template/top.html').read()
index = open('content/index.html').read()
projects = open('content/projects.html').read()
blog = open('content/blog.html').read()
bottom = open('template/bottom.html').read()

index = top + index + bottom
blog = top + blog + bottom
projects = top + projects + bottom
open('index.html', 'w+').write(art)
open('projects.html', 'w+').write(blog)
open('blog.html', 'w+').write(index)


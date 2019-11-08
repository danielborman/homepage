top = open('templates/top.html').read()
index = open('content/index.html').read()
projects = open('content/projects.html').read()
blog = open('content/blog.html').read()
bottom = open('templates/bottom.html').read()

index = top + index + bottom
blog = top + blog + bottom
projects = top + projects + bottom
open('index.html', 'w+').write(index)
open('projects.html', 'w+').write(projects)
open('blog.html', 'w+').write(blog)


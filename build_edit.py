def main():
    base = open("templates/base.html").read()
    
pages = [
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "About Me",
    },
    {
        "filename": "content/projects.html",
        "output": "docs/projects.html",
        "title": "My Projects",
    },
    {
        "filename": "content/blog.html",
        "output": "docs/blog.html",
        "title": "My programming blog",
    },
]


if __name__  == "__main__":
    main()
    
for page in pages:
    print(page)







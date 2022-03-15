# LastTag utility

After you clone the repo, to use lasttag you need to install dependencies first

`pip install -r requirements.txt`

it can be used right away with
`python lasttag.py <path to repo>`
but I guess we all feel it is a bit cumbersome

so:
```
sudo cp lasttag.py /usr/local/bin/lasstag
sudo chmod +x /usr/local/bin/lasstag
```

Now we can use it as simply as `lasttag .` if our pwd is the repo itself of course

The **output** is the latest tag. Be aware it is not a tag with highest version but the tag pushed last.


So if we call the lasttag on itself
```
lasttag ~/projects/lasttag
```

we get
```
0.0.0-dev
```
(now when I'm writing this)

*ToDo*: add parameter for fetching tags from remote origin

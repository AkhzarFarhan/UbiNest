# usage: make git m='your comment'
git:
	git checkout dev
	git add .
	git commit -m "$m"
	git push origin dev
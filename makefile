# usage: make git m='your comment'
git:
	git checkout dev
	git add .
	git commit -m "$m"
	git push origin dev

# usage: make merge
merge:
	git checkout main
	git merge dev
	git push origin main
	git checkout dev
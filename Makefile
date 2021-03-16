default:
	false

new:
	mkdir -p miniposts/$$(date +%Y)/$$(date +%Y-%m-%d)/
	touch miniposts/$$(date +%Y)/$$(date +%Y-%m-%d)/new-post.md
